# Auto Screenshot Organizer

Automatically organize screenshots from a directory into date-based folders.

## Description

This CLI tool scans a directory for screenshot files and organizes them into folders based on their creation/modification date. It identifies screenshots based on common naming patterns and file extensions.

## Features

- 🔍 **Smart Detection**: Automatically identifies screenshots based on common naming patterns
- 📅 **Date-Based Organization**: Organizes files into folders by date (YYYY-MM-DD format)
- 🔄 **Duplicate Handling**: Automatically handles duplicate filenames
- 👁️ **Dry Run Mode**: Preview changes before moving files
- 🎯 **Flexible Destination**: Specify custom destination directory or use default
- 📊 **Progress Feedback**: Shows what's being moved in real-time

## Supported Screenshot Patterns

The tool recognizes files with these patterns in their names:
- `screenshot`
- `screen shot` or `screen_shot`
- `capture`
- `scr_` followed by numbers
- `img_` followed by numbers

## Supported File Extensions

- `.png`
- `.jpg` / `.jpeg`
- `.gif`
- `.bmp`
- `.tiff`
- `.webp`

## Usage

### Basic Usage

```bash
python auto_screenshot_organizer.py /path/to/screenshots
```

This will create a `Screenshots_Organized` folder in the source directory and organize all screenshots by date.

### Specify Custom Destination

```bash
python auto_screenshot_organizer.py /path/to/screenshots -d /path/to/destination
```

### Dry Run (Preview Only)

```bash
python auto_screenshot_organizer.py /path/to/screenshots --dry-run
```

This shows what would be moved without actually moving any files.

## Examples

### Example 1: Organize Downloads folder

```bash
python auto_screenshot_organizer.py ~/Downloads
```

### Example 2: Organize to specific location

```bash
python auto_screenshot_organizer.py ~/Desktop -d ~/Pictures/Screenshots
```

### Example 3: Preview changes first

```bash
python auto_screenshot_organizer.py ~/Desktop --dry-run
```

## Output Structure

The tool creates a folder structure like this:

```
Screenshots_Organized/
├── 2024-10-15/
│   ├── screenshot_001.png
│   └── screen_capture_01.jpg
├── 2024-10-16/
│   └── screenshot_002.png
└── 2024-10-18/
    └── screen_shot_2024.png
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

1. Download the script
2. Make it executable (optional):
   ```bash
   chmod +x auto_screenshot_organizer.py
   ```

## Contributing

Feel free to submit issues or pull requests for improvements!

## License

This project is open source and available for anyone to use and modify.
