# File Name Sanitizer

## Description

A Python utility that cleans filenames in a folder by removing spaces and special characters, making them filesystem-friendly and safe for cross-platform usage.

## Features

- **Automatic Sanitization**: Removes spaces (replaced with underscores) and special characters from filenames
- **Safe Processing**: Preserves file extensions and handles edge cases
- **Dry-Run Mode**: Preview changes before applying them
- **Conflict Resolution**: Automatically handles filename conflicts by appending numbers
- **User-Friendly Output**: Clear progress indicators and summary statistics
- **Error Handling**: Robust validation of folder paths and file operations

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository or download the script
2. No additional installation needed - pure Python!

## Usage

### Basic Usage

Sanitize files in the current directory:
```bash
python file_name_sanitizer.py
```

### Specify a Folder

Sanitize files in a specific folder:
```bash
python file_name_sanitizer.py /path/to/folder
```

### Dry-Run Mode

Preview changes without actually renaming files:
```bash
python file_name_sanitizer.py /path/to/folder --dry-run
# or use the short flag
python file_name_sanitizer.py /path/to/folder -d
```

## Examples

### Example 1: Basic Sanitization

**Before:**
- `My Document (1).pdf`
- `Photo@2024!.jpg`
- `Report #5 - Final.docx`

**After:**
- `My_Document_1.pdf`
- `Photo2024.jpg`
- `Report_5_Final.docx`

### Example 2: Handling Conflicts

If `document.txt` already exists and `document (1).txt` gets sanitized to the same name, it will automatically become `document_1.txt`.

### Example 3: Dry-Run Output

```
File Name Sanitizer
==================================================
[DRY RUN MODE - No files will be renamed]

Processing 3 file(s) in '/home/user/documents'...

→ Would rename: 'My Document (1).pdf' → 'My_Document_1.pdf'
→ Would rename: 'Photo@2024!.jpg' → 'Photo2024.jpg'
✓ Skipped: 'clean_file.txt' (already clean)

Summary: 2 file(s) renamed, 1 file(s) skipped.
```

## How It Works

1. **Scans** the specified folder for all files (skips subdirectories)
2. **Analyzes** each filename to determine if sanitization is needed
3. **Transforms** filenames by:
   - Replacing spaces with underscores
   - Removing special characters (keeps alphanumeric, underscores, and hyphens)
   - Removing multiple consecutive underscores
   - Trimming leading/trailing underscores and hyphens
4. **Checks** for naming conflicts and resolves them automatically
5. **Renames** files (or shows preview in dry-run mode)
6. **Reports** summary of operations performed

## Sanitization Rules

- **Spaces** → Converted to underscores (`_`)
- **Special Characters** → Removed (except hyphens and underscores)
- **Multiple Underscores** → Collapsed to single underscore
- **Leading/Trailing Special Chars** → Removed
- **Empty Names** → Replaced with `unnamed_file`
- **File Extensions** → Always preserved

## Contributing

This script was created for issue [#1013](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1013) of the 100LinesOfPythonCode repository.

Contributions are welcome! Please ensure:
- Code stays within 100 lines (excluding comments and blank lines)
- Follows Python best practices
- Includes proper error handling

## License

This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Please refer to the main repository for license information.

## Author

Created as part of Hacktoberfest 2024 contributions.

## Related Issues

- Original Issue: [#1013 - File Name Sanitizer](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1013)

---

**Note**: Always backup important files before running batch rename operations!
