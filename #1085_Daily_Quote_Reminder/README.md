# Daily Quote Reminder

## Description
A Python CLI tool that displays motivational quotes at scheduled times to keep you inspired throughout the day.

## Features
- 🎯 Display random motivational quotes from a curated collection of 20 inspiring quotes
- ⏰ Schedule quotes at specific times (e.g., 09:00 AM daily)
- ⏱️ Set custom intervals between quotes (default: 24 hours)
- 🚀 Get an instant quote with the `--now` flag
- 💡 Simple and lightweight CLI interface

## Usage

### Display a quote immediately
```bash
python daily_quote_reminder.py --now
```

### Schedule daily quotes at 9:00 AM
```bash
python daily_quote_reminder.py --time 09:00
```

### Set custom interval (e.g., every 6 hours)
```bash
python daily_quote_reminder.py --interval 6
```

### Default behavior (24-hour interval)
```bash
python daily_quote_reminder.py
```

## Installation

1. Clone the repository
2. Navigate to the `#1085_Daily_Quote_Reminder` directory
3. Run the script with Python 3

```bash
cd #1085_Daily_Quote_Reminder
python daily_quote_reminder.py --now
```

## Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Examples

### Example Output
```
================================================================================
DAILY MOTIVATIONAL QUOTE
================================================================================

The only way to do great work is to love what you do. - Steve Jobs

================================================================================
Time: 2025-10-18 14:30:00
================================================================================
```

## Contributing
Feel free to contribute by:
- Adding more inspirational quotes
- Improving the scheduling functionality
- Enhancing the CLI interface

## License
This project is part of the 100LinesOfPythonCode repository.

## Issue Reference
Resolves issue [#1085](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1085)
