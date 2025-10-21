# File Change Notifier

## Overview

The File Change Notifier is a robust Python script that monitors files and directories for changes in real-time. It detects file creation, modification, and deletion events, and sends notifications through multiple channels.

## Features

- **Multi-Path Monitoring**: Monitor multiple files and directories simultaneously
- **Recursive Scanning**: Optionally scan directories recursively to monitor all subdirectories
- **Accurate Change Detection**: Uses SHA-256 hash comparison to accurately detect file modifications
- **Flexible Notifications**: Console output and optional log file notifications
- **Configurable**: Adjustable check intervals and monitoring options
- **Command-Line Interface**: Easy-to-use CLI with argument parsing

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/file_change_notifier
```

2. Make the script executable (optional):
```bash
chmod +x file_change_notifier.py
```

## Usage

### Basic Usage

Monitor a single directory:
```bash
python file_change_notifier.py /path/to/directory
```

Monitor multiple paths:
```bash
python file_change_notifier.py /path/to/dir1 /path/to/dir2 /path/to/file.txt
```

### Advanced Options

Monitor with custom check interval (10 seconds):
```bash
python file_change_notifier.py -i 10 /path/to/directory
```

Monitor with log file output:
```bash
python file_change_notifier.py -l changes.log /path/to/directory
```

Monitor non-recursively:
```bash
python file_change_notifier.py --recursive false /path/to/directory
```

### Command-Line Arguments

- `paths`: One or more file/directory paths to monitor (required)
- `-r, --recursive`: Monitor directories recursively (default: True)
- `-i, --interval`: Check interval in seconds (default: 5)
- `-l, --log-file`: Path to log file for saving notifications

## Examples

### Example 1: Monitor a Project Directory

```bash
python file_change_notifier.py -i 3 -l project_changes.log ~/my_project
```

This monitors `~/my_project` with a 3-second check interval and logs changes to `project_changes.log`.

### Example 2: Monitor Multiple Directories

```bash
python file_change_notifier.py ~/Documents ~/Downloads
```

This monitors both Documents and Downloads directories with default settings.

## Output

The script provides real-time notifications for:

- **NEW FILE**: When a new file is created
- **MODIFIED**: When an existing file is modified
- **DELETED**: When a file is deleted

Example output:
```
2025-10-19 19:06:45 - INFO - Initializing file registry...
2025-10-19 19:06:45 - INFO - Monitoring directory: /home/user/test (15 files)
2025-10-19 19:06:45 - INFO - Starting file monitoring (check interval: 5s)
2025-10-19 19:06:50 - INFO - NEW FILE: /home/user/test/newfile.txt
2025-10-19 19:06:55 - INFO - MODIFIED: /home/user/test/document.txt
2025-10-19 19:07:00 - INFO - DELETED: /home/user/test/oldfile.txt
```

## How It Works

1. **Initialization**: The script scans all monitored paths and creates a registry of files with their metadata (size, modification time, SHA-256 hash)
2. **Monitoring Loop**: Every N seconds (configurable), the script re-scans the monitored paths
3. **Change Detection**: Compares the current state with the registry to detect:
   - New files (present in current scan but not in registry)
   - Deleted files (present in registry but not in current scan)
   - Modified files (hash comparison shows changes)
4. **Notification**: Sends notifications to console and/or log file

## Technical Details

- **Hash Algorithm**: SHA-256 for file content comparison
- **File Reading**: Uses 4KB block reading for memory efficiency
- **Error Handling**: Comprehensive exception handling for file system operations
- **Logging**: Standard Python logging module with customizable output

## Limitations

- Check interval may miss rapid changes between scans
- Large directories may take time to scan
- File hash calculation adds computational overhead

## Contributing

This project is part of the 100LinesOfPythonCode repository. Contributions are welcome!

## License

This project follows the license of the parent repository.

## Issue Reference

This implementation addresses issue [#657](https://github.com/sumanth-0/100LinesOfPythonCode/issues/657) - File Change Notifier.
