# ASCII Digital Clock

A live-updating digital clock made entirely from ASCII characters in Python with a beautifully bordered display.

## Features

- **Real-time updates**: The clock updates every second automatically
- **ASCII art digits**: Beautiful block-style ASCII representations of numbers 0-9
- **Dynamic sizing**: The border box automatically adjusts to fit the time display
- **Perfect alignment**: All digits are consistently sized for proper visual alignment
- **Compact design**: Optimized spacing for clean, professional appearance
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Easy to use**: Simply run the script and enjoy!

## Files

- `ascii_clock.py` - Main clock application with live updates
- `test_clock.py` - Test script to verify functionality without live updates
- `README.md` - This documentation file

## How to Use

### Run the Live Clock
```bash
python ascii_clock.py
```

The clock will start immediately and display the current time in ASCII format within a decorative border. It updates every second automatically.

### Stop the Clock
Press `Ctrl+C` to stop the clock and return to the command prompt.

### Test the Clock
```bash
python test_clock.py
```

This will display a single snapshot of the current time in ASCII format without the live updates or border.

## Example Output

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                    ASCII CLOCK                                    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                   ║
║            ██████   ██████       ██████   ██████       ██████  ██    ██           ║
║                ██       ██  ██        ██ ██    ██  ██  ██    ██ ██    ██          ║
║            ██████   ██████       ██████   ██████      ██    ██ ████████           ║
║          ██             ██  ██  ██       ██    ██  ██  ██    ██       ██          ║
║           ████████  ██████      ████████  ██████       ██████        ██           ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝

Press Ctrl+C to stop the clock
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in modules)

## How It Works

1. **ASCII Digit Definitions**: Each digit (0-9) is represented as a 5-line ASCII art pattern using block characters (█), all consistently sized to 8 characters wide
2. **Time Formatting**: Uses Python's `datetime` module to get the current time in HH:MM:SS format
3. **Dynamic Box Sizing**: Calculates the required width based on the actual time display and creates a properly sized border
4. **Perfect Centering**: Each line of the time display is individually centered within the border box
5. **Compact Spacing**: Uses single-space separation between digits and a compact colon design for optimal fit
6. **Real-time Updates**: Uses a simple `while` loop with `time.sleep(1)` to update every second

## Technical Improvements

- **Consistent Width**: All ASCII digit patterns are exactly 8 characters wide for perfect alignment
- **Dynamic Layout**: The border automatically adjusts to accommodate different time displays
- **Optimized Spacing**: Reduced spacing between characters for a more compact, professional look
- **Clean Borders**: Uses Unicode box-drawing characters for a polished appearance

## Customization

You can easily customize the clock by:
- Modifying the ASCII digit patterns in the `digits` dictionary (ensure they remain 8 characters wide)
- Changing the display format (add AM/PM, change to 12-hour format)
- Adjusting the update frequency by changing the sleep time
- Adding colors using ANSI escape codes (on supported terminals)
- Modifying the border characters or adding decorative elements

Enjoy your ASCII digital clock! 🕐✨
