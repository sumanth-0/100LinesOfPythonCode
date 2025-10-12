# File Duplicate Remover

A Python script that scans a folder for duplicate files by comparing file hashes and provides options to list or remove them safely.

## Features

- 🔍 **Smart Detection**: Uses SHA-256 hashing to accurately identify duplicate files
- 📊 **Detailed Reports**: Shows duplicate file groups with sizes and locations
- 🗑️ **Safe Removal**: Keeps one copy while removing duplicates with user confirmation
- 🔄 **Recursive Scanning**: Scans all subdirectories within the target folder
- 💾 **Space Savings**: Calculates total space wasted by duplicates

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository or download the script
2. Ensure Python 3 is installed on your system

```bash
python --version  # Should be 3.8 or higher
```

## Usage

### List Duplicates (Dry Run)

To scan a folder and list duplicate files without removing them:

```bash
python file_duplicate_remover.py /path/to/folder
```

### Remove Duplicates

To remove duplicate files (keeps the first occurrence):

```bash
python file_duplicate_remover.py /path/to/folder --remove
```

**Note**: You will be prompted for confirmation before any files are deleted.

## Example Output

```
Scanning folder: /home/user/documents
Found 250 files. Calculating hashes...

Found 3 sets of duplicate files:

[1] Hash: a8f3c2d1e4b7f9... (3 copies, 1,024,000 bytes each)
    - /home/user/documents/photo1.jpg
    - /home/user/documents/backup/photo1.jpg
    - /home/user/documents/old/photo1.jpg

[2] Hash: b7e9f1a2c3d8... (2 copies, 512,000 bytes each)
    - /home/user/documents/report.pdf
    - /home/user/documents/copies/report.pdf

Total: 3 duplicate file(s) wasting 2,560,000 bytes
```

## How It Works

1. **Scanning**: The script recursively scans the specified folder and all its subdirectories
2. **Hashing**: Each file is read in chunks and a SHA-256 hash is calculated
3. **Grouping**: Files with identical hashes are grouped together as duplicates
4. **Reporting**: Duplicate groups are displayed with file paths and sizes
5. **Removal** (optional): With user confirmation, keeps the first file and removes others

## Safety Features

- ✅ Requires explicit `--remove` flag to delete files
- ✅ Prompts for user confirmation before deletion
- ✅ Always keeps at least one copy of each file
- ✅ Provides detailed information before any action
- ✅ Error handling for file access issues

## Command Line Options

```
Usage: python file_duplicate_remover.py <folder_path> [--remove]

  <folder_path>  : Path to scan for duplicates
  --remove       : Remove duplicates (keeps first occurrence)
```

## Contributing

This project is part of the 100 Lines of Python Code repository. Contributions and improvements are welcome!

## License

This script is provided as-is for educational and practical use.

## Issue Reference

Solution for issue #686 - File Duplicate Remover
