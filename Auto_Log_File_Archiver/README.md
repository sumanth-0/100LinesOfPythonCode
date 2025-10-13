# Auto Log File Archiver

A minimal Python script that automatically moves log files older than a week to an "archive" folder.

## Features

- **Automatic Detection**: Finds log files (`.log`, `.txt`, `.out`)
- **Age Check**: Identifies files older than 7 days
- **Archive Creation**: Creates archive folder automatically
- **Duplicate Handling**: Adds timestamps to prevent overwrites
- **Sample Generation**: Creates test logs for demonstration

## Usage

### Interactive Mode
```bash
python log_archiver.py
```

### With Custom Directories
```bash
# Will prompt for directories
python log_archiver.py
```

## File Types Archived

- `.log` files
- `.txt` files  
- `.out` files

## Example Output

```
Auto Log File Archiver
=========================
Enter log directory (or press Enter for sample): 
Created sample logs in: sample_logs

Enter archive directory (optional): 

Scanning: sample_logs
Archived: old.log

Archived 1 log file(s)
```

## How It Works

1. **Scan Directory**: Looks for log files in specified directory
2. **Check Age**: Uses file modification time to determine age
3. **Create Archive**: Makes "archive" subfolder if needed
4. **Move Files**: Moves files older than 7 days to archive
5. **Handle Duplicates**: Adds timestamp suffix if file exists

## Sample Test

The script can create sample logs for testing:
- `recent.log` - Current timestamp (not archived)
- `old.log` - 10 days old (gets archived)

## Requirements

- Python 3.6+
- No external dependencies

## Error Handling

- Permission errors are caught and reported
- Missing directories show appropriate messages
- File operation errors are handled gracefully

## Author

Created for issue #787 - 100 Lines of Python Code Project