# 🔐 AI-Powered Encrypted Keylogger (CLI Tool)

This is a Python-based CLI keylogger that uses an AI model (LSTM) to classify user keystrokes into categories like `Password`, `Command`, `URL`, and `General`. It also encrypts the logs using Fernet encryption and stores them securely.

## ✨ Features

- ✅ Keystroke logging with timestamp
- 🧠 AI behavior prediction using a pre-trained LSTM model (`behavior_model.h5`)
- 🔐 Secure encryption using `cryptography.fernet`
- 📄 Generates:
  - `behavior_log.txt` – Plain log
  - `behavior_encrypted_log.bin` – Encrypted log
  - `behavior_key.key` – Secret encryption key
- 📁 All logs saved in one place
- 🔧 Simple CLI interface with `--start`, `--analyze`, and `--decrypt`
- ⚙️ `setup.sh` installs dependencies and sets up environment

---

## 📂 File Structure

AI-Powered-Encrypted-Keylogger/
├── cli_keylogger.py # Main CLI tool
├── behavior_model.h5 # LSTM model for classification
├── setup.sh # Auto setup script
├── requirements.txt # Required Python packages
├── README.md # This file
├── LICENSE
├── .gitignore
├── logs/
│ ├── behavior_log.txt # Human-readable log
│ ├── behavior_encrypted_log.bin # Encrypted log
│ └── behavior_key.key # Fernet key file


---

## 🚀 Quick Start

### 🐧 On Kali Linux or any Linux system:

```bash
git clone https://github.com/Yuvarajklr/AI-Powered-Encrypted-Keylogger.git
cd AI-Powered-Encrypted-Keylogger
bash setup.sh

    This will create a virtual environment, install all required dependencies, and get the tool ready.

📌 Usage

    Always activate the virtual environment first:

source tfenv/bin/activate

▶ Start Keylogger

python3.9 cli_keylogger.py --start

    Press ESC to stop logging.

    Logs saved in logs/ folder.

📊 Analyze Logs

python3.9 cli_keylogger.py --analyze

🔓 Decrypt Logs

python3.9 cli_keylogger.py --decrypt

    Decrypted output will be printed in terminal using behavior_key.key.

📦 Dependencies

    pynput

    cryptography

    numpy

    tensorflow

    keras

These are automatically installed using setup.sh.

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

MIT License. See [LICENSE](https://github.com/Yuvarajklr/AI-Powered-Encrypted-Keylogger/blob/main/LICENSE) for more details.
