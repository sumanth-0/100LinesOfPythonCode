# Mood Logger CLI

A command-line tool for logging and tracking your daily moods with timestamps. This application helps you maintain a record of your emotional states and provides insights through statistics and trends.

## Features

- 📝 **Log Moods**: Record your current mood with optional notes
- 👀 **View Entries**: Display recent mood logs with timestamps
- 📊 **Statistics**: View mood breakdown and trends
- 🔍 **Filter**: Filter mood entries by specific mood type
- 🗑️ **Delete**: Remove individual entries or clear all data
- 🎨 **Emoji Support**: Visual mood representation with emojis
- 💾 **Data Persistence**: All data stored locally in JSON format

## Available Moods

The application supports 15 different mood types:

- 😊 Happy
- 😢 Sad
- 😰 Anxious
- 🤩 Excited
- 😌 Calm
- 😫 Stressed
- 🙏 Grateful
- 😠 Angry
- ☮️ Peaceful
- ⚡ Energetic
- 😴 Tired
- 💪 Motivated
- 😤 Frustrated
- 😊 Content
- 😵 Overwhelmed

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/mood_logger_cli
```

2. Make the script executable (optional):
```bash
chmod +x mood_logger_cli.py
```

## Usage

### Log a Mood

Record your current mood with an optional note:

```bash
python mood_logger_cli.py log happy "Had a great day at work!"
```

Or without a note:

```bash
python mood_logger_cli.py log calm
```

### View Mood Entries

Display the last 10 mood entries (default):

```bash
python mood_logger_cli.py view
```

View a specific number of entries:

```bash
python mood_logger_cli.py view --limit 20
```

Filter by a specific mood:

```bash
python mood_logger_cli.py view --filter happy
```

### View Statistics

Display mood statistics including breakdown, percentages, and trends:

```bash
python mood_logger_cli.py stats
```

### List Available Moods

See all available mood options:

```bash
python mood_logger_cli.py list
```

### Delete an Entry

Delete a specific entry by its index (as shown in the view command):

```bash
python mood_logger_cli.py delete 1
```

### Clear All Data

Remove all mood entries (requires confirmation):

```bash
python mood_logger_cli.py clear
```

## Examples

### Example Session

```bash
# Log a few moods
$ python mood_logger_cli.py log happy "Successfully completed my project!"
😊 Mood logged successfully!
Mood: Happy
Time: 2025-10-19 10:30:45
Note: Successfully completed my project!

$ python mood_logger_cli.py log stressed "Dealing with a tight deadline"
😫 Mood logged successfully!
Mood: Stressed
Time: 2025-10-19 14:20:15
Note: Dealing with a tight deadline

# View your mood log
$ python mood_logger_cli.py view
============================================================
MOOD LOG ENTRIES
============================================================

1. 😫 STRESSED
   Time: 2025-10-19 14:20:15
   Note: Dealing with a tight deadline

2. 😊 HAPPY
   Time: 2025-10-19 10:30:45
   Note: Successfully completed my project!

============================================================

# Check your mood statistics
$ python mood_logger_cli.py stats
============================================================
MOOD STATISTICS
============================================================

Total entries: 2

Mood breakdown:
  😊 Happy           ████████████████████████ 1 (50.0%)
  😫 Stressed        ████████████████████████ 1 (50.0%)

🏆 Most common mood: 😊 Happy (1 times)

============================================================
```

## Data Storage

All mood data is stored in a JSON file located at:
- **Linux/Mac**: `~/.mood_logger_data.json`
- **Windows**: `C:\Users\<username>\.mood_logger_data.json`

### Data Format

The data file contains an array of mood entries:

```json
{
  "entries": [
    {
      "mood": "happy",
      "note": "Had a great day!",
      "timestamp": "2025-10-19T10:30:45.123456"
    }
  ]
}
```

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions are welcome!

## License

This project is open source and available under the MIT License.

## Issue Reference

This implementation addresses issue [#1031 - Mood Logger CLI](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1031)

## Author

Created as part of the 100 Lines of Python Code project for Hacktoberfest 2025.
