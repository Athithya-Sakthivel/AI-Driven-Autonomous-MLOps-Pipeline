# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (if needed)
EXPOSE 8080

# Command to run the application (adjust if necessary)
CMD ["python", "src/pipeline/run_pipeline.py"]
