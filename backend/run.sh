#!/bin/env bash
set -e  # Exit immediately if a command exits with a non-zero status

# Change to the directory where the script is located
cd "$(dirname "$0")"

# Check if the virtual environment exists
if [[ ! -d venv ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
else
    echo "Virtual environment already exists. Activating..."
    source venv/bin/activate
fi

# Start the Flask server
echo "Starting Flask server..."
flask run
