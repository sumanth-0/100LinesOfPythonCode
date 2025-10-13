# Terminal File Search

A powerful command-line tool for searching files with various filters and options.

## Description

This Python script provides a comprehensive terminal-based file search utility that allows you to search for files based on multiple criteria including name patterns, file extensions, file types, and size ranges. It supports both recursive and non-recursive searches with detailed or simple output formats.

## Features

- **Name Pattern Search**: Search files using wildcard patterns (e.g., `*.txt`, `test_*`)
- **Extension Filter**: Filter files by specific extensions
- **Type Filter**: Search specifically for files or directories
- **Size Range**: Filter by minimum and maximum file sizes
- **Recursive Search**: Search through all subdirectories
- **Verbose Output**: Display detailed information including file size and modification time
- **Result Limiting**: Limit the number of search results
- **Human-Readable Formats**: File sizes displayed in KB, MB, GB, etc.

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository or download the script
2. Make the script executable (on Unix-like systems):
```bash
chmod +x terminal_file_search.py
```

## Usage

### Basic Syntax
```bash
python terminal_file_search.py [directory] [options]
```

### Options

- `-n, --name PATTERN`: File name pattern (supports wildcards like `*` and `?`)
- `-e, --ext EXTENSION`: File extension without dot (e.g., `py`, `txt`)
- `-t, --type TYPE`: Type filter - `f` for files, `d` for directories
- `--min-size SIZE`: Minimum file size in KB
- `--max-size SIZE`: Maximum file size in KB
- `-r, --recursive`: Search recursively through subdirectories
- `-v, --verbose`: Show detailed output with file size and modification time
- `-l, --limit NUMBER`: Limit the number of results

### Examples

#### Search for all Python files in current directory
```bash
python terminal_file_search.py -e py
```

#### Search recursively for files starting with "test"
```bash
python terminal_file_search.py -n "test*" -r
```

#### Find all files larger than 100KB
```bash
python terminal_file_search.py --min-size 100 -r
```

#### Search for directories only
```bash
python terminal_file_search.py -t d -r
```

#### Verbose search for text files with size constraints
```bash
python terminal_file_search.py -e txt --min-size 10 --max-size 1000 -r -v
```

#### Search in specific directory with result limit
```bash
python terminal_file_search.py /path/to/directory -n "*.log" -r -l 10
```

#### Combine multiple filters
```bash
python terminal_file_search.py . -e py -n "*test*" --min-size 5 -r -v
```

## Output Format

### Standard Output
```
/path/to/file1.py
/path/to/file2.py
```

### Verbose Output
```
/path/to/file1.py | Size: 15.43 KB | Modified: 2025-10-12 20:30:15
/path/to/file2.py | Size: 8.21 KB | Modified: 2025-10-11 14:22:08
```

## Error Handling

- Gracefully handles permission errors
- Skips files/directories that cannot be accessed
- Provides informative error messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Issue Reference

This implementation resolves issue #788 - Terminal File Search
