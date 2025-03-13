import os
import subprocess
import yaml
import sys
from pathlib import Path

# Load config.yaml
CONFIG_PATH = Path(__file__).resolve().parents[3] / "config" / "config.yaml"

def load_config():
    """Loads configuration from YAML file."""
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()
S3_BUCKET = config.get("aws", {}).get("bucket_name", "")
DATA_PATHS = config.get("aws", {}).get("sync_paths", ["data/raw", "data/processed", "data/external", "data/synthetic"])

if not S3_BUCKET:
    print("Error: S3 bucket name missing in config.yaml.")
    sys.exit(1)

def ensure_directories_exist():
    """Creates missing directories from DATA_PATHS if they don't exist."""
    for path in DATA_PATHS:
        os.makedirs(path, exist_ok=True)

def load_aws_credentials():
    """Loads AWS credentials from sops-encrypted aws_credentials.yaml."""
    creds_path = Path(__file__).resolve().parents[3] / "config" / "aws_credentials.yaml"
    try:
        result = subprocess.run(["sops", "--decrypt", str(creds_path)], capture_output=True, text=True, check=True)
        aws_creds = yaml.safe_load(result.stdout).get("aws", {})

        if not aws_creds:
            print("Error: AWS credentials missing in decrypted file.")
            sys.exit(1)

        os.environ["AWS_ACCESS_KEY_ID"] = aws_creds.get("access_key_id", "")
        os.environ["AWS_SECRET_ACCESS_KEY"] = aws_creds.get("secret_access_key", "")

        # Ensure the region is valid
        aws_region = aws_creds.get("region") or "us-east-1"
        os.environ["AWS_DEFAULT_REGION"] = aws_region

    except subprocess.CalledProcessError as e:
        print("Error: Failed to decrypt AWS credentials. Ensure `sops` is installed and configured.")
        print("SOPS Error:", e)
        sys.exit(1)

def sync_s3(local_path, direction):
    """Syncs a local directory with S3."""
    if not os.path.exists(local_path):
        print(f"Skipping: Directory '{local_path}' does not exist.")
        return  # Skip instead of exiting

    load_aws_credentials()
    s3_uri = f"s3://{S3_BUCKET}/{os.path.basename(local_path)}/"

    if direction == "upload":
        command = ["aws", "s3", "sync", local_path, s3_uri, "--exact-timestamps"]
        print(f"Uploading: {local_path} → {s3_uri}")
    else:
        command = ["aws", "s3", "sync", s3_uri, local_path, "--exact-timestamps"]
        print(f"Downloading: {s3_uri} → {local_path}")

    subprocess.run(command, check=True)
    print(f"Sync complete for {local_path}")

if __name__ == "__main__":
    direction = "upload"  # Default direction

    # Override with CLI argument if provided
    if len(sys.argv) > 1:
        direction = sys.argv[1].lower()
        if direction not in ["upload", "download"]:
            print("Error: Direction must be 'upload' or 'download'.")
            sys.exit(1)

    # Ensure directories exist before syncing
    ensure_directories_exist()

    # Sync all predefined directories
    for path in DATA_PATHS:
        sync_s3(path, direction)
