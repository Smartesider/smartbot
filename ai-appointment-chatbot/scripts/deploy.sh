#!/bin/bash

# This script is for deploying the AI Appointment Chatbot application.

# Exit immediately if a command exits with a non-zero status
set -e

# Define environment variables
export $(grep -v '^#' .env | xargs)

# Build the Docker containers
echo "Building Docker containers..."
docker-compose build

# Run database migrations
echo "Running database migrations..."
./scripts/migrate.sh

# Start the application
echo "Starting the application..."
docker-compose up -d

# Display the status of the containers
echo "Deployment complete. Checking the status of the containers..."
docker-compose ps

# End of script