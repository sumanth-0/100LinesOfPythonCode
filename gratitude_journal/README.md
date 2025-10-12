# Gratitude Journal 📔

A simple command-line interface (CLI) tool to record and view your daily gratitude entries. Practice gratitude by documenting what you're thankful for each day!

## Features

✨ **Add Gratitude Entries**: Record what you're grateful for with timestamps

📜 **List All Entries**: View your complete gratitude journal history

💾 **Persistent Storage**: All entries are saved locally in JSON format

🕐 **Automatic Timestamps**: Each entry includes the date and time it was created

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `gratitude_journal` folder
3. Make the script executable (optional):
   ```bash
   chmod +x gratitude_journal.py
   ```

## Usage

### Add a new gratitude entry

```bash
python gratitude_journal.py add "Your gratitude message"
```

**Examples:**
```bash
python gratitude_journal.py add "A beautiful sunny day"
python gratitude_journal.py add "Time spent with family"
python gratitude_journal.py add "Good health and well-being"
```

### List all entries

```bash
python gratitude_journal.py list
```

This will display all your gratitude entries with their timestamps in a formatted view.

### Show help

```bash
python gratitude_journal.py help
```

## File Structure

```
gratitude_journal/
├── gratitude_journal.py    # Main CLI application
├── README.md               # This file
└── gratitude_entries.json  # Created automatically when you add your first entry
```

## How It Works

The gratitude journal stores all entries in a `gratitude_entries.json` file in the same directory. Each entry contains:
- **date**: Timestamp when the entry was created (YYYY-MM-DD HH:MM:SS format)
- **gratitude**: Your gratitude message

## Example Output

### Adding an entry:
```
$ python gratitude_journal.py add "Grateful for my morning coffee"
✓ Gratitude entry added successfully!
  Date: 2025-10-12 19:30:00
  Entry: Grateful for my morning coffee
```

### Listing entries:
```
$ python gratitude_journal.py list

============================================================
  MY GRATITUDE JOURNAL (3 entries)
============================================================

Entry #1
Date: 2025-10-12 09:15:00
Gratitude: A beautiful sunny day
------------------------------------------------------------
Entry #2
Date: 2025-10-12 14:30:00
Gratitude: Time spent with family
------------------------------------------------------------
Entry #3
Date: 2025-10-12 19:30:00
Gratitude: Grateful for my morning coffee
------------------------------------------------------------
```

## Benefits of Gratitude Practice

Research shows that regularly practicing gratitude can:
- Improve mental health and well-being
- Increase happiness and life satisfaction
- Reduce stress and negative emotions
- Strengthen relationships
- Improve sleep quality

Make it a daily habit to record at least one thing you're grateful for!

## Code Statistics

- **Lines of Code**: 100 lines (including docstrings and comments)
- **Language**: Python 3
- **License**: Open source

## Contributing

This project is part of the 100 Lines of Python Code repository. Contributions, suggestions, and improvements are welcome!

## Author

Created as a contribution to [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode)

---

**Start your gratitude journey today! 🌟**
