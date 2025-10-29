# Clipboard Logger

A simple, cross-platform Python script that monitors the system clipboard and logs any new text content to a local file (`clipboard_history.log`).

## Description

This tool runs in the terminal and periodically checks the clipboard. When it detects new text, it appends that text, along with a timestamp, to `clipboard_history.log` in the same directory.

This is useful for:
* Keeping a history of copied items
* Preventing loss of important information from the clipboard
* Testing and debugging applications that interact with the clipboard

## Requirements

This script requires the `pyperclip` library.

## Installation

1. **Clone or download this repository**

2. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

## How to Use

1. **Run the script:**
```bash
   python clipboard_logger.py
```

2. **The script will start running.** You will see this output:
```
   Clipboard Logger Started.
   Monitoring clipboard every 1 second(s).
   History will be saved to: /path/to/clipboard_history.log
   Press Ctrl+C to stop.
```

3. **Copy any text.** The script will detect it and log it automatically.

4. **Press Ctrl+C** in the terminal to stop the logger.

## Files

- `clipboard_logger.py` - Main script file
- `clipboard_history.log` - Generated log file (created automatically when the script runs)

## Platform Support

Works on:
- Windows
- macOS
- Linux

## License

This project is open source and available for personal and educational use.

---

**Note:** The log file will be created in the same directory as the script. Make sure you have write permissions in that directory.