# 🍅 Pomodoro Focus Timer

**Issue #771** - A simple command-line Pomodoro timer implementation to boost productivity and focus.

## Description

The Pomodoro Technique is a time management method that uses a timer to break work into focused intervals (traditionally 25 minutes) separated by short breaks. This implementation provides a clean, distraction-free command-line timer with the following features:

- **Customizable Focus Sessions**: Default 25-minute focus periods
- **Smart Break Management**: Automatic short breaks (5 min) and long breaks (15 min)
- **Visual Countdown**: Real-time display of remaining time in MM:SS format
- **Audio Alerts**: Terminal bell notification when sessions complete
- **Pause/Resume**: Keyboard interrupt handling to pause and resume sessions
- **Flexible Cycles**: Run multiple Pomodoro cycles in sequence

## Usage

### Basic Usage (4 cycles by default):
```bash
python focus_timer.py
```

### Custom Number of Cycles:
```bash
python focus_timer.py 6  # Run 6 focus sessions
```

### Interactive Controls:
- Press **Enter** to start each focus session or break
- Press **Ctrl+C** to pause the timer
- Press **Enter** again to resume, or **Ctrl+C** twice to quit

## Timer Configuration

The default durations can be modified at the top of the script:
- `FOCUS_TIME`: 25 minutes (1500 seconds)
- `SHORT_BREAK`: 5 minutes (300 seconds)
- `LONG_BREAK`: 15 minutes (900 seconds)

## Example Session

```
🍅 Pomodoro Focus Timer Started!
Running 4 focus sessions...

--- Cycle 1/4 ---
Press Enter to start focus session...
Focus Time: 24:59 

(After 25 minutes)
Focus Time: 00:00 - Complete!

Time for a short break!
Press Enter to start break...
Short Break: 04:59 
```

## Requirements

- Python 3.x
- Standard library only (no external dependencies)
- Works on Windows, macOS, and Linux

## Benefits

- ✅ Under 100 lines of clean, well-documented code
- ✅ No external dependencies required
- ✅ Cross-platform compatibility
- ✅ Keyboard interrupt handling for flexibility
- ✅ Clear visual feedback and audio alerts

---

*Perfect for developers, students, and anyone looking to improve focus and productivity!* 🎯
