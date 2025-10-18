# File Extension Counter

A Python CLI tool that counts and displays the number of files per extension in a specified directory.

## Features

- **Recursive scanning**: Counts files in all subdirectories
- **Extension tracking**: Identifies files by their extension
- **Formatted output**: Displays results in a clean, readable table format
- **Statistics**: Shows count and percentage breakdown for each extension
- **Error handling**: Gracefully handles permission errors and invalid paths
- **No extension support**: Tracks files without extensions

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation

No installation required! Simply download the script:

```bash
curl -O https://raw.githubusercontent.com/sumanth-0/100LinesOfPythonCode/main/%231005_FILE_EXTENSION_COUNTER/file_extension_counter.py
```

## Usage

### Basic Usage

Count files in the current directory:

```bash
python file_extension_counter.py
```

### Specify a Directory

Count files in a specific directory:

```bash
python file_extension_counter.py /path/to/directory
```

### Examples

```bash
# Count files in Documents folder
python file_extension_counter.py ~/Documents

# Count files in current project
python file_extension_counter.py .

# Count files in a specific path
python file_extension_counter.py /Users/username/projects
```

## Output Example

```
Scanning directory: /Users/username/projects...

============================================================
File Extension Count Report
Directory: /Users/username/projects
============================================================

Extension            Count     Percentage
-------------------- ---------- ------------
.py                      45       45.0%
.md                      20       20.0%
.txt                     15       15.0%
.json                    10       10.0%
(no extension)           10       10.0%

------------------------------------------------------------
Total Files:            100
============================================================
```

## How It Works

1. **Path Validation**: Checks if the provided path exists and is a directory
2. **Recursive Scan**: Uses `pathlib.Path.rglob()` to find all files recursively
3. **Extension Extraction**: Captures each file's extension using `Path.suffix`
4. **Counting**: Aggregates extensions using Python's `Counter` from collections
5. **Display**: Formats and displays results sorted by count (descending)

## Error Handling

The tool handles common errors gracefully:

- **Directory not found**: Displays clear error message
- **Permission denied**: Catches and reports permission issues
- **Invalid path**: Validates that the path is a directory
- **General exceptions**: Catches and displays unexpected errors

## Code Structure

- `count_extensions(directory)`: Scans directory and counts file extensions
- `display_results(extension_counts, directory)`: Formats and displays results
- `main()`: Entry point, handles command-line arguments

## Contributing

This project is part of the 100LinesOfPythonCode repository. Contributions are welcome!

For issue #1005 - File Extension Counter

## License

This project follows the license of the parent repository.

## Author

Contributed to [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) - Issue #1005
