# Directory Size Monitor

## Description
A Python CLI tool to analyze and report directory sizes with threshold alerts. This tool helps you monitor disk usage and identify large directories that may need attention.

**Related to Issue:** [#1008](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1008)

## Features
- 📊 Calculate total directory size recursively
- 🚨 Alert when directory size exceeds a specified threshold
- 📝 Human-readable size formatting (B, KB, MB, GB, TB, PB)
- 📁 List subdirectory sizes with sorting by size
- 🔝 Display top N largest subdirectories
- 🛡️ Handles permission errors gracefully
- ⚡ Fast and efficient directory scanning

## Requirements
- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/#1008_Directory_Size_Monitor
```

2. Make the script executable (optional):
```bash
chmod +x directory_size_monitor.py
```

## Usage

### Basic Usage
Analyze a directory:
```bash
python directory_size_monitor.py /path/to/directory
```

### With Threshold Alert
Set a threshold and get alerts if exceeded:
```bash
python directory_size_monitor.py /path/to/directory -t 500MB
python directory_size_monitor.py /path/to/directory --threshold 1.5GB
```

### Show Subdirectories
List all subdirectories with their sizes:
```bash
python directory_size_monitor.py /path/to/directory -r
python directory_size_monitor.py /path/to/directory --recursive
```

### Show Top N Largest Subdirectories
Display only the top N largest subdirectories:
```bash
python directory_size_monitor.py /path/to/directory -n 10
python directory_size_monitor.py /path/to/directory --top 5
```

### Combined Options
```bash
python directory_size_monitor.py ~/Documents -t 2GB -n 10
```

## Command Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `directory` | - | Directory path to analyze (required) |
| `--threshold` | `-t` | Size threshold (e.g., 100MB, 1.5GB) |
| `--recursive` | `-r` | Show all subdirectory sizes |
| `--top` | `-n` | Show top N largest subdirectories |

## Threshold Format

The threshold can be specified with the following units:
- `B` - Bytes
- `KB` - Kilobytes (1024 bytes)
- `MB` - Megabytes (1024 KB)
- `GB` - Gigabytes (1024 MB)
- `TB` - Terabytes (1024 GB)

Examples: `500MB`, `1.5GB`, `100KB`, `2TB`

## Example Output

```
Analyzing: /home/user/Documents
----------------------------------------------------------------------
Total size: 3.45 GB (3,704,512,345 bytes)
Threshold: 2.00 GB
⚠️  WARNING: Directory size exceeds threshold!
   Exceeded by: 1.45 GB

Subdirectories:
  Photos                                      1.85 GB
  Videos                                      1.20 GB
  Projects                                  285.34 MB
  Downloads                                 105.67 MB
  Documents                                  15.23 MB
```

## Use Cases

- 🔍 **Disk Space Management**: Identify directories consuming excessive disk space
- 📦 **Backup Planning**: Determine which directories need backup priority
- 🧹 **Cleanup Operations**: Find candidates for cleanup or archival
- 📊 **System Monitoring**: Set up regular checks with threshold alerts
- 🚀 **Performance Optimization**: Identify directories that might slow down operations

## Code Quality

- ✅ Clean, readable code
- ✅ Proper error handling
- ✅ No external dependencies
- ✅ Under 100 lines of code
- ✅ PEP 8 compliant

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions, improvements, and bug reports are welcome!

## License

This project follows the license of the parent repository.

## Author

Contributed as part of Issue #1008

---

**Note**: This tool handles permission errors gracefully. If you encounter "Permission denied" errors for certain directories, the tool will skip them and continue with accessible directories.
