#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "antenv" ]; then
    python -m venv antenv
fi

# Activate the virtual environment
source antenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the app
exec gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
