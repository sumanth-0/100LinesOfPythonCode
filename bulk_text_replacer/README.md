# Bulk Text Replacer

## Overview

A comprehensive command-line tool for performing bulk find-and-replace operations across multiple files. This Python utility supports regular expressions, case-sensitive/insensitive matching, automatic backup creation, and interactive confirmation modes.

## Features

- 🔍 **Flexible Pattern Matching**: Support for both literal text and regular expressions
- 🔠 **Case Control**: Case-sensitive or case-insensitive matching options
- 📁 **Recursive Search**: Search through directories and subdirectories
- 🎯 **File Filtering**: Target specific file types using extension filters
- 💾 **Automatic Backups**: Create timestamped backups before modifications
- 🤝 **Interactive Mode**: Review and confirm each replacement
- 📊 **Statistics Tracking**: Detailed reports on files processed and replacements made
- ⚠️ **Error Handling**: Graceful error handling with detailed error reporting

## Installation

No external dependencies required! This tool uses only Python standard library modules.

```bash
# Clone the repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git

# Navigate to the bulk_text_replacer directory
cd 100LinesOfPythonCode/bulk_text_replacer

# Make the script executable (optional)
chmod +x bulk_text_replacer.py
```

## Usage

### Basic Syntax

```bash
python bulk_text_replacer.py <directory> <pattern> <replacement> [options]
```

### Arguments

- `directory`: Root directory to search for files
- `pattern`: Text pattern to find
- `replacement`: Text to replace with

### Options

- `-e, --extension <ext>`: Filter by file extension (e.g., `.txt`, `.py`)
- `--no-recursive`: Do not search subdirectories
- `-i, --ignore-case`: Case-insensitive matching
- `-r, --regex`: Treat pattern as regular expression
- `--no-backup`: Do not create backup files
- `--interactive`: Ask for confirmation before each replacement

## Examples

### Example 1: Simple Replacement in Text Files

Replace all occurrences of "old" with "new" in all `.txt` files:

```bash
python bulk_text_replacer.py /path/to/directory "old" "new" -e .txt
```

### Example 2: Case-Insensitive Replacement

Replace "TODO" with "DONE" (case-insensitive) in Python files:

```bash
python bulk_text_replacer.py /path/to/project "TODO" "DONE" -e .py -i
```

### Example 3: Regular Expression Replacement

Replace email addresses with a placeholder using regex:

```bash
python bulk_text_replacer.py /path/to/docs "\w+@\w+\.\w+" "[EMAIL]" -e .txt -r
```

### Example 4: Interactive Mode Without Backup

Replace "draft" with "final" with confirmation prompts:

```bash
python bulk_text_replacer.py /docs "draft" "final" --no-backup --interactive
```

### Example 5: Non-Recursive Search

Search only the top-level directory (not subdirectories):

```bash
python bulk_text_replacer.py /path/to/directory "find" "replace" --no-recursive
```

## How It Works

1. **File Discovery**: The tool scans the specified directory (recursively by default) for files matching the extension filter
2. **Pattern Matching**: For each file, it searches for the specified pattern using either literal string matching or regex
3. **Backup Creation**: If enabled, creates a timestamped backup of each file before modification
4. **Replacement**: Performs the find-and-replace operation
5. **Statistics**: Tracks and reports the number of files processed, modified, and total replacements made

## Sample Output

```
============================================================
Bulk Text Replacer
============================================================
Directory: /path/to/project
Pattern: old_function
Replacement: new_function
Recursive: True
Case-sensitive: True
Regex: False
Backup: True
============================================================

Found 15 file(s) to process...

Processing: /path/to/project/main.py
  Replaced 3 occurrence(s).
Processing: /path/to/project/utils.py
  Replaced 1 occurrence(s).
Processing: /path/to/project/config.py
  No matches found.
...

============================================================
SUMMARY
============================================================
Files processed: 15
Files modified: 8
Total replacements: 24
============================================================
```

## Code Structure

The tool is organized as a class-based design with the following main components:

- `BulkTextReplacer` class: Core functionality for file processing and replacement
  - `find_files()`: Discovers files matching the criteria
  - `create_backup()`: Creates timestamped backup files
  - `replace_in_file()`: Performs replacement operations in a single file
  - `process_files()`: Main processing loop
  - `get_statistics()`: Returns operation statistics

- `main()` function: Command-line interface using argparse

## Safety Features

- **Automatic Backups**: By default, creates timestamped backups of all modified files
- **Interactive Mode**: Option to review and confirm each replacement
- **Error Handling**: Robust error handling prevents data loss on failures
- **Preview Mode**: Preview files that would be affected (via file list output)

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Contributing

Contributions are welcome! This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Issue Reference

This implementation addresses issue [#879](https://github.com/sumanth-0/100LinesOfPythonCode/issues/879) - Bulk Text Replacer.

## License

This project follows the license of the parent repository.

## Author

Developed as part of the Hacktoberfest contribution to 100LinesOfPythonCode.

## Troubleshooting

### Common Issues

**Issue**: "Permission denied" error when modifying files
- **Solution**: Ensure you have write permissions for the target directory

**Issue**: Backup files taking up too much space
- **Solution**: Use the `--no-backup` flag if you're confident in your changes

**Issue**: Regex pattern not matching as expected
- **Solution**: Test your regex pattern separately, ensure proper escaping

**Issue**: Unicode errors when processing files
- **Solution**: The tool handles UTF-8 encoding with error ignoring, but some rare encodings may cause issues

## Tips

- Always test with a small subset of files first
- Use the `--interactive` mode when making important changes
- Keep backups enabled for critical files
- Use specific file extensions to avoid unintended replacements
- Test regex patterns with a regex tester before use

---

**Happy replacing! 🚀**
