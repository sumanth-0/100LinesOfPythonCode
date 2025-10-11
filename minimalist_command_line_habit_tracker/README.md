# Minimalist Command-Line Habit Tracker

A simple, lightweight CLI tool to track daily habits with persistent JSON storage.

## Features

- **Add Habits**: Create new habits to track
- **Check Off Habits**: Mark habits as complete for the current day
- **List Habits**: View all habits with completion status and history
- **Persistent Storage**: Data saved in JSON format
- **Minimalist Interface**: Clean, distraction-free command-line experience

## Installation

1. Clone the repository or download the script
2. Ensure you have Python 3.x installed
3. No external dependencies required!

## Usage

### Add a New Habit

```bash
python minimalist_command_line_habit_tracker.py add "Exercise"
python minimalist_command_line_habit_tracker.py add "Read for 30 minutes"
```

### Check Off a Habit for Today

```bash
python minimalist_command_line_habit_tracker.py check "Exercise"
python minimalist_command_line_habit_tracker.py check "Read for 30 minutes"
```

### List All Habits

```bash
python minimalist_command_line_habit_tracker.py list
```

Output example:
```
📋 Your Habits:
----------------------------------------
✓ Exercise (completed 5 times)
○ Read for 30 minutes (completed 3 times)
----------------------------------------
```

## Data Storage

Habits are stored in a `habits.json` file in the same directory as the script. The file contains:
- List of all habits
- Completion dates for each habit

## Example Workflow

```bash
# Day 1: Set up your habits
python minimalist_command_line_habit_tracker.py add "Morning meditation"
python minimalist_command_line_habit_tracker.py add "Drink 8 glasses of water"
python minimalist_command_line_habit_tracker.py add "Write in journal"

# Complete some habits
python minimalist_command_line_habit_tracker.py check "Morning meditation"
python minimalist_command_line_habit_tracker.py check "Drink 8 glasses of water"

# Check your progress
python minimalist_command_line_habit_tracker.py list
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.
