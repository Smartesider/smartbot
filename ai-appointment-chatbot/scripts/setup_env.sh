#!/bin/bash

# This script sets up the environment variables for the AI Appointment Chatbot project.

# Load environment variables from the .env file
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found. Please create one based on .env.example."
    exit 1
fi

# Additional setup can be added here if needed.