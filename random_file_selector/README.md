# Random File Selector

A command-line tool to randomly select one or more files from a specified directory. Perfect for tasks like selecting random samples, testing with random files, or creating playlists.

## Features

- 🎲 Select one or multiple random files from a directory
- 📁 Recursive directory search (optional)
- 🔍 Filter by file extensions
- 📊 Multiple output formats (simple, detailed, JSON)
- 🙈 Option to include/exclude hidden files
- 🎯 Reproducible results with seed option
- ⚡ Fast and lightweight (100+ lines of Python)

## Installation

1. Clone or download this repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/random_file_selector
```

2. Make sure you have Python 3.6+ installed:
```bash
python --version
```

3. No additional dependencies required! Uses only Python standard library.

## Usage

### Basic Usage

Select one random file from a directory:
```bash
python random_file_selector.py /path/to/directory
```

### Advanced Options

```bash
# Select 5 random files
python random_file_selector.py /path/to/directory -n 5

# Search recursively through subdirectories
python random_file_selector.py /path/to/directory -r

# Filter by file extensions (e.g., only images)
python random_file_selector.py /path/to/directory -e jpg png jpeg gif

# Use detailed output format
python random_file_selector.py /path/to/directory -f detailed

# Use JSON output format (great for scripting)
python random_file_selector.py /path/to/directory -f json

# Include hidden files
python random_file_selector.py /path/to/directory --include-hidden

# Use a seed for reproducible results
python random_file_selector.py /path/to/directory -s 42

# Allow selecting the same file multiple times
python random_file_selector.py /path/to/directory -n 10 --allow-duplicates
```

### Combined Examples

```bash
# Select 3 random Python files recursively with detailed output
python random_file_selector.py ~/projects -r -e py -n 3 -f detailed

# Get JSON output of random media files
python random_file_selector.py ~/media -e mp4 mp3 avi -n 5 -f json

# Select random images from a specific folder
python random_file_selector.py ~/Pictures -e jpg png -n 10
```

## Command-Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `directory` | - | Directory to search for files (required) |
| `--number` | `-n` | Number of files to select (default: 1) |
| `--recursive` | `-r` | Search subdirectories recursively |
| `--extensions` | `-e` | Filter by file extensions (space-separated) |
| `--format` | `-f` | Output format: `simple`, `detailed`, or `json` |
| `--include-hidden` | - | Include hidden files (starting with .) |
| `--allow-duplicates` | - | Allow selecting the same file multiple times |
| `--seed` | `-s` | Random seed for reproducible results |

## Output Formats

### Simple (default)
Returns absolute paths of selected files, one per line:
```
/home/user/documents/file1.txt
/home/user/documents/file2.txt
```

### Detailed
Provides comprehensive information about each file:
```
[1] file1.txt
    Path: /home/user/documents/file1.txt
    Size: 1024 bytes
    Extension: .txt

[2] file2.txt
    Path: /home/user/documents/file2.txt
    Size: 2048 bytes
    Extension: .txt
```

### JSON
Machine-readable format for scripting and automation:
```json
[
  {
    "name": "file1.txt",
    "path": "/home/user/documents/file1.txt",
    "size": 1024,
    "extension": ".txt",
    "relative_path": "file1.txt"
  }
]
```

## Use Cases

- **Random Testing**: Select random files for testing purposes
- **Sampling**: Pick random samples from large datasets
- **Media Players**: Create random playlists
- **Data Processing**: Process random subsets of files
- **File Management**: Randomly select files for review or cleanup
- **Education**: Pick random files for students to analyze

## Contributing

This is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions, bug reports, and feature requests are welcome!

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Issue Reference

This implementation addresses issue [#1009](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1009) - Random File Selector

## License

This project follows the license of the parent repository [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode).

## Author

Contributed to 100 Lines of Python Code repository

---

**Note**: This tool uses Python's built-in `random` module for file selection. For cryptographically secure randomness, consider using `secrets` module instead.
