#!/bin/bash

echo "[+] Setting up virtual environment..."
python3.9 -m venv tfenv

source tfenv/bin/activate

echo "[+] Installing dependencies from requirements.txt..."

if [ ! -f "requirements.txt" ]; then
    echo "[!] Error: requirements.txt not found!"
    echo "    Make sure you're in the correct project folder."
    deactivate
    exit 1
fi

pip install -r requirements.txt

echo "[✓] Setup complete. You can now run: source tfenv/bin/activate && python3.9 cli_keylogger.py --start"

