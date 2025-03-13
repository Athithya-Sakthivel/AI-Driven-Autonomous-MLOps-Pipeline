# **Autonomous Drift Detection and Model Optimization in an AI-Augmented MLOps Pipeline**  


As machine learning models operate in dynamic environments, they **degrade over time** due to changes in data distributions (data drift) and shifts in model performance (model drift). Traditional MLOps pipelines often rely on **static retraining schedules**, which fail to respond effectively to real-world variations.  

This project builds an **AI-driven autonomous MLOps pipeline** that:  
- **Continuously monitors and detects drift** using AI agents.  
- **Automates model retraining** based on detected drift patterns.  
- **Optimizes models dynamically** using AI-powered hyperparameter tuning.  
- **Simulates real-world drift scenarios** with synthetic data.  
- **Deploys seamlessly** in both local and cloud environments.  

This pipeline ensures that models **remain adaptive, robust, and optimized** without manual intervention.  

---

## ** Autonomous AI Agents in the Pipeline**  

The pipeline is powered by AI agents that **automate key processes**, ensuring a self-sustaining MLOps system.  

1. **Data Ingestion Agent**  
   - Periodically collects and preprocesses data from external sources.  
   - Detects ingestion anomalies and missing data patterns.  

2. **Drift Detection Agent**  
   - Monitors both **data drift** (changes in input distribution) and **model drift** (performance degradation).  
   - Triggers automated retraining when drift surpasses a defined threshold.  

3. **Model Optimization Agent**  
   - Automatically fine-tunes hyperparameters to ensure optimal model performance.  
   - Adapts the model dynamically to evolving data distributions.  

These agents **replace manual workflows** and ensure that the pipeline continuously improves model accuracy and efficiency.  

---

## **3. Key Features & Capabilities**  

| **Feature**                 | **Description**                                                                  |
|-----------------------------|----------------------------------------------------------------------------------|
| **Automated Data Ingestion** | Fetches and processes external data at scheduled intervals.                     |
| **Autonomous Drift Detection** | AI-powered monitoring of data and model drift.                                 |
| **Intelligent Model Retraining** | Triggers updates only when necessary, optimizing computational resources.    |
| **Dynamic Hyperparameter Tuning** | AI agents optimize models after retraining for continuous improvement.    |
| **Synthetic Data Generation** | Simulates drift scenarios to enhance model robustness.                         |
| **Scalable & Portable**      | Runs locally and can be deployed to the cloud for production use.               |
| **Monitoring & Alerting**    | Dashboards provide real-time insights into pipeline performance.                |

---

## **4. End-to-End Pipeline Workflow**  

1. **Data Collection & Ingestion**  
   - AI agent fetches external data at scheduled intervals.  
   - Data is preprocessed and stored for downstream tasks.  

2. **Drift Detection & Model Retraining**  
   - AI agent monitors drift in new data batches.  
   - If drift exceeds a defined threshold, automated model retraining is triggered.  

3. **Model Optimization & Deployment**  
   - Hyperparameters are optimized post-retraining.  
   - The updated model is seamlessly deployed for inference.  

4. **Continuous Monitoring & Alerts**  
   - Dashboards track drift, retraining events, and model performance.  
   - Alerts notify when intervention is needed.  

### **Scheduled Execution**  
- The ingestion pipeline can be automated using a **scheduler** like `cron` or an **orchestration tool**.  
- Example `cron` job (runs ingestion every 5 minutes):  
  ```bash
  */5 * * * * /path/to/venv/bin/python /path/to/project/src/data/ingest_data.py
  ```  

### **Cloud Deployment**  
- The pipeline is **cloud-ready** and can be deployed using containerization and infrastructure automation.  
- Supports **CI/CD workflows** for seamless updates.  

---

## **6. Project Deliverables**  
- **Fully automated MLOps pipeline** with AI-driven agents.  
- **Monitoring dashboards** for drift detection and model performance tracking.  
- **CI/CD integration** for continuous testing and deployment.  
- **Synthetic data experiments** to evaluate model robustness.  

---

This project **pushes the boundaries of AI-driven automation** by enabling models to self-adapt, ensuring long-term reliability without human intervention.








