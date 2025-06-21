# 🛡️ CYBER REQ - DoS Simulator Tool (v2.0)

> 🚀 A GUI tool to simulate HTTP flood-style requests using Python — built for educational and ethical use only.

---

## 🧠 Description

CYBER REQ is a graphical user interface (GUI) tool developed for **ethical hacking education**, **penetration testing practice**, and **cybersecurity demonstrations**. It allows users to send **N number of HTTP requests** to a target URL using various methods (GET, POST, etc.) with optional delay and real-time logging.

---

## 🆕 What’s New in Version 2.0

- ❌ Removed Proxy Support  
  ➤ *Note: Use [TOR](https://www.torproject.org/download/) or any VPN instead.*
- ⚡ Improved multi-threading for faster, more stable request sending
- 🖥️ Optimized UI (Removed splash screen lag)
- 📜 Real-time request logs and attack summary
- 🎯 Added randomized user-agents and custom headers

---

## 🛠️ Features

- 📡 HTTP Methods: `GET`, `POST`, `HEAD`, `OPTIONS`
- 🧩 Custom request count & optional delay per request
- 🖥️ GUI Interface with real-time log console
- 📊 Final summary: success, fail, SSL errors
- 🛑 Cancel attack button (safe interruption)
- 🔐 Randomized headers & user-agent for realism
- 🧑‍💻 Built for students, cybersecurity learners & demo labs

---

## 📦 Installation (All Platforms)

### 🪟 Windows

```powershell
pip install -r requirements.txt
python gui_tool.py
To build a standalone .exe file:

powershell
Copy code
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=cyber-req.ico gui_tool.py
🔍 Run the compiled .exe from the dist/ folder.

🐧 Linux (Debian/Ubuntu/Kali)
bash
Copy code
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
python3 gui_tool.py
To build a binary (optional):

bash
Copy code
pip3 install pyinstaller
pyinstaller --onefile --noconsole gui_tool.py
🍎 macOS
bash
Copy code
brew install python3  # If Python is not installed
pip3 install -r requirements.txt
python3 gui_tool.py
Optional app bundle build:

bash
Copy code
pip3 install pyinstaller
pyinstaller --onefile --noconsole gui_tool.py
💡 macOS users may need to allow the app manually under System Settings → Privacy & Security.

🧰 Usage
To launch the tool:

bash
Copy code
python gui_tool.py
✅ Works on both CLI and GUI environments. Internet required for testing.

To compile into a standalone executable (for Windows):

bash
Copy code
pyinstaller --onefile --noconsole --icon=cyber-req.ico gui_tool.py
📁 Project Structure
Copy code
cyber-req/
│
├── gui_tool.py
├── gui_tool.spec
├── cyber-req.ico
├── license.txt
├── logo.png
├── requirements.txt
├── README.md
└── dist/
📢 Disclaimer
CYBER REQ is developed solely for educational and demonstration purposes.
Any misuse of this tool (unauthorized DoS attacks, disruption of live systems, etc.) is strictly prohibited and against the developer’s intent. Always seek legal permission before testing any real-world target.

© 2025 Yarra Rajkumar
🔗 GitHub: RajJJDVPD
🔗 LinkedIn: yarra-raj-kumar