# Eye Rest Notifier

A simple console-based reminder application to help prevent eye strain by prompting users to take regular breaks.

## Description

Eye Rest Notifier follows the **20-20-20 rule** recommended by optometrists:
- Every **20 minutes**, take a break
- Look at something **20 feet** away
- For at least **20 seconds**

This helps reduce digital eye strain, computer vision syndrome, and eye fatigue from prolonged screen time.

## Features

- ⏰ **Automatic Reminders**: Notifies you every 20 minutes to take an eye rest
- ⏱️ **Countdown Timer**: Displays a 20-second countdown during rest periods
- 📊 **Session Tracking**: Keeps track of total breaks completed
- 💻 **Console-Based**: Lightweight, no GUI required
- 🎨 **Clean Interface**: Clear visual feedback with emoji support
- ⌨️ **Keyboard Control**: Easy to start and stop with Ctrl+C

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation

1. Clone the repository or download the file:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/eye_rest_notifier
```

2. Make the script executable (optional, Unix/Linux/Mac):
```bash
chmod +x eye_rest_notifier.py
```

## Usage

### Basic Usage

Run the script from the command line:
```bash
python eye_rest_notifier.py
```

or on Unix/Linux/Mac:
```bash
python3 eye_rest_notifier.py
```

### Stopping the Notifier

Press `Ctrl+C` to stop the application. It will display a session summary showing the total number of breaks taken.

## How It Works

1. **Startup**: The application displays a banner with settings and start time
2. **Countdown**: Shows time remaining until the next break
3. **Break Notification**: After 20 minutes, displays a notification to rest your eyes
4. **Rest Timer**: Counts down 20 seconds for your eye rest
5. **Resume**: Press Enter to acknowledge and continue tracking
6. **Repeat**: The cycle continues until you stop the application

## Example Output

```
============================================================
               EYE REST NOTIFIER
============================================================
Interval: 20 minutes
Rest Duration: 20 seconds
Total Breaks Completed: 0
============================================================

[Started at 14:30:00]

Press Ctrl+C to stop the notifier.

Next break in: 19:45
```

When it's time for a break:
```
************************************************************
               TIME FOR EYE REST!
************************************************************

⏰ It's been 20 minutes! Time to rest your eyes.

👀 Follow the 20-20-20 rule:
   Look at something 20 feet away for 20 seconds

------------------------------------------------------------
Rest time remaining: 00:20

✓ Great job! Your eyes thank you.

Press Enter to continue...
```

## Customization

You can modify the intervals by editing the `main()` function in the script:

```python
def main():
    # Change these values as needed
    notifier = EyeRestNotifier(
        interval_minutes=20,      # Time between breaks
        rest_duration_seconds=20  # Duration of each break
    )
    notifier.run()
```

## Health Benefits

Regular eye breaks can help:
- Reduce eye strain and fatigue
- Prevent dry eyes
- Decrease risk of computer vision syndrome
- Improve focus and productivity
- Reduce headaches related to screen time

## Contributing

This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions are welcome!

## Issue Reference

Created for issue [#1077](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1077)

## License

This project follows the license of the parent repository.

## Tips

- Run the script at the start of your work session
- Actually take the breaks when prompted - don't skip them!
- Look at distant objects outside a window if possible
- Blink frequently during the rest period
- Consider adjusting screen brightness and position for optimal comfort

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Remember**: Your eyes are important! Take regular breaks and practice good screen habits. 👀✨
