### **1.1 Configurations**

---

### **1.1.1 `config.yaml` — Global Settings, Paths, and Hyperparameters**
---

**Purpose:**  
The `config.yaml` file is the **centralized configuration hub** for your entire project. It defines project-wide settings, data paths, model hyperparameters, agent configurations, and environment-specific details. By consolidating these parameters in a single file, you improve **maintainability**, **scalability**, and **consistency** across modules.  

Instead of hardcoding values directly into Python scripts, referencing this file ensures changes are propagated consistently throughout the project.  

---

**Recommended Structure:**
```yaml
# General project settings
project:
  name: "Autonomous MLOps Pipeline"
  version: "1.0.0"

# Data paths for all major data stages
paths:
  raw_data: "./data/raw"
  processed_data: "./data/processed"
  synthetic_data: "./data/synthetic"
  models: "./artifacts/models"
  logs: "./logs"

# Model parameters for CatBoost model
model:
  type: "CatBoost"
  hyperparameters:
    learning_rate: 0.01
    max_depth: 6
    iterations: 1000
    early_stopping_rounds: 50
  optimization:
    algorithm: "Optuna"
    n_trials: 100
    timeout: 3600  # 1 hour for tuning time limit

# Autonomous agents' configuration
agents:
  data_ingestion_agent:
    batch_size: 10000
    retries: 3
  drift_detection_agent:
    threshold: 0.05
  retraining_agent:
    trigger_drift_threshold: 0.07

# Logging configuration (links to `logging.yaml`)
logging:
  level: "INFO"

# AWS S3 settings for model and data storage
aws:
  bucket_name: "autonomous-mlops-pipelinexw"
  region: "us-east-1"
```

---

**Key Best Practices for `config.yaml`:**

- Avoid hardcoding paths, file names, or parameters directly in code. This simplifies updates when paths or parameters change.  
- Use **YAML anchors** (`&` for defining values) and **aliases** (`*` for referencing them) to reduce duplication across sections.  
- Add **meaningful comments** to describe key configuration entries to improve clarity for future developers.  
- Do not include **sensitive information** (e.g., passwords, tokens, keys) in `config.yaml`. Such data should be stored securely in `.env` or encrypted files like `aws_credentials.yaml`.

---

### **1.1.2 `logging.yaml` — Log Formatting and Control**
---

**Purpose:**  
The `logging.yaml` file standardizes your project's logging structure. A centralized logging configuration improves visibility into the system’s behavior, aids debugging, and ensures traceability.  

