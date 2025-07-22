#!/bin/bash

echo "🔧 Starting setup for AI-Powered Encrypted Keylogger..."

# Step 1: Update system
sudo apt update && sudo apt upgrade -y

# Step 2: Install Python 3.9 and venv if not already installed
sudo apt install python3.9 python3.9-venv python3.9-dev -y

# Step 3: Create virtual environment
python3.9 -m venv tfenv
source tfenv/bin/activate

# Step 4: Upgrade pip
pip install --upgrade pip

# Step 5: Install required Python packages
pip install tensorflow==2.13 keras pynput cryptography numpy

# Step 6: Make folders and download model (if hosted online)
mkdir -p models
echo "[!] Please place your trained model file as models/behavior_model.h5"

# Step 7: Provide user instruction
echo "✅ Setup complete!"
echo "👉 To activate the virtual environment: source tfenv/bin/activate"
echo "👉 To run the logger: python3 cli_keylogger.py --start"
