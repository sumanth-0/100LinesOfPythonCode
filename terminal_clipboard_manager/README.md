# Terminal Clipboard Manager

A command-line tool for managing clipboard history with copy, paste, list, and clear operations.

## Features

- **Copy**: Copy text to clipboard and automatically save to history
- **Paste**: Paste content from clipboard
- **List**: View your clipboard history with timestamps and character counts
- **Recall**: Copy any previous clipboard entry back to clipboard
- **Clear**: Clear all clipboard history
- **Persistent Storage**: Clipboard history is saved to disk and persists across sessions

## Requirements

```bash
pip install pyperclip
```

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install pyperclip
   ```
3. Make the script executable (optional):
   ```bash
   chmod +x terminal_clipboard_manager.py
   ```

## Usage

### Copy text to clipboard
```bash
python terminal_clipboard_manager.py copy "Hello World"
```

### Paste from clipboard
```bash
python terminal_clipboard_manager.py paste
```

### List clipboard history
```bash
# Show last 10 entries (default)
python terminal_clipboard_manager.py list

# Show last 20 entries
python terminal_clipboard_manager.py list -n 20
```

### Recall entry from history
```bash
# Copy the 3rd entry from history back to clipboard
python terminal_clipboard_manager.py recall 3
```

### Clear clipboard history
```bash
python terminal_clipboard_manager.py clear
```

## How It Works

- Clipboard history is stored in `~/.clipboard_history.json`
- Each entry includes:
  - Text content
  - Timestamp
  - Character count
- Maximum of 100 entries are kept (oldest are automatically removed)
- Uses `pyperclip` library for cross-platform clipboard access

## Examples

```bash
# Copy multiple pieces of text
python terminal_clipboard_manager.py copy "First item"
python terminal_clipboard_manager.py copy "Second item"
python terminal_clipboard_manager.py copy "Third item"

# View history
python terminal_clipboard_manager.py list

# Copy the second item back to clipboard
python terminal_clipboard_manager.py recall 2

# Paste it
python terminal_clipboard_manager.py paste
```

## Help

```bash
python terminal_clipboard_manager.py --help
```

## Features Explained

### Copy
Copies text to the system clipboard and adds it to the history file. Each entry is timestamped and includes the text length.

### Paste
Retrieves and displays the current clipboard content.

### List
Displays the clipboard history with:
- Entry number (for recall)
- Timestamp
- Character count
- Truncated text preview (first 60 characters)

### Recall
Copies a specific entry from history back to the clipboard using its index number (1-based).

### Clear
Removes all entries from the clipboard history file.

## Notes

- History is stored in JSON format in your home directory
- The tool maintains up to 100 clipboard entries
- Works on Windows, macOS, and Linux (via pyperclip)
- Text content is displayed with escaped newlines for better readability in list view

## License

This project is part of the 100LinesOfPythonCode repository.

## Contributing

References issue #1011 - Terminal Clipboard Manager
