# Tiny Log Analyzer

A simple CLI tool to scan log files and count occurrences of specific keywords.

## Description

This tool helps analyze log files by searching for and counting occurrences of specified keywords. It's particularly useful for quickly identifying error patterns, warning frequencies, or other important events in large log files.

## Features

- **Keyword Search**: Search for multiple keywords in a single scan
- **Case Sensitivity**: Optional case-sensitive or case-insensitive matching
- **Line Numbers**: Display line numbers where keywords appear
- **Multiple Formats**: Works with any text-based log format
- **Performance**: Efficiently handles large log files

## Installation

No installation required! Just ensure you have Python 3.6+ installed.

```bash
# Clone the repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/#1010_Tiny_Log_Analyzer
```

## Usage

### Basic Usage

```bash
python log_analyzer.py <log_file> <keyword1> [keyword2] ...
```

### Examples

**Search for ERROR and WARNING in a log file:**
```bash
python log_analyzer.py server.log ERROR WARNING
```

**Case-sensitive search:**
```bash
python log_analyzer.py app.log -c Error Warning
```

**Show line numbers where keywords appear:**
```bash
python log_analyzer.py system.log -l ERROR CRITICAL
```

**Combine options:**
```bash
python log_analyzer.py debug.log -c -l Exception Traceback
```

### Command-Line Options

- `logfile`: Path to the log file to analyze (required)
- `keywords`: One or more keywords to search for (required)
- `-c, --case-sensitive`: Make keyword matching case-sensitive (default: case-insensitive)
- `-l, --lines`: Show line numbers where keywords appear
- `-h, --help`: Show help message

## Sample Output

```
==================================================
LOG ANALYSIS RESULTS
==================================================

ERROR: 45 occurrences
  Lines: 12, 34, 56, 78, 90, 123, 145, 167, 189, 201 ... (35 more)
WARNING: 23 occurrences
  Lines: 5, 15, 25, 35, 45, 55, 65, 75, 85, 95 ... (13 more)
INFO: 567 occurrences

==================================================
Total matches: 635
==================================================
```

## How It Works

1. Opens and reads the specified log file
2. Scans each line for the specified keywords
3. Counts occurrences (including multiple occurrences per line)
4. Optionally tracks line numbers where keywords appear
5. Displays results sorted by frequency

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of the 100LinesOfPythonCode repository.

## Author

Created for Issue #1010 - Tiny Log Analyzer

## Related Issues

Fixes #1010
