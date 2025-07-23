#!/bin/bash

echo "[+] Setting up virtual environment..."
python3.9 -m venv tfenv
source tfenv/bin/activate

echo "[+] Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[✓] Setup complete. You can now run: source tfenv/bin/activate && python3.9 cli_keylogger.py --start"

