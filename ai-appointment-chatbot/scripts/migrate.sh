#!/bin/bash

# Navigate to the backend directory
cd ../backend

# Run database migrations using Alembic
alembic upgrade head

# Print a success message
echo "Database migrations completed successfully."