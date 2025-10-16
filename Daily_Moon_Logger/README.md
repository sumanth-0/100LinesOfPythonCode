# Daily Mood Logger 🌙

A simple and intuitive Python script to track your daily mood and maintain a personal emotional journal.

## Description

Daily Mood Logger helps you keep track of your emotional well-being by logging your mood each day. The data is saved locally in a CSV file, making it easy to analyze your mood patterns over time.

## Features

- 📝 Log your mood (Happy, Sad, Neutral)
- 📅 Automatic date and timestamp recording
- 💭 Add optional notes to your mood entries
- 📊 View your mood history
- 📈 Get mood statistics and insights
- 💾 Data stored locally in CSV format

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone the repository or download the script
2. Navigate to the `Daily_Moon_Logger` directory
3. Run the script:

```bash
python daily_moon_logger.py
```

## Usage

When you run the script, you'll see a menu with the following options:

```
1. Log today's mood
2. View mood history
3. View mood statistics
4. Exit
```

### Logging Your Mood

1. Select option 1 from the main menu
2. Choose your current mood:
   - Happy
   - Sad
   - Neutral
3. Optionally add a note to describe your feelings
4. Your mood will be saved with the current date and time

### Viewing History

Select option 2 to view your recent mood entries. You can specify how many entries you want to see, or press Enter to see the last 7 entries by default.

### Mood Statistics

Select option 3 to see:
- Total number of mood entries
- Mood distribution (percentage of each mood)
- Overall mood insights

## Data Storage

All mood data is stored in `mood_log.csv` in the same directory as the script. The CSV file contains:

- **Date**: The date of the mood entry (YYYY-MM-DD)
- **Time**: The time of the mood entry (HH:MM:SS)
- **Mood**: Your mood (happy, sad, or neutral)
- **Note**: Optional note about your mood

Example CSV structure:
```csv
Date,Time,Mood,Note
2025-10-13,14:30:45,happy,Had a great day at work!
2025-10-14,09:15:22,neutral,Feeling okay today
```

## Example Output

```
========================================
  Daily Mood Logger
========================================

Options:
1. Log today's mood
2. View mood history
3. View statistics
4. Exit

Enter your choice (1-4): 1

Available moods: happy, sad, neutral
Enter your mood: happy
Add a note (optional): Finished a great project!

✓ Mood logged: happy on 2025-10-13 at 14:30:45
```

## Privacy

All your mood data is stored locally on your computer. No data is transmitted or shared online.

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Feel free to suggest improvements or report issues!

## License

This project follows the license of the parent repository.

## Author

Created as a contribution to 100 Lines of Python Code project (Issue #847)
