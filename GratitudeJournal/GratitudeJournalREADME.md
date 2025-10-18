#  Gratitude Journal

A lightweight, cross-platform CLI tool for daily gratitude journaling. Track what you're grateful for each day with timestamped entries, view your history, and export your reflections to markdown.

## Features

-  **Daily Gratitude Prompts** — Write multiline entries about what you're grateful for
-  **Timestamped Entries** — Automatic date and time tracking for each entry
-  **View History** — Browse today's entry or your entire journal
-  **Manage Entries** — Delete entries you no longer need
-  **Export to Markdown** — Convert your journal to a beautifully formatted markdown file
-  **Persistent Storage** — All entries saved locally in JSON format
-  **No Dependencies** — Uses only Python standard library
-  **Cross-Platform** — Works on Windows, macOS, and Linux

## Installation

### Requirements

- Python 3.7 or higher

### Setup

1. **Clone the repository** (or download the script)

    ```bash
    git clone https://github.com/yourusername/gratitude-journal.git
    cd gratitude-journal
    ```

2. **Make the script executable** (macOS/Linux only)

    ```bash
    chmod +x gratitude_journal.py
    ```

3. **Run the program**

    ```bash
    python gratitude_journal.py
    ```


## Usage

### Starting the Journal

```bash
python gratitude_journal.py
```

You'll see an interactive menu with the following options:
### Menu Options
|Option|Description|
|---|---|
|**1. Add today's gratitude**|Write a new entry. Press Enter twice to finish.|
|**2. View today's entry**|Display your gratitude entry for today.|
|**3. View all entries**|Browse your complete journal history.|
|**4. Delete an entry**|Remove an entry by its number.|
|**5. Export to markdown**|Save your journal as a formatted markdown file.|
|**6. Exit**|Close the application.|
### Example Workflow
```
🙏 Gratitude Journal
==================================================
1. Add today's gratitude
2. View today's entry
3. View all entries
4. Delete an entry
5. Export to markdown
6. Exit
==================================================
Enter your choice (1-6): 1
📝 What are you grateful for today?
(Enter multiple lines. Press Enter twice when done)
I'm grateful for my health and the support of my friends.
Today was a good day at work.

✅ Gratitude entry saved successfully!
```

## Data Storage

### Location

- **JSON entries**: `~/.gratitude_journal/entries.json`
- **Markdown exports**: `~/.gratitude_journal/gratitude_journal_export.md`

### Format

Entries are stored in JSON format with the following structure:

```json
{
  "date": "2025-10-17",
  "timestamp": "2025-10-17T14:32:15.123456",
  "content": "Grateful for my friends and family..."
}
```

### Markdown Export

When you export to markdown, your entries are formatted as:

```markdown
# 🙏 Gratitude Journal

*Exported on 2025-10-17 14:32:15*

---

## 2025-10-17 at 14:32:15

Grateful for my friends and family...

---
```

## Project Structure

```
gratitude-journal/
├── gratitude_journal.py    # Main application
├── README.md               # This file
└── LICENSE                 # License (if applicable)
```

## Features in Detail

### Adding Entries

- Write multiple lines of text
- Press Enter twice to save
- Entries are automatically timestamped
- Empty entries are rejected

### Viewing Entries

- **Today's Entry**: Quick access to your most recent reflection
- **All Entries**: Chronological list of all your journal entries
- **Numbered Display**: Easy reference for deletion

### Exporting

- Export your entire journal to a markdown file
- Perfect for sharing, printing, or archiving
- UTF-8 encoding supports all languages and emojis

## Error Handling

The application includes robust error handling for:

- Invalid menu choices
- File I/O errors
- JSON parsing errors
- Empty entries
- Invalid entry numbers

## Future Enhancements

Potential features for future versions:

-  End-to-end encryption for privacy
-  Search functionality to find entries by keyword
-  Gratitude streak counter
- Cloud synchronization
-  GUI interface
-  Mobile app version
-  Email reminders

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with:

- Bug fixes
- New features
- Documentation improvements
- Code optimizations

## License

This project is licensed under the MIT License — see the LICENSE file for details.

## Support

If you encounter any issues:

1. Check that Python 3.7+ is installed: `python --version`
2. Ensure you have write permissions to your home directory
3. Try deleting `~/.gratitude_journal/` and restarting (backs up your entries first!)
4. Open an issue on GitHub with details about the error

## Acknowledgments

Built with ❤️ to help people practice gratitude and mindfulness.

---

**Start your gratitude journey today!** 🌟