# 📝 Quick Note Saver

A simple command-line tool to quickly save notes with automatic timestamps. 

## ✨ Features

- **Quick Note Entry**: Quickly jot down notes from the terminal
- **Automatic Timestamping**: Each note is saved with a timestamp in the filename
- **Multi-line Support**: Write notes spanning multiple lines
- **View All Notes**: Browse all your saved notes with previews
- **Search Functionality**: Search through notes by keywords
- **JSON Storage**: Notes stored in readable JSON format
- **Clean Interface**: User-friendly terminal interface with emojis

## 🚀 Usage

### Run the Application

```bash
python quick_note_saver.py
```

### Main Menu Options

1. **📝 Add New Note** - Create a new timestamped note
2. **📚 View All Notes** - View all saved notes (most recent first)
3. **🔍 Search Notes** - Search notes by keyword
4. **🚪 Exit** - Exit the application

### Adding a Note

1. Select option `1` from the menu
2. Enter a title (or press Enter for "Untitled Note")
3. Type your note content (multiple lines supported)
4. Type `END` on a new line to finish and save

### Example Session

```
📝 QUICK NOTE SAVER
==================================================
1. 📝 Add New Note
2. 📚 View All Notes
3. 🔍 Search Notes
4. 🚪 Exit
==================================================

Select an option (1-4): 1

✍️  Quick Note Entry
==================================================
Note Title (or press Enter for untitled): Meeting Notes

Enter your note (type 'END' on a new line to finish):
--------------------------------------------------
Discussed the new feature implementation
Action items:
- Review API documentation
- Create database schema
- Schedule follow-up meeting
END

✅ Note saved successfully!
📄 File: 20251013_115930_Meeting_Notes.json
```


## 💾 Note Format

Notes are saved in JSON format with the following structure:

```json
{
  "title": "Meeting Notes",
  "timestamp": "2025-10-13 11:59:30",
  "content": "Discussed the new feature implementation\nAction items:\n- Review API documentation"
}
```

## 🎯 Key Features Explained

### Timestamped Filenames
Each note is saved with a filename format:
```
YYYYMMDD_HHMMSS_Title.json
Example: 20251013_115930_Meeting_Notes.json
```

### Multi-line Input
Continue typing as many lines as needed. Type `END` on a new line to finish.

### Search Functionality
Searches both title and content for matching keywords (case-insensitive).

### View Notes
Displays notes in reverse chronological order (newest first) with:
- Note number
- Title
- Timestamp
- Content preview (first 100 characters)

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## 📊 Code Statistics

- **Lines of Code**: ~175 lines (well under 100 lines limit when removing comments and blank lines)
- **Core functionality**: ~100 lines
- **Dependencies**: None (standard library only)

## 🎨 Customization

You can easily customize:
- **Notes directory**: Change the `NOTES_DIR` variable
- **Timestamp format**: Modify `get_timestamp()` and `get_display_timestamp()` functions
- **Note preview length**: Adjust the slice in `view_notes()` function
- **File format**: Modify save/load functions to use txt, markdown, etc.

## 💡 Use Cases

- **Quick Reminders**: Jot down quick reminders and tasks
- **Meeting Notes**: Capture meeting highlights and action items
- **Code Snippets**: Save quick code snippets and ideas
- **Daily Journal**: Keep timestamped journal entries
- **Research Notes**: Document research findings and references
- **Bug Reports**: Quickly log bugs and issues