user@LAPTOP-J7J7UEO3:~/final/AI-Driven-Autonomous-MLOps-Pipeline$ tree
.
├── Dockerfile
├── Dockerfile.dev
├── README.md
├── artifacts
│   ├── mlflow
│   ├── models
│   └── optuna_study
├── config
│   ├── README.md
│   ├── aws_credentials.yaml
│   ├── config.yaml
│   ├── environments
│   │   ├── dev.env
│   │   ├── prod.env
│   │   └── test.env
│   ├── logging.yaml
│   ├── setup_sops.sh
│   └── sops
│       └── age
│           └── keys.txt
├── data
│   ├── processed
│   │   ├── processed_20250313_170111.csv
│   │   └── processed_20250313_170113.csv
│   ├── raw
│   │   ├── newsapi_20250313_140827.json
│   │   ├── newsapi_20250313_141430.json
│   │   ├── newsapi_20250313_153012.json
│   │   ├── newsapi_20250313_153150.json
│   │   ├── newsapi_20250313_160252.json
│   │   ├── newsapi_20250313_160305.json
│   │   ├── newsapi_20250313_160318.json
│   │   └── newsapi_20250313_160402.json
│   └── synthetic
├── docker-compose.override.yml
├── docker-compose.yml
├── docs
│   └── docker.md
├── logs
│   └── alerts
├── monitoring
│   ├── grafana
│   │   └── grafana_dashboard.json
│   ├── prometheus
│   │   └── prometheus_config.yml
│   └── streamlit
│       └── streamlit_dashboard.py
├── notebooks
│   ├── eda_fraud.ipynb
│   ├── eda_gdelt.ipynb
│   └── synthetic_data_analysis.ipynb
├── requirements-aws.txt
├── requirements-dev.txt
├── requirements-docker.txt
├── requirements-test.txt
├── requirements.txt
├── src
│   ├── agents
│   │   ├── ci_cd_agent.py
│   │   ├── data_ingestion_agent.py
│   │   ├── drift_detection_agent.py
│   │   ├── evaluation_agent.py
│   │   ├── optimization_agent.py
│   │   └── retraining_agent.py
│   ├── ci_cd
│   │   ├── build_pipeline.py
│   │   ├── deploy_pipeline.py
│   │   └── test_pipeline.py
│   ├── data
│   │   ├── generate_synthetic_data.py
│   │   ├── ingest_data.py
│   │   └── preprocess_feature_eng.py
│   ├── infrastructure
│   │   ├── aws
│   │   │   ├── ecs_deploy.sh
│   │   │   └── s3_data_sync.py
│   │   ├── k8s
│   │   │   └── k8s_deployment.yaml
│   │   └── pulumi
│   │       ├── Pulumi.dev.yaml
│   │       ├── Pulumi.yaml
│   │       ├── __main__.py
│   │       └── requirements.txt
│   ├── models
│   │   ├── evaluate_model.py
│   │   ├── optimize_model.py
│   │   ├── retrain_model.py
│   │   ├── serve_model.py
│   │   └── train_model.py
│   ├── monitoring
│   │   ├── alerts.py
│   │   ├── drift_detection.py
│   │   ├── log_performance.py
│   │   └── model_health_monitor.py
│   └── pipeline
│       ├── orchestrate_pipeline.py
│       ├── pipeline_utils.py
│       └── run_pipeline.py
└── tests
    ├── e2e
    │   └── test_end_to_end.py
    ├── integration
    │   ├── test_model_serving.py
    │   └── test_pipeline.py
    └── unit
        ├── test_data_ingestion.py
        ├── test_drift_detection.py
        ├── test_model_training.py
        └── test_preprocessing.py

36 directories, 74 files
user@LAPTOP-J7J7UEO3:~/final/AI-Driven-Autonomous-MLOps-Pipeline$ 




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

news_api:
  base_url: "https://newsapi.org/v2/everything"
  api_key: "b00b276a080b4015ba9aeed375450017"
  query: "Machine Learning"
  language: "en"
  max_results: 100

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


## **1.1.3 `aws_credentials.yaml` — Encrypted AWS Credentials (Updated for IAM User without MFA)**

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
sops --decrypt "$AWS_CREDENTIALS" >/dev/null && echo " AWS Credentials encrypted successfully!"
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




# **1.2 Docker and Virtualization – Comprehensive Guide**  

This section focuses on **containerizing the AI-Driven MLOps pipeline** using **Docker and Docker Compose** to ensure **portability, reproducibility, and scalability**.  

---

## **1.2.1 `Dockerfile` (Production Build)**  

The `Dockerfile` defines a **lightweight, self-contained production environment** for running the pipeline.  

### **Contents of `Dockerfile`**  
```dockerfile
# Use official minimal Python 3.10 image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependencies file first to optimize caching
COPY requirements.txt .

# Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose a port (if running a web service inside the container)
EXPOSE 8080

# Run the pipeline script when the container starts
CMD ["python", "src/pipeline/run_pipeline.py"]
```

