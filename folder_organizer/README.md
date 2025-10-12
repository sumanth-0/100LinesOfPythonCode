# Folder Organizer

A Python script that automatically organizes files in a directory by moving them into categorized subfolders based on their file extensions.

## Features

- **Automatic File Categorization**: Sorts files into predefined categories:
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.ico`, `.webp`)
  - Documents (`.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`)
  - Videos (`.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`)
  - Audio (`.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`)
  - Archives (`.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`)
  - Code (`.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.h`, `.php`, `.rb`, `.go`)
  - Executables (`.exe`, `.dmg`, `.app`, `.deb`, `.rpm`, `.msi`)
  - Data (`.json`, `.xml`, `.csv`, `.sql`, `.db`, `.sqlite`)
  - Others (files with no extension or unknown extensions)

- **Duplicate Handling**: Automatically renames files if a file with the same name already exists in the destination folder
- **Safe Operation**: Only processes files in the specified directory (doesn't touch subdirectories)
- **Progress Reporting**: Displays which files are being moved and provides a summary at the end
- **Error Handling**: Gracefully handles errors and reports issues

## Requirements

- Python 3.x
- No external dependencies (uses only standard library modules: `os`, `shutil`, `pathlib`)

## Usage

### Command Line

```bash
# Organize files in a specific folder
python folder_organizer.py /path/to/folder

# Organize files in the current directory
python folder_organizer.py .
```

### Interactive Mode

Run without arguments to be prompted for the folder path:

```bash
python folder_organizer.py
```

Then enter the folder path when prompted, or press Enter to organize the current directory.

## Example

```bash
$ python folder_organizer.py ~/Downloads

Organizing files in: /Users/username/Downloads

Moved: vacation.jpg -> Images/
Moved: report.pdf -> Documents/
Moved: song.mp3 -> Audio/
Moved: movie.mp4 -> Videos/
Moved: archive.zip -> Archives/
Moved: script.py -> Code/

Organization complete!
Files moved: 6
Files skipped: 0
```

## How It Works

1. The script scans all files in the specified directory
2. For each file, it identifies the file extension
3. It determines which category the file belongs to based on its extension
4. It creates a subfolder for the category if it doesn't exist
5. It moves the file to the appropriate category subfolder
6. If a file with the same name exists, it adds a number suffix to avoid overwriting

## Safety Notes

- **Backup Important Data**: Always backup important files before running organization scripts
- **Test First**: Try the script on a test folder before using it on important directories
- **Non-Recursive**: The script only processes files in the specified directory, not in subdirectories
- **No Deletion**: The script only moves files, it never deletes them

## Contributing

This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions and improvements are welcome!

## License

This project is open source and available under the MIT License.

## References

Fixes issue [#685](https://github.com/sumanth-0/100LinesOfPythonCode/issues/685)
