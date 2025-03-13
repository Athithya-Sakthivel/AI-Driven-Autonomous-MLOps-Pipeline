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