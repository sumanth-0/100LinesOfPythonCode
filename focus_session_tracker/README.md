# Focus Session Tracker

A comprehensive tool to track focus/work sessions with timer, logging, and statistics.

## Features

- **⏰ Real-time Session Timer**: Live countdown display with hours:minutes:seconds format
- **💾 Automatic Logging**: All sessions saved to `focus_sessions.json` for persistent storage
- **📊 Comprehensive Statistics**: 
  - Total number of sessions
  - Completed vs interrupted sessions
  - Completion rate percentage
  - Total focus time (minutes and hours)
  - Average session duration
- **📜 Session History**: Review your 10 most recent focus sessions
- **📝 Interactive CLI Menu**: Easy-to-use command-line interface
- **⏸️ Interruption Handling**: Press Ctrl+C to stop early (progress is still saved)
- **👍 User-friendly Output**: Emoji-enhanced display for better readability

## Installation

No external dependencies required! Just Python 3.6+

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/focus_session_tracker

# Run the script
python focus_session_tracker.py
```

## Usage

### Starting the Application

```bash
python focus_session_tracker.py
```

### Menu Options

```
🎯 FOCUS SESSION TRACKER
==================================================
1. Start a focus session
2. View statistics
3. View session history
4. Clear history
5. Exit
==================================================
```

### 1. Start a Focus Session

- Enter a task name (e.g., "Study Python", "Write documentation")
- Enter duration in minutes (e.g., 25 for a Pomodoro session)
- Watch the live countdown timer
- Press `Ctrl+C` to interrupt early if needed
- Session is automatically saved when completed or interrupted

**Example:**
```
🎯 Starting focus session: Complete project documentation
⏱️  Duration: 25 minutes

⏰ Time remaining: 00:24:58
```

### 2. View Statistics

Displays comprehensive analytics:
- Total sessions count
- Number of completed sessions
- Completion rate as percentage
- Total focus time (in both minutes and hours)
- Average session duration

**Example:**
```
==================================================
📊 FOCUS SESSION STATISTICS
==================================================
Total Sessions: 15
Completed Sessions: 12
Completion Rate: 80.0%
Total Focus Time: 360.0 minutes (6.0 hours)
Average Session: 24.0 minutes
==================================================
```

### 3. View Session History

Shows your 10 most recent sessions with:
- Status (✅ completed or ⏸️ interrupted)
- Task name
- Start date and time
- Actual duration

**Example:**
```
==================================================
📜 SESSION HISTORY (Most Recent)
==================================================

1. ✅ Study Python
   Started: 2025-10-19 13:45
   Duration: 25.0 minutes

2. ⏸️ Write tests
   Started: 2025-10-19 12:30
   Duration: 18.5 minutes
==================================================
```

### 4. Clear History

Permanently deletes all saved session data.
- Asks for confirmation before deleting
- Type "yes" to confirm

### 5. Exit

Closes the application gracefully.

## Data Storage

All session data is stored in `focus_sessions.json` in the same directory.

**Session Data Structure:**
```json
{
  "task": "Task name",
  "start_time": "2025-10-19T13:45:30.123456",
  "end_time": "2025-10-19T14:10:30.123456",
  "planned_duration": 25,
  "actual_duration": 25.0,
  "completed": true
}
```

## Tips for Effective Use

1. **Pomodoro Technique**: Use 25-minute sessions with 5-minute breaks
2. **Specific Task Names**: Be clear about what you're working on
3. **Regular Reviews**: Check your statistics weekly to track productivity
4. **Completion Rate**: Aim for 80%+ completion rate
5. **Consistent Practice**: Use daily for best results

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (uses only standard library)
- **Lines of Code**: 200+ (exceeds the 100-line requirement)
- **Modules Used**: `time`, `json`, `os`, `datetime`, `pathlib`

## Implementation Features

- Object-oriented design with `FocusSessionTracker` class
- JSON-based persistent storage
- Real-time countdown with flush output
- Graceful interrupt handling with KeyboardInterrupt
- ISO format timestamps for precision
- Input validation and error handling
- Clear separation of concerns (timer, logging, statistics, history)

## Contributing

This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

Contributions for issue [#1033](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1033) are welcome!

## Issue Reference

This implementation addresses [Issue #1033: Focus Session Tracker](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1033)

## License

See the main repository for license information.

## Author

Implemented as part of the 100 Lines of Python Code challenge.

---

**Happy focusing! 🎯**
