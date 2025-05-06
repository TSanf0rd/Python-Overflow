#!/bin/bash

echo "Setting up your PythonOverflow environment..."

# Step 1: Ensure python3 and pip3 are available
if ! command -v python3 &> /dev/null; then
    echo "python3 is not installed. Please install Python 3 first."
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip for Python 3."
    exit 1
fi

# Step 2: Alias python to python3 if necessary
if ! command -v python &> /dev/null; then
    echo "Installing python-is-python3 to alias python → python3..."
    sudo apt update && sudo apt install -y python-is-python3
fi

# Step 3: Create a virtual environment
echo "🐍 Creating virtual environment in ./venv..."
python -m venv venv

# Step 4: Activate and install dependencies
source venv/bin/activate
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete. To run the app:"
echo "source venv/bin/activate"
echo "python app.py"