### **Explanation**  
- The `FROM` instruction selects a minimal Python image to reduce container size.  
- The `WORKDIR /app` command ensures that all subsequent operations run inside `/app`.  
- The `COPY requirements.txt .` copies the dependency file separately to leverage Docker’s layer caching.  
- The `RUN pip install --no-cache-dir -r requirements.txt` installs dependencies within the container.  
- The `COPY . .` copies all project files into the container.  
- The `EXPOSE 8080` specifies the port if a web-based service (e.g., Flask, FastAPI) is running.  
- The `CMD ["python", "src/pipeline/run_pipeline.py"]` ensures the pipeline runs when the container starts.  

---

## **1.2.2 `Dockerfile.dev` (Development Environment)**  

This file defines a **development-friendly environment** with additional tools for debugging.  

### **Contents of `Dockerfile.dev`**  
```dockerfile
# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies useful for debugging
RUN apt-get update && apt-get install -y \
    curl git vim && rm -rf /var/lib/apt/lists/*

# Copy development dependencies
COPY requirements-dev.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the entire project
COPY . .

# Expose port for local services
EXPOSE 8080

# Keep the container running for interactive debugging
CMD ["/bin/bash"]
```

### **Explanation**  
- Installs debugging tools (`curl`, `git`, `vim`).  
- Uses `requirements-dev.txt` to install additional dependencies.  
- Keeps the container running with an interactive Bash shell for debugging.  

---

## **1.2.3 `docker-compose.yml` (Production Multi-Container Setup)**  

Docker Compose is used to manage **multi-container deployments**. This file defines a **production environment** where multiple services can run together.  

### **Contents of `docker-compose.yml`**  
```yaml
version: "3.9"

services:
  mlops-pipeline:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: mlops_pipeline
    restart: unless-stopped
    volumes:
      - .:/app
    ports:
      - "8080:8080"
    environment:
      - ENVIRONMENT=production
```

### **Explanation**  
- The `services` section defines the main containerized application (`mlops-pipeline`).  
- The `build` section specifies the context (`.`) and `Dockerfile`.  
- The `container_name` assigns a name to the running container.  
- The `restart: unless-stopped` ensures the container restarts automatically if it stops unexpectedly.  
- The `volumes` mapping mounts the project directory inside the container, allowing live code changes.  
- The `ports` mapping exposes port `8080`.  
- The `environment` variable sets the container’s execution mode to **production**.  

---

## **1.2.4 `docker-compose.override.yml` (Development Mode)**  

This file **modifies the default `docker-compose.yml`** to create a **development-friendly environment**.  

### **Contents of `docker-compose.override.yml`**  
```yaml
version: "3.9"

services:
  mlops-pipeline:
    build:
      context: .
      dockerfile: Dockerfile.dev
    environment:
      - ENVIRONMENT=development
    ports:
      - "8080:8080"
    volumes:
      - .:/app
    command: ["/bin/bash"]
```

### **Explanation**  
- Uses `Dockerfile.dev` instead of `Dockerfile`.  
- Keeps the container running interactively.  
- Maps local files to the container for real-time development.  

---

## **Running the Containers**  

### **Building Docker Images**  
```bash
docker-compose build
```

### **Starting Development Mode**  
```bash
docker-compose up -d
```
To attach to the container’s terminal:  
```bash
docker exec -it mlops_pipeline /bin/bash
```

### **Starting Production Mode**  
```bash
docker-compose -f docker-compose.yml up -d
```

### **Stopping and Removing Containers**  
```bash
docker-compose down
```
To remove all containers and images:  
```bash
docker system prune -a
```

---

## **Adding `.gitignore` for Docker**  

Modify the `.gitignore` file to **prevent tracking unwanted files**.  

```gitignore
# Ignore Python caches
__pycache__/
*.pyc
*.pyo

# Ignore Virtual Environments
.venv/
env/

# Ignore Docker-specific files
docker-compose.override.yml
*.log
*.db
```

---

## **Verifying Setup**  

After starting your container, verify if the pipeline is running correctly:  
```bash
docker ps  # Check running containers
docker logs mlops_pipeline  # View logs
```

---

## **Automating Setup with a Script**  

The following script automates Docker setup and execution.  

Save as `setup_docker.sh`:  
```bash
#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install it manually."
    exit 1
fi

# Build the project
echo "Building Docker images..."
docker-compose build

# Start development mode
echo "Starting Docker containers..."
docker-compose up -d

echo "Docker setup complete!"
```

