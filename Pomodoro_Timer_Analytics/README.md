# Pomodoro Timer with Focus Analytics

## Description
A Python implementation of the Pomodoro Technique with comprehensive focus analytics and productivity tracking. This script helps you manage your work sessions using the proven Pomodoro method while providing detailed insights into your productivity patterns.

## Features

### Pomodoro Timer Logic
- **25-minute work sessions**: Focused work intervals based on the Pomodoro Technique
- **5-minute short breaks**: Quick breaks between work sessions
- **15-minute long breaks**: Extended breaks after every 4th session
- **Real-time countdown display**: Visual timer showing remaining time

### Focus Analytics
- **Session Tracking**: 
  - Total sessions started
  - Completed sessions count
  - Interrupted sessions count
- **Productivity Metrics**:
  - Total focus time in minutes
  - Completion rate percentage
  - Session history with timestamps
- **Data Persistence**: All analytics automatically saved to JSON file

## Installation

No external dependencies required! Uses only Python standard library:
```python
import time
import json
import os
from datetime import datetime
```

## Usage

### Basic Usage
```bash
python pomodoro_analytics.py
```

### How It Works
1. Run the script to start your first Pomodoro session
2. The timer will count down from 25 minutes (work session)
3. After completion, you'll get a break (5 or 15 minutes depending on session number)
4. After each session, choose whether to continue or stop
5. View your analytics dashboard at any time

### Controls
- **Ctrl+C**: Interrupt current session (tracked as interrupted)
- **y/n**: Continue or stop after each session

## Analytics Dashboard

The script displays a comprehensive analytics dashboard showing:
```
📊 Focus Analytics Dashboard
==================================================
Total Sessions Started: X
Completed Sessions: Y
Interrupted Sessions: Z
Total Focus Time: N minutes
Completion Rate: XX.X%

Recent Sessions:
  Session #1: ✓ Completed (2025-10-11 10:30:00)
  Session #2: ✓ Completed (2025-10-11 11:00:00)
  Session #3: ✗ Interrupted (2025-10-11 11:35:00)
==================================================
```

## Data Storage

All analytics are automatically saved to `pomodoro_analytics.json` in the same directory. The file includes:
- Total and completed session counts
- Focus time tracking
- Detailed session history with timestamps
- Completion status for each session

## Code Structure

- **Line count**: 100 lines (meets repository requirements)
- **Class-based design**: `PomodoroTimer` class encapsulates all functionality
- **Well-commented**: Clear documentation for maintainability
- **Python best practices**: Following PEP 8 style guidelines

## Example Session

```
🍅 Pomodoro Session #1 starting...
Work Time: 24:59
...
Work Time: 00:00
Work Time completed! 🎉

Starting Short Break...
Short Break: 04:59
...
Short Break completed! 🎉

Continue to next session? (y/n): y
```

## Contributing

This script is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

For contributions or improvements:
1. Follow the repository's contribution guidelines
2. Keep code under 100 lines
3. Maintain clear documentation

## References

- **Issue**: [#627 - Pomodoro Timer with Focus Analytics](https://github.com/sumanth-0/100LinesOfPythonCode/issues/627)
- **Repository**: [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode)

## License

Follows the parent repository's license terms.

---

**Author**: DevNexis  
**Created**: October 2025  
**Purpose**: Issue #627 Solution
