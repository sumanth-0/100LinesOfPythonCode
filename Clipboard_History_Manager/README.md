# Clipboard History Manager

## Description
A Python-based clipboard history manager that automatically monitors and stores clipboard content, allowing users to access their previous clipboard entries.

## Features
- Real-time clipboard monitoring
- Persistent storage of clipboard history
- View clipboard history with timestamps
- Copy entries back to clipboard
- Configurable history size
- JSON-based storage for easy access

## Requirements
```
pyperclip
```

## Installation
```bash
pip install pyperclip
```

## Usage
```python
python clipboard_history_manager.py
```

## How It Works
1. The program monitors your clipboard every second
2. When new content is detected, it's automatically saved to history
3. Each entry includes the text, timestamp, and character count
4. History is persisted in a JSON file for future access
5. You can view and restore previous clipboard entries

## Author
Contributed as part of the 100LinesOfPythonCode repository

## Related Issue
Fixes #755 - Clipboard History Manager
