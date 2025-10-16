# Auto File Backup

## Description
Automatic file backup script that copies important files from a source directory to a backup folder with timestamps. This script helps protect your important data by creating regular backups with configurable settings.

## Features
- **Automated Backup**: Copies files from source to backup directory
- **Timestamp-based Naming**: Each backup is stored with a unique timestamp
- **Configurable File Types**: Specify which file extensions to backup
- **Folder Exclusion**: Exclude specific folders from backup (e.g., temp, cache)
- **Automatic Cleanup**: Removes old backups based on configurable retention policy
- **Logging**: Detailed logging of all backup operations
- **JSON Configuration**: Easy-to-edit configuration file

## Usage

### Basic Usage
```bash
python auto_file_backup.py <source_directory> <backup_directory>
```

### Example
```bash
python auto_file_backup.py /home/user/Documents /home/user/Backups
```

### With Custom Config
```bash
python auto_file_backup.py /home/user/Documents /home/user/Backups --config my_config.json
```

## Configuration

The script uses a `backup_config.json` file with the following structure:

```json
{
    "file_extensions": [".txt", ".pdf", ".doc", ".docx", ".xlsx"],
    "exclude_folders": ["temp", "cache"],
    "max_backups": 7
}
```

### Configuration Options
- **file_extensions**: List of file extensions to include in backup
- **exclude_folders**: Folders to skip during backup
- **max_backups**: Maximum number of backup folders to keep (older ones are deleted)

## Requirements
- Python 3.6 or higher
- Standard library only (no external dependencies)

## Scheduling Daily Backups

### On Linux/Mac (using cron):
```bash
# Edit crontab
crontab -e

# Add this line for daily backup at 2 AM
0 2 * * * /usr/bin/python3 /path/to/auto_file_backup.py /source /backup
```

### On Windows (using Task Scheduler):
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to Daily
4. Set action to run Python script with arguments

## Issue Reference
This script addresses issue #753 - Auto File Backup

## Author
Contributed to 100LinesOfPythonCode repository
