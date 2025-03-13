import pulumi
import pulumi_aws as aws
import yaml
from pathlib import Path

# Load config.yaml
CONFIG_PATH = Path(__file__).resolve().parents[3] / "config" / "config.yaml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# Extract bucket details
bucket_name = config.get("aws", {}).get("bucket_name", "default-bucket")
region = config.get("aws", {}).get("region", "us-east-1")

# Create an S3 bucket (No ACL as it's deprecated)
s3_bucket = aws.s3.Bucket(bucket_name, 
    bucket=bucket_name,
    force_destroy=True,  # Destroys bucket with Pulumi `destroy`
    tags={"Environment": "MLOps"}
)

# Export bucket name
pulumi.export("s3_bucket_name", s3_bucket.id)
