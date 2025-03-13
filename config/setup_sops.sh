#!/bin/bash

set -e  # Exit on any error

### --- Dynamically Find and Navigate to Project Root --- ###
PROJECT_ROOT=$(realpath "$(dirname "$0")/..")
cd "$PROJECT_ROOT" || exit 1
echo "Navigated to project root: $PROJECT_ROOT"
cd config

CONFIG_DIR="$PROJECT_ROOT/config"
SOPS_DIR="$CONFIG_DIR/sops"
AGE_DIR="$SOPS_DIR/age"
AGE_KEY_FILE="$AGE_DIR/keys.txt"
SOPS_CONFIG="$CONFIG_DIR/.sops.yaml"
AWS_CREDENTIALS="$CONFIG_DIR/aws_credentials.yaml"

### --- Prompt for AWS Credentials --- ###
read -p "Enter AWS Access Key ID: " AWS_ACCESS_KEY
read -s -p "Enter AWS Secret Access Key: " AWS_SECRET_KEY
echo
read -p "Enter AWS Region: " AWS_REGION

### --- Remove Existing SOPS Configuration and Credentials --- ###
rm -rf "$SOPS_DIR" "$SOPS_CONFIG" "$AWS_CREDENTIALS"

### --- Recreate Directory Structure --- ###
mkdir -p "$AGE_DIR"

### --- Download and Install SOPS --- ###
SOPS_DEB="sops_3.9.4_amd64.deb"
SOPS_URL="https://github.com/getsops/sops/releases/download/v3.9.4/$SOPS_DEB"

wget -q "$SOPS_URL" -O "/tmp/$SOPS_DEB"
sudo dpkg -i "/tmp/$SOPS_DEB"
rm "/tmp/$SOPS_DEB"

### --- Install Age Encryption Tool --- ###
sudo apt-get update && sudo apt-get install -y age

### --- Generate New Age Encryption Key --- ###
age-keygen -o "$AGE_KEY_FILE"
AGE_PUBLIC_KEY=$(grep -o "age1[0-9a-zA-Z]*" "$AGE_KEY_FILE")

### --- Set SOPS to Use the New Key --- ###
export SOPS_AGE_KEY_FILE="$AGE_KEY_FILE"
echo "export SOPS_AGE_KEY_FILE=$AGE_KEY_FILE" >> ~/.bashrc
source ~/.bashrc

### --- Create New SOPS Configuration --- ###
cat <<EOF > "$SOPS_CONFIG"
creation_rules:
  - path_regex: '.*aws_credentials.yaml$'
    encrypted_regex: '.*'
    key_groups:
      - age:
          - "$AGE_PUBLIC_KEY"
EOF

### --- Set Correct Permissions --- ###
chmod 600 "$AGE_KEY_FILE" "$SOPS_CONFIG"

### --- Create New AWS Credentials File --- ###
cat <<EOF > "$AWS_CREDENTIALS"
aws:
  access_key_id: $AWS_ACCESS_KEY
  secret_access_key: $AWS_SECRET_KEY
  region: $AWS_REGION
EOF

### --- Encrypt AWS Credentials --- ###
sops --encrypt --age "$AGE_PUBLIC_KEY" --output "$AWS_CREDENTIALS" "$AWS_CREDENTIALS"

### --- Test Decryption --- ###
sops --decrypt "$AWS_CREDENTIALS" >/dev/null && echo "✅ SOPS setup, key regeneration, and encryption completed successfully."
