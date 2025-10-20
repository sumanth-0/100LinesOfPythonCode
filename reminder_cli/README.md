# Reminder CLI

A simple command-line reminder application that helps you schedule, list, and manage reminders directly from your terminal.

## Features

- 📅 Schedule reminders with specific date and time
- 📋 List all scheduled reminders
- 🗑️ Delete reminders by ID
- ⏰ Check for due reminders
- 💾 Persistent storage using JSON
- 🎨 Clean and intuitive terminal interface

## Installation

1. Clone this repository or download the `reminder_cli.py` file
2. Make the script executable (Linux/Mac):
   ```bash
   chmod +x reminder_cli.py
   ```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Usage

### Add a New Reminder

Schedule a reminder with a message, date, and time:

```bash
python reminder_cli.py add "Team meeting" 2025-10-20 14:30
```

Format:
- Date: `YYYY-MM-DD`
- Time: `HH:MM` (24-hour format)

### List All Reminders

View all upcoming reminders:

```bash
python reminder_cli.py list
```

Show all reminders including past ones:

```bash
python reminder_cli.py list --all
```

### Delete a Reminder

Remove a reminder by its ID:

```bash
python reminder_cli.py delete 1
```

### Check for Due Reminders

Check if any reminders are currently due:

```bash
python reminder_cli.py check
```

## Examples

```bash
# Add reminders
python reminder_cli.py add "Doctor appointment" 2025-10-25 09:00
python reminder_cli.py add "Submit report" 2025-10-22 17:00
python reminder_cli.py add "Call mom" 2025-10-21 18:30

# List all upcoming reminders
python reminder_cli.py list

# Check for due reminders
python reminder_cli.py check

# Delete a reminder
python reminder_cli.py delete 2
```

## Data Storage

Reminders are stored in a JSON file at `~/.reminders.json` in your home directory. This ensures your reminders persist between sessions.

## Output Format

When listing reminders, you'll see a formatted table:

```
============================================================
ID    Date         Time     Message
============================================================
1     2025-10-20   14:30    Team meeting
2     2025-10-25   09:00    Doctor appointment
============================================================
```

## Error Handling

- The application validates date/time format and ensures reminders are set in the future
- Clear error messages guide you if something goes wrong
- Graceful handling of missing or corrupted data files

## Use Cases

- 📝 Keep track of appointments and meetings
- ⏰ Set reminders for important tasks
- 🎯 Manage deadlines and due dates
- 💼 Organize your daily schedule
- 🔔 Never forget important events

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) collection.

Issue: #1034

## License

Feel free to use and modify this code for your personal or commercial projects.

## Tips

- Use cron jobs or task schedulers to periodically run `check` command
- Combine with notification systems for desktop alerts
- Export reminders list to integrate with other tools
- Set up aliases in your shell for quicker access

---

**Happy Organizing! 🎉**