This file defines:  
- **Log levels** (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`) to control verbosity.  
- **Log formatters** to define log structure for consistency.  
- **Handlers** to direct logs to multiple outputs (e.g., console, file).  
- **Rotating log files** to prevent excessive log growth.  

---

**Recommended Structure:**
```yaml
version: 1
disable_existing_loggers: False

formatters:
  standard:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  detailed:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s"

handlers:
  console:
    class: logging.StreamHandler
    formatter: standard
    level: INFO
  file:
    class: logging.FileHandler
    formatter: detailed
    level: DEBUG
    filename: "./logs/system_logs.log"
  rotation_file:
    class: logging.handlers.TimedRotatingFileHandler
    formatter: detailed
    level: DEBUG
    filename: "./logs/rotated_logs.log"
    when: midnight
    interval: 1
    backupCount: 7

loggers:
  root:
    level: INFO
    handlers: [console, file]
```

---

**Key Best Practices for `logging.yaml`:**

- Use **multiple log levels**:  
  - `DEBUG` for development insights.  
  - `INFO` for general system behavior.  
  - `WARNING`, `ERROR`, and `CRITICAL` for severe issues.  
- Use **log rotation** to archive old logs, preventing large log files.  
- Include **detailed context** (e.g., module name, function name, and line number) to improve traceability during debugging.  
- Use different log files for:  
  - System logs  
  - Drift detection logs  
  - Model performance logs  
- Ensure logs are generated for key checkpoints such as data ingestion, preprocessing, training, and inference.

---


### **1.1.3 `aws_credentials.yaml` — Encrypted AWS Credentials (Updated for IAM User without MFA)**

---

### **Step 1: Create an AWS IAM User via CLI**

Since you’re opting for an IAM user without MFA, follow these steps to create a new user with the necessary permissions for your project.

---

**1. Create the IAM User:**
```bash
aws iam create-user --user-name autonomous-pipeline-user
```

---

**2. Attach Required Permissions:**

For this project, the following permissions are essential:

- **`AmazonS3FullAccess`** — Full access to manage S3 storage.
- **`AmazonEC2FullAccess`** — For managing AWS ECS deployment.
- **`AWSLambda_FullAccess`** — For Lambda automation (if required).
- **`CloudWatchFullAccess`** — For enhanced monitoring.
- **`AmazonSNSFullAccess`** — For alerts and notifications.

Run the following command for each policy:

```bash
aws iam attach-user-policy \
    --user-name autonomous-pipeline-user \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

Repeat the command for each required policy.  

---

**3. Generate Access Keys:**
```bash
aws iam create-access-key --user-name autonomous-pipeline-user
```

This command outputs:

```json
{
    "AccessKey": {
        "UserName": "autonomous-pipeline-user",
        "AccessKeyId": "AKIAEXAMPLEID",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "Status": "Active",
        "CreateDate": "2025-03-13T10:30:00Z"
    }
}
```

**Important:** Save these credentials securely, as the `SecretAccessKey` will not be shown again.

---

### **Step 2: Encrypt AWS Credentials for `aws_credentials.yaml`**  

Since you won’t use MFA, encrypting your AWS credentials is crucial to protect sensitive information. This guide will walk you through securing your `aws_credentials.yaml` file using `sops`.  

---

## **Step 2.1: Install `sops` (YAML Encryption Tool)**  

`sops` is a powerful tool designed for encrypting YAML, JSON, and other structured data formats securely. It’s highly effective for protecting sensitive keys and credentials.  

### **Installation on Linux (Ubuntu/Debian)**
```bash
sudo apt-get update
sudo apt-get install sops
```

### **Manual Installation (if package is unavailable)**
Download and install `sops` manually:  
```bash
wget -O sops.deb "https://github.com/getsops/sops/releases/download/v3.9.4/sops_3.9.4_amd64.deb"
sudo dpkg -i sops.deb
rm sops.deb
```

### **Installation on Windows (via WSL)**  
If you are working in **WSL (Windows Subsystem for Linux)**, use the Ubuntu installation method above.  

### **Installation on macOS**  
```bash
brew install sops
```


### **Step 2: Encrypt AWS Credentials for `aws_credentials.yaml`**  

Since you won’t use MFA, encrypting your AWS credentials is crucial to protect sensitive information. This guide will walk you through securing your `aws_credentials.yaml` file using `sops`.  

---

## **Step 2.1: Install `sops` (YAML Encryption Tool)**  

`sops` is a powerful tool designed for encrypting YAML, JSON, and other structured data formats securely. It’s highly effective for protecting sensitive keys and credentials.  

### **Installation on Linux (Ubuntu/Debian)**
```bash
sudo apt-get update
sudo apt-get install sops
```

### **Manual Installation (if package is unavailable)**
Download and install `sops` manually:  
```bash
wget -O sops.deb "https://github.com/getsops/sops/releases/download/v3.9.4/sops_3.9.4_amd64.deb"
sudo dpkg -i sops.deb
rm sops.deb
```

### **Installation on Windows (via WSL)**  
If you are working in **WSL (Windows Subsystem for Linux)**, use the Ubuntu installation method above.  

### **Installation on macOS**  
```bash
brew install sops
```

---

## **Step 2.2: Automate AWS Credentials Encryption with SOPS**  
This script dynamically **generates, encrypts, and verifies** an AWS credentials file using SOPS and Age encryption. It ensures that sensitive credentials are never stored in plaintext.

### **Script for AWS Credentials Encryption**
```bash
#!/bin/bash

### --- Step 2.2: Encrypt AWS Credentials --- ###

# Navigate to the Project Root
PROJECT_ROOT=$(realpath "$(dirname "$0")/..")
cd "$PROJECT_ROOT" || exit 1
cd config

# Define Configuration Paths
CONFIG_DIR="$PROJECT_ROOT/config"
SOPS_DIR="$CONFIG_DIR/sops"
AGE_DIR="$SOPS_DIR/age"
AGE_KEY_FILE="$AGE_DIR/keys.txt"
SOPS_CONFIG="$CONFIG_DIR/.sops.yaml"
AWS_CREDENTIALS="$CONFIG_DIR/aws_credentials.yaml"

# Prompt for AWS Credentials
read -p "Enter AWS Access Key ID: " AWS_ACCESS_KEY
read -s -p "Enter AWS Secret Access Key: " AWS_SECRET_KEY
echo
read -p "Enter AWS Region: " AWS_REGION

# Remove Existing Setup
rm -rf "$SOPS_DIR" "$SOPS_CONFIG" "$AWS_CREDENTIALS"
mkdir -p "$AGE_DIR"

# Generate Age Encryption Key
age-keygen -o "$AGE_KEY_FILE"
AGE_PUBLIC_KEY=$(grep -o "age1[0-9a-zA-Z]*" "$AGE_KEY_FILE")

# Configure SOPS to Use Age Key
export SOPS_AGE_KEY_FILE="$AGE_KEY_FILE"
echo "export SOPS_AGE_KEY_FILE=$AGE_KEY_FILE" >> ~/.bashrc
source ~/.bashrc

# Create SOPS Configuration
cat <<EOF > "$SOPS_CONFIG"
creation_rules:
  - path_regex: '.*aws_credentials.yaml$'
    encrypted_regex: '.*'
    key_groups:
      - age:
          - "$AGE_PUBLIC_KEY"
EOF

# Set Permissions
chmod 600 "$AGE_KEY_FILE" "$SOPS_CONFIG"

# Create AWS Credentials File
cat <<EOF > "$AWS_CREDENTIALS"
aws:
  access_key_id: $AWS_ACCESS_KEY
  secret_access_key: $AWS_SECRET_KEY
  region: $AWS_REGION
EOF

# Encrypt AWS Credentials
sops --encrypt --age "$AGE_PUBLIC_KEY" --output "$AWS_CREDENTIALS" "$AWS_CREDENTIALS"

# Verify Encryption
sops --decrypt "$AWS_CREDENTIALS" >/dev/null && echo "✅ AWS Credentials encrypted successfully!"
```

---

### **Explanation of the Script**
1. **Prompts for AWS credentials dynamically** instead of using hardcoded values.
2. **Removes any previous encryption setup** and regenerates everything from scratch.
3. **Generates a new Age encryption key** to ensure fresh security keys.
4. **Configures SOPS to automatically encrypt `aws_credentials.yaml`**.
5. **Applies correct file permissions** to prevent unauthorized access.
6. **Encrypts the AWS credentials** using Age encryption.
7. **Verifies decryption works correctly** before confirming success.

This approach ensures that AWS credentials are securely stored and **never exposed in plaintext**.

### **Step 2.3: Modify `.gitignore` to Prevent Leaking Sensitive Files**  

To ensure that sensitive encryption keys and unencrypted credentials are **never committed to Git**, update your `.gitignore` file with the following:  

#### **Append the Following to `.gitignore`**
```plaintext
# Ignore unencrypted AWS credentials
config/aws_credentials.yaml

# Ignore Age encryption keys
config/sops/age/
# Ignore environment variables and credentials
.env
config/credentials/*
config/aws_credentials.yaml
config/.sops.yaml

# Ignore SOPS-related encryption keys and directories
config/sops/
config/sops/**
config/sops/age/
config/sops/age/*
config/sops/age/keys.txt

# Ignore SOPS configuration (optional, if you don't want it in version control)
config/.sops.yaml
```

### **Why This Matters?**
- **Prevents committing unencrypted AWS credentials**, reducing the risk of accidental exposure.
- **Ensures encryption keys stay private**, preventing unauthorized decryption.
- **Keeps your repository clean**, ensuring only encrypted credentials are versioned.

This ensures that even if someone accesses your repo, they **cannot decrypt your AWS credentials** without your local Age key.
