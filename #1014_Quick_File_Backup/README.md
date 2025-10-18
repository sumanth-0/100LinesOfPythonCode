# Quick File Backup

A fast and simple CLI tool for backing up files and folders with automatic timestamping.

## Description

Quick File Backup is a lightweight Python utility that allows you to quickly backup important files and directories to a designated location. Each backup is automatically timestamped, making it easy to track and manage multiple backup versions.

## Features

- ✅ Backup individual files or entire directories
- ✅ Automatic timestamp-based backup folders (YYYYMMDD_HHMMSS)
- ✅ Human-readable file size display
- ✅ Cross-platform compatibility (Windows, macOS, Linux)
- ✅ Error handling with clear user feedback
- ✅ Preserves file metadata (timestamps, permissions)
- ✅ Simple and intuitive command-line interface

## Installation

1. Clone this repository or download the script
2. Ensure you have Python 3.6 or higher installed
3. No additional dependencies required (uses only standard library)

## Usage

### Basic Syntax

```bash
python quick_file_backup.py <source> [destination]
```

### Examples

**Backup a single file** (creates backups folder in current directory):
```bash
python quick_file_backup.py myfile.txt
```

**Backup a single file to a specific location**:
```bash
python quick_file_backup.py myfile.txt /path/to/backups
```

**Backup an entire folder**:
```bash
python quick_file_backup.py myfolder
```

**Backup to a custom destination**:
```bash
python quick_file_backup.py important_folder /external/drive/backups
```

## How It Works

1. The script creates a timestamped backup directory (e.g., `backup_20231018_143022`)
2. Copies the source file or directory to this backup location
3. Preserves original file metadata
4. Reports the operation status and backup size

## Output Example

```
==================================================
Quick File Backup Tool
==================================================

Backup location: backups/backup_20231018_143022

✓ Backed up: myfile.txt (2.45 MB)

✓ Backup completed successfully!
Location: backups/backup_20231018_143022
```

## Requirements

- Python 3.6+
- Standard library modules:
  - `os`
  - `shutil`
  - `sys`
  - `datetime`
  - `pathlib`

## Contributing

This project is part of the 100 Lines of Python Code challenge. Contributions should follow the repository's contributing guidelines.

## Issue Reference

This project addresses issue [#1014](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1014) from the 100LinesOfPythonCode repository.

## License

This project follows the license of the parent repository.

## Tips

- Use absolute paths for critical backups
- Regular backups help prevent data loss
- Consider automating with cron jobs or scheduled tasks
- Test restore procedures periodically
