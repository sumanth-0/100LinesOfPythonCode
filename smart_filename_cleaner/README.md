# Smart Filename Cleaner

🧹 A Python CLI tool that batch renames files in a folder for consistency by converting to snake_case, removing spaces, duplicates, and special characters.

## Features

- **Snake Case Conversion**: Converts filenames to lowercase snake_case format
- **Space Removal**: Replaces spaces and hyphens with underscores
- **Special Character Cleanup**: Removes all special characters except underscores and dots
- **Duplicate Word Removal**: Eliminates duplicate words in filenames (e.g., "file_file_name" → "file_name")
- **Conflict Resolution**: Automatically handles naming conflicts by adding numbers
- **Preview Mode**: Shows all changes before applying them
- **Safe Operations**: Preserves file extensions and prevents data loss

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/smart_filename_cleaner
```

2. No external dependencies required! Uses only Python standard library.

## Usage

### Basic Usage (with preview)
```bash
python smart_filename_cleaner.py <directory>
```

### Example
```bash
python smart_filename_cleaner.py ./downloads
```

### Skip Preview Mode
To rename files without confirmation:
```bash
python smart_filename_cleaner.py <directory> --no-preview
```

## Examples

### Before and After

| Original Filename | Cleaned Filename |
|------------------|------------------|
| `My Document (1).txt` | `my_document_1.txt` |
| `photo 2023-10-15.jpg` | `photo_20231015.jpg` |
| `File--File Name.pdf` | `file_name.pdf` |
| `Report @#$ Final.docx` | `report_final.docx` |
| `video   spaces.mp4` | `video_spaces.mp4` |

### Sample Output
```
Files to be renamed in './test_folder':
------------------------------------------------------------
My Document (1).txt           -> my_document_1.txt
photo 2023-10-15.jpg          -> photo_20231015.jpg
File--File Name.pdf           -> file_name.pdf
------------------------------------------------------------
Total: 3 files will be renamed.

Proceed with renaming? (yes/no): yes

Successfully renamed 3 out of 3 files.
```

## How It Works

1. **Scans** the specified directory for all files
2. **Cleans** each filename by:
   - Converting to lowercase
   - Replacing spaces/hyphens with underscores
   - Removing special characters
   - Eliminating duplicate underscores and words
3. **Detects** naming conflicts and adds numbers if needed
4. **Previews** all changes (unless --no-preview flag is used)
5. **Renames** files safely after user confirmation

## Requirements

- Python 3.6 or higher
- No external dependencies

## Safety Features

- Preview mode by default (see changes before applying)
- Automatic conflict resolution (adds numbers to prevent overwrites)
- Error handling for file system operations
- File extension preservation

## Contributing

This project is part of the 100 Lines of Python Code challenge. Contributions are welcome!

## License

Open source - feel free to use and modify as needed.

## Related Issue

This solution addresses issue [#648](https://github.com/sumanth-0/100LinesOfPythonCode/issues/648) in the 100LinesOfPythonCode repository.