Run it using:  
```bash
bash setup_docker.sh
```

---

## **Summary**  

1. **`Dockerfile`** - Defines a lightweight production container for the MLOps pipeline.  
2. **`Dockerfile.dev`** - Creates an interactive development container.  
3. **`docker-compose.yml`** - Defines multi-container production deployment.  
4. **`docker-compose.override.yml`** - Overrides production settings for local development.  
5. **Container management commands** - Explained how to build, run, and stop containers.  
6. **`.gitignore`** - Configured to prevent tracking unnecessary Docker files.  
7. **Automation** - Provided `setup_docker.sh` to streamline execution.  

This ensures the **MLOps pipeline is fully containerized, scalable, and easy to manage**.

---



# 2.1.1 Data ingestion and syncing #

- Loads **API key from `config.yaml`** securely.  
- **Fetches** news articles from NewsAPI.  
- **Handles errors** and retries if needed.  
- **Saves data** to `data/raw/` with a timestamp.  
- **Includes a unit test** for validation.  
- Uses **only open-source libraries** and avoids unnecessary dependencies.  

---

## **Step 1: Get API Key and Store It Securely**
1. Go to **[NewsAPI.org](https://newsapi.org/register)** and create a free account.  
2. Copy your API key.  
3. Store it in `config/config.yaml` (do not hardcode it in Python files).  

```yaml
news_api:
  base_url: "https://newsapi.org/v2/everything"
  api_key: "b00b276a080b4015ba9aeed375450017"
  query: "Machine Learning"
  language: "en"
  max_results: 100

```

---

## **Step 2: Implement `ingest_data.py`**
Create `src/data/ingest_data.py` and add the following code:  

```python
import os
import yaml
import requests
import json
import time
from datetime import datetime
from pathlib import Path

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()
NEWSAPI_CONFIG = config.get("news_api", {})
DATA_PATHS = config.get("paths", {})

def fetch_newsapi_data():
    if not NEWSAPI_CONFIG.get("api_key"):
        print("Error: Missing NewsAPI key in config.yaml.")
        return None

    url = f"{NEWSAPI_CONFIG['base_url']}?q={NEWSAPI_CONFIG['query']}&pageSize={NEWSAPI_CONFIG['max_results']}&language={NEWSAPI_CONFIG['language']}&apiKey={NEWSAPI_CONFIG['api_key']}"
    retries = config.get("agents", {}).get("data_ingestion_agent", {}).get("retries", 3)
    backoff_factor = 5

    for _ in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json().get("articles", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching NewsAPI data: {e}. Retrying in {backoff_factor} seconds...")
            time.sleep(backoff_factor)
    return None

def save_data(data, source):
    if not data:
        print(f"No data fetched from {source}. Skipping save.")
        return

    # Ensure paths are relative to the project root
    save_dir = PROJECT_ROOT / Path(DATA_PATHS.get("raw_data", "data/raw"))
    save_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = save_dir / f"{source}_{timestamp}.json"

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {len(data)} articles from {source} to {save_path}")

def main():
    data = fetch_newsapi_data()
    save_data(data, "newsapi")

if __name__ == "__main__":
    main()


```

---

## **Step 3: Running and Testing the Script**
### **Activate Virtual Environment**
```bash
source .venv/bin/activate  # Linux/Mac
```

### **Install Dependencies**
```bash
pip install requests pyyaml
```

### **Run the Script**
```bash
python src/data/ingest_data.py
```

### **Expected Output**
```
Saved 50 articles from newsapi to data/raw/newsapi_20250313_203015.json
```

### **Check Saved Data**
```bash
ls data/raw/
cat data/raw/newsapi_20250313_203015.json | jq
```

---

## **Final Summary**
- **Step 1:** Get API key and store it securely.  
- **Step 2:** Implement `ingest_data.py` to fetch and save NewsAPI data.  
- **Step 3:** Run the script and validate results.  

This ensures **secure, automated, and robust news ingestion** using **NewsAPI**.




# 2.1.2: Syncing Data with S3 (`s3_data_sync.py`)**  

After fetching and processing data, syncing it with **AWS S3** ensures **data availability, scalability, and version control** for downstream tasks like training, monitoring, and retraining. This step will:  
- **Upload new data** to S3 when ingestion occurs.  
- **Download data** from S3 when required.  
- **Ensure efficient synchronization** to avoid unnecessary uploads.  

---

### **1. Setup AWS Credentials for S3 Access**  
Ensure AWS credentials are **encrypted** using `sops` (Step 2.2). To configure AWS CLI with the credentials stored in `aws_credentials.yaml`:  

#### **Load Credentials in Environment Variables**
```bash
export AWS_ACCESS_KEY_ID=$(sops --decrypt config/aws_credentials.yaml | yq '.aws.access_key_id')
export AWS_SECRET_ACCESS_KEY=$(sops --decrypt config/aws_credentials.yaml | yq '.aws.secret_access_key')
export AWS_DEFAULT_REGION=$(sops --decrypt config/aws_credentials.yaml | yq '.aws.region')
```

---

### **2. Implementing `s3_data_sync.py`**  
This script will:  
- **Load bucket name and paths dynamically from `config.yaml`.**  
- **Automatically sync data directories with S3.**  
- **Skip already-uploaded files** to save bandwidth.  

#### **`src/data/s3_data_sync.py`**
```python
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

```

---

### **3. Usage Examples**  
Run the script dynamically with user input:  

#### **Upload Data to S3**
```bash
python src/data/s3_data_sync.py --path data/raw --direction upload
```

#### **Download Data from S3**
```bash
python src/data/s3_data_sync.py --path data/raw --direction download
```

---

### **5. Updating `.gitignore` to Prevent Sensitive File Uploads**
Modify `.gitignore` to ensure that sensitive or unnecessary files do not get committed:

#### **`.gitignore` Additions**
```
# AWS Credentials
config/aws_credentials.yaml

# Local data and logs
data/*
logs/*
!data/external/
!data/raw/
```

---

## **Key Features of this Implementation**  
- **Security-first approach**: AWS credentials are encrypted with `sops`.  
- **Automated handling**: No hardcoded values; dynamically fetches bucket name from `config.yaml`.  
- **Sync efficiency**: Uses `aws s3 sync` to avoid unnecessary reuploads.  
- **User-friendly**: Provides both **Python and Bash** implementations for ease of use.  

This completes **Step 2.1.2 (S3 Data Sync)**.





# **2.2 Data Preprocessing and feature engineering **  

# **2.2 Data Preprocessing Guide**  
This guide covers the entire **data preprocessing pipeline**, including **data cleaning, feature engineering, and schema validation** using the `preprocess_and_validate.py` script.

---

## **Overview of the Preprocessing Pipeline**
1. **Loading raw data** from JSON files stored in `data/raw/`.
2. **Cleaning the data**:
   - Removing duplicates.
   - Handling missing values.
   - Dropping unnecessary columns.
3. **Feature engineering**:
   - Extracting date-related attributes.
   - Creating text-based features.
4. **Saving the processed data** in `data/processed/`.
5. **Validating schema and data types** to ensure consistency.

---

## **2.2.1 Preprocessing and Validation Code**
### **File: `src/data/preprocess_feature_eng.py`**
```python
import os
import json
import yaml
import pandas as pd
import re
from pathlib import Path
from datetime import datetime

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

# Load configuration
def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()
DATA_PATHS = config.get("paths", {})

RAW_DATA_DIR = PROJECT_ROOT / Path(DATA_PATHS.get("raw_data", "data/raw"))
PROCESSED_DATA_DIR = PROJECT_ROOT / Path(DATA_PATHS.get("processed_data", "data/processed"))
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)  # Ensure processed directory exists

# Expected schema for validation
EXPECTED_SCHEMA = {
    "title": str,
    "description": str,
    "url": str,
    "publishedAt": "datetime64[ns]",
    "published_year": "int64",
    "published_month": "int64",
    "published_day": "int64",
    "published_weekday": "int64",
    "title_word_count": "int64",
    "description_word_count": "int64"
}

# Load raw JSON data
def load_raw_data():
    """Loads the most recent raw JSON data from data/raw/"""
    json_files = sorted(RAW_DATA_DIR.glob("newsapi_*.json"), reverse=True)

    if not json_files:
        print("No raw data files found.")
        return None

    latest_file = json_files[0]
    with open(latest_file, "r") as f:
        data = json.load(f)

    return pd.DataFrame(data)

# Clean raw data
def clean_data(df):
    """Cleans raw data by handling missing values, duplicates, and unnecessary columns."""
    if df.empty:
        print("Empty dataset after loading. Skipping cleaning.")
        return df

    # Drop duplicates
    df.drop_duplicates(subset=["title", "url"], inplace=True)

    # Drop unnecessary columns
    drop_columns = ["source", "content"]  # Content is often incomplete in NewsAPI
    df.drop(columns=[col for col in drop_columns if col in df.columns], inplace=True)

    # Handle missing values
    df.dropna(subset=["title", "description", "url"], inplace=True)

    return df

# Feature engineering
def feature_engineering(df):
    """Extracts useful features from the data."""
    if df.empty:
        print("Empty dataset after cleaning. Skipping feature engineering.")
        return df

    # Convert `publishedAt` to datetime
    df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")

    # Extract date-related features
    df["published_year"] = df["publishedAt"].dt.year
    df["published_month"] = df["publishedAt"].dt.month
    df["published_day"] = df["publishedAt"].dt.day
    df["published_weekday"] = df["publishedAt"].dt.weekday

    # Text-based features
    df["title_word_count"] = df["title"].apply(lambda x: len(str(x).split()))
    df["description_word_count"] = df["description"].apply(lambda x: len(str(x).split()))

    return df

# Save processed data
def save_processed_data(df):
    """Saves the cleaned and transformed data to the processed directory."""
    if df.empty:
        print("Processed data is empty. Skipping save.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = PROCESSED_DATA_DIR / f"processed_{timestamp}.csv"

    df.to_csv(save_path, index=False)
    print(f"Processed data saved to {save_path}")
    return save_path  # Return path for validation step

# Validate schema
def validate_data(csv_path):
    """Validates the processed data against the expected schema."""
    if not csv_path or not Path(csv_path).exists():
        print(f"Error: Processed data file not found at {csv_path}")
        return False

    df = pd.read_csv(csv_path)

    # Check required columns
    missing_columns = [col for col in EXPECTED_SCHEMA.keys() if col not in df.columns]
    if missing_columns:
        print(f"Error: Missing columns {missing_columns}")
        return False

    # Convert columns explicitly to correct types
    df["title"] = df["title"].fillna("").astype(str)
    df["description"] = df["description"].fillna("").astype(str)
    df["url"] = df["url"].fillna("").astype(str)

    # Validate data types
    for col, expected_dtype in EXPECTED_SCHEMA.items():
        if col in df.columns:
            actual_dtype = str(df[col].dtype)
            if actual_dtype != expected_dtype:
                print(f"Error: Column {col} has incorrect data type: expected {expected_dtype}, found {actual_dtype}")
                return False

    # Validate URLs
    url_pattern = re.compile(r"https?://[^\s]+")
    invalid_urls = df[~df["url"].astype(str).str.match(url_pattern, na=False)]
    if not invalid_urls.empty():
        print(f"Error: Invalid URLs found:\n{invalid_urls[['url']].head()}")
        return False

    print("Data validation passed successfully.")
    return True

# Main execution
def main():
    df = load_raw_data()
    if df is not None:
        df = clean_data(df)
        df = feature_engineering(df)
        processed_file = save_processed_data(df)

        if processed_file:
            validate_data(processed_file)

if __name__ == "__main__":
    main()
```

---

## **Step-by-Step Guide**

### **1. Load Raw Data**
- The script retrieves the most recent raw JSON file from `data/raw/`.
- JSON data is loaded into a Pandas DataFrame.
- If no data is found, it prints an error message.

### **2. Data Cleaning**
- **Duplicate Removal:** Removes duplicate entries based on `title` and `url`.
- **Column Dropping:** Removes unnecessary columns (`source`, `content`).
- **Handling Missing Values:** Drops rows where `title`, `description`, or `url` are missing.

### **3. Feature Engineering**
- Converts `publishedAt` to a proper datetime format.
- Extracts date-related attributes:
  - `published_year`
  - `published_month`
  - `published_day`
  - `published_weekday`
- Extracts text-based attributes:
  - `title_word_count`
  - `description_word_count`

### **4. Save Processed Data**
- The processed data is saved as a CSV file in `data/processed/`.
- The filename includes a timestamp (`processed_YYYYMMDD_HHMMSS.csv`).

### **5. Schema Validation**
- Ensures the processed CSV file exists.
- Checks if required columns are present.
- Converts `title`, `description`, and `url` to string format.
- Validates expected column data types.
- Checks if `url` values follow a proper format.

### **6. Execution**
Run the script with:
```bash
python3 src/data/preprocess_feature_eng.py
```
If validation fails, it prints the errors found.

---

## **Final Notes**
- This script automates both **data preprocessing** and **validation** in a single execution.
- It ensures that the dataset is **clean, structured, and validated** before further processing.
