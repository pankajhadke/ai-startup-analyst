# Stage 1: Build dependencies in a larger image with a compiler
FROM python:3.12 AS builder

WORKDIR /app

# Install build dependencies, including the missing pygobject library
RUN apt-get update && apt-get install -y build-essential libdbus-1-dev libgirepository1.0-dev pkg-config

# Copy your requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the final, smaller image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install poppler-utils for testing
RUN apt-get update && apt-get install -y poppler-utils

# Copy the installed Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy your application code
COPY web.py .
COPY app/ app/
COPY templates/ templates/
COPY data/ data/

# Expose the port that the app will run on
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "web.py"]
