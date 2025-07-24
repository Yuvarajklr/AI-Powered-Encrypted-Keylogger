#!/bin/bash

echo "[+] Setting up virtual environment..."
python3.9 -m venv tfenv
source tfenv/bin/activate

echo "[+] Installing dependencies from requirements.txt..."
pip install --upgrade pip
python3.9 -m pip install pynput
python3.9 -m pip install cryptography
pip install numpy==1.23.5
python3.9 -m pip install tensorflow-cpu==2.11


echo "[✓] Setup complete. You can now run: source tfenv/bin/activate && python3.9 clic_keylogger.py --start"


