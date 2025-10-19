# Simple Backup Script

A comprehensive Python backup utility for creating compressed backups of directories and files with logging support.

## Description

This script provides a simple yet powerful solution for backing up directories and files. It creates compressed ZIP archives with timestamps, maintains detailed logs, and supports both backup and restore operations.

## Features

- 📦 **Directory Backup**: Backup entire directories with all subdirectories and files
- 📄 **File Backup**: Backup specific individual files
- 🗜️ **Compression**: Automatic ZIP compression to save storage space
- 📝 **Logging**: Detailed logging of all operations to files and console
- ⏰ **Timestamps**: Automatic timestamping of backup archives
- 🔄 **Restore**: Restore files from backup archives
- 📋 **List Backups**: View all available backup files
- ⚙️ **Configuration**: Optional JSON configuration file support
- 🖥️ **CLI**: Full command-line interface with argparse

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/simple_backup_script
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Backup a Directory

```bash
python simple_backup_script.py -s /path/to/source -d /path/to/backup/destination
```

### Backup Specific Files

```bash
python simple_backup_script.py -f file1.txt file2.txt -d /path/to/backup/destination
```

### List Available Backups

```bash
python simple_backup_script.py -l -d /path/to/backup/destination
```

### Restore a Backup

```bash
python simple_backup_script.py -r /path/to/backup/file.zip --restore-dir /path/to/restore
```

### Using Configuration File

Create a `config.json` file:
```json
{
  "log_dir": "backup_logs",
  "default_backup_dir": "backups"
}
```

Then run:
```bash
python simple_backup_script.py -c config.json -s /path/to/source
```

## Command Line Options

```
-s, --source          Source directory to backup
-d, --destination     Destination directory for backups (default: 'backups')
-f, --files          Specific files to backup (space-separated list)
-r, --restore        Backup file to restore
--restore-dir        Directory to restore backup to (default: 'restored')
-l, --list           List all available backups
-c, --config         Configuration file path (JSON format)
```

## Examples

### Example 1: Backup Documents Folder
```bash
python simple_backup_script.py -s ~/Documents -d ~/Backups
```

### Example 2: Backup Multiple Configuration Files
```bash
python simple_backup_script.py -f ~/.bashrc ~/.vimrc ~/.gitconfig -d ~/config_backups
```

### Example 3: Restore Latest Backup
```bash
python simple_backup_script.py -r ~/Backups/Documents_backup_20251019_120000.zip --restore-dir ~/Restored
```

## Output

- **Backup Archives**: Stored as `.zip` files with timestamps in the format: `<source_name>_backup_<YYYYMMDD_HHMMSS>.zip`
- **Log Files**: Stored in `backup_logs/` directory with timestamps: `backup_<YYYYMMDD_HHMMSS>.log`

## Technical Details

- **Language**: Python 3
- **Lines of Code**: 100+ lines
- **Dependencies**: Standard library only (os, shutil, zipfile, datetime, argparse, logging, json)
- **Compression**: ZIP format with DEFLATED compression method
- **Logging**: INFO level by default with file and console handlers

## Project Structure

```
simple_backup_script/
├── simple_backup_script.py    # Main backup script
├── README.md                   # This documentation file
├── backups/                    # Default backup directory (created automatically)
└── backup_logs/                # Log files directory (created automatically)
```

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

Contributions are welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Issue Reference

This script was created to address Issue #881 - Simple Backup Script

## License

This project is open source and available under the repository's license.

## Author

Created as part of Hacktoberfest 2025 contribution

## Acknowledgments

- Thanks to [@sumanth-0](https://github.com/sumanth-0) for maintaining the 100LinesOfPythonCode repository
- Created for Issue [#881](https://github.com/sumanth-0/100LinesOfPythonCode/issues/881)
