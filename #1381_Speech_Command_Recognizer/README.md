# 🎤 Speech Command Recognizer

A Python-based voice command detector that recognizes basic commands like "start", "stop", "pause", "resume", and "exit" using speech recognition.

## Features

- 🎧 Real-time voice command recognition
- 🎯 Detects multiple commands: start, stop, pause, resume, exit, help
- 📊 Visual status indicators
- 🔊 Uses Google Speech Recognition API
- ⚡ Fast response time
- 🎚️ Automatic ambient noise calibration

## Supported Commands

- **START** - Start the system
- **STOP** - Stop the system
- **PAUSE** - Pause the system
- **RESUME** - Resume from pause
- **EXIT/QUIT** - Exit the program
- **HELP** - Show available commands

## Requirements

- Python 3.6+
- Microphone access
- Internet connection (for Google Speech Recognition API)

## Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

**Note for macOS users:** You may need to install PortAudio first:

```bash
brew install portaudio
pip install pyaudio
```

**Note for Linux users:**

```bash
sudo apt-get install python3-pyaudio
```

# 🎤 Speech Command Recognizer

A minimal Python project that recognizes basic voice commands like `start`, `stop`, `pause`, `resume`, `exit`, and `help` using your microphone and the Google Speech Recognition API. The code is under 100 lines!

---

## 🚀 What does it do?

- Listens for your voice through the microphone
- Recognizes and responds to these commands:
  - **start**: Start the system
  - **stop**: Stop the system
  - **pause**: Pause the system
  - **resume**: Resume from pause
  - **exit/quit**: Exit the program
  - **help**: Show available commands
- Shows the current status (Running, Paused, Stopped)
- Gives feedback in the terminal for each command

---

## 🛠️ How to Run

### 1. Install dependencies

**On macOS:**

```bash
brew install portaudio
```

**Create and activate a virtual environment (recommended):**

```bash
python3 -m venv ../.venv
source ../.venv/bin/activate
```

**Install Python packages:**

```bash
pip install SpeechRecognition PyAudio
```

### 2. Run the program

From the `#1318_Speech_Command_Recognizer` directory, simply run:

```bash
./run.sh
```

Or, if you want to run directly:

```bash
../.venv/bin/python Speech_Command_Recognizer.py
```

---

## 🗣️ How to Use

- Speak one of the supported commands into your microphone
- The program will print what you said and execute the command
- To stop the program, say `exit` or press `Ctrl+C`

---

## 📝 Example Session

```
🎤 Speech Command Recognizer
Speak: start, stop, pause, resume, exit, help
Press Ctrl+C to quit

Status: ⚪ Stopped
🎧 Listening... (speak a command)
💬 You said: "start"
🎯 Command: START
✅ START command received!
🚀 System started!

Status: 🟢 Running
🎧 Listening... (speak a command)
💬 You said: "pause"
🎯 Command: PAUSE
✅ PAUSE command received!
⏸️  System paused!

Status: 🟡 Paused
🎧 Listening... (speak a command)
💬 You said: "exit"
🎯 Command: EXIT
✅ EXIT command received!
👋 Goodbye!
```

---

## ❓ Troubleshooting

- **Microphone not detected:** Check permissions and hardware
- **PyAudio install error:** Make sure PortAudio is installed (`brew install portaudio`)
- **Recognition errors:** Speak clearly and check your internet connection

---
