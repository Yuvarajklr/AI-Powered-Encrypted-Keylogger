🔐 AI-Powered Encrypted Keylogger
This project is an AI-enhanced keylogger that monitors user keystroke behavior and classifies the input as a command, password, URL, or general text using an LSTM-based neural network. The logs are encrypted using Fernet symmetric encryption for secure storage.
📌 Features: Keystroke logging using pynput, Typing behavior analysis using LSTM deep learning model, Encrypted logging with cryptography.fernet, CLI tool for logging, analysis, and decryption, Simple and secure Python implementation.
🛠 Requirements: Python 3.9+, Linux-based OS (Kali Linux tested), Install dependencies with:

open therminal:

sudo apt update  
sudo apt install python3.9 python3.9-venv python3-pip  
python3.9 -m venv tfenv  
source tfenv/bin/activate  
pip install -r requirements.txt  

🧾 Create a requirements.txt file with:

pynput  
cryptography  
numpy  
tensorflow==2.13.0  

📁 Project Structure:
AI_Encrypted_Keylogger_Project/
├── cli_keylogger.py — Main script to run the logger
├── behavior_model.h5 — Pre-trained LSTM model
├── behavior_log.txt — Plain logs
├── behavior_encrypted_log.bin — Encrypted logs
├── behavior_key.key — Fernet encryption key
├── requirements.txt — Python dependencies
└── README.md — Project documentation

🚀 How to Run:

    Activate virtual environment:

source tfenv/bin/activate  

    Start logging:

python3.9 cli_keylogger.py --start  

    Analyze logs:

python3.9 cli_keylogger.py --analyze  

    Decrypt logs:

python3.9 cli_keylogger.py --decrypt  

📦 Key Files Explained:

    cli_keylogger.py: The main script with CLI options

    behavior_model.h5: LSTM model for typing behavior prediction

    behavior_log.txt: Human-readable log

    behavior_encrypted_log.bin: Encrypted log

    behavior_key.key: Generated key used by Fernet encryption

🧠 AI Typing Behavior Classification:
The AI model uses typing delay patterns to classify input into categories like "Password", "Command", "URL", or "General". Helps monitor behavior patterns intelligently.

🔐 Security Focus:
All logs are encrypted before storage using Fernet. Encryption key is saved as behavior_key.key. Do not share or lose this key.

👨‍💻 Example Usage:

source tfenv/bin/activate  
python cli_keylogger.py --start  

Then press ESC key to stop logging.

📎 Notes:

    Intended only for ethical and educational use

    Do not deploy without permission

    Logs are securely stored and classified by AI

📚 Learn More:

    TensorFlow: https://www.tensorflow.org/

    Cryptography: https://cryptography.io/en/latest/fernet/

    pynput: https://pynput.readthedocs.io/en/latest/

📄 License

MIT License. See LICENSE for more details.
