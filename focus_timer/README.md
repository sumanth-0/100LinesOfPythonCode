# Focus Timer

A simple and elegant Pomodoro/focus timer CLI tool that helps you stay productive with timed work sessions.

## Features

- ⏱️ **Countdown Timer**: Visual countdown with progress bar
- 🔔 **System Notifications**: Desktop notifications when timer completes (requires `plyer`)
- ⚙️ **Customizable**: Set custom duration and session labels
- ⌨️ **Keyboard Controls**: Graceful handling of interruptions (Ctrl+C)
- 📊 **Visual Progress**: Real-time progress bar in terminal
- 🎯 **Focused**: Minimal distractions, maximum productivity

## Installation

1. Clone this repository or download `focus_timer.py`
2. (Optional) Install dependencies for system notifications:
   ```bash
   pip install plyer
   ```

## Usage

### Basic Usage (Default 25-minute Pomodoro)
```bash
python focus_timer.py
```

### Custom Duration
```bash
python focus_timer.py --duration 50
```

### Custom Duration with Label
```bash
python focus_timer.py -d 5 -l "Short Break"
```

### Options
- `-d`, `--duration`: Duration in minutes (default: 25)
- `-l`, `--label`: Label for the timer session (default: "Focus Session")
- `-h`, `--help`: Show help message

## Examples

**Standard Pomodoro (25 minutes)**
```bash
python focus_timer.py
```

**Long Focus Session (50 minutes)**
```bash
python focus_timer.py --duration 50 --label "Deep Work"
```

**Short Break (5 minutes)**
```bash
python focus_timer.py -d 5 -l "Break Time"
```

## How It Works

1. Run the script with your desired duration
2. Watch the countdown timer with visual progress bar
3. Receive a notification when time is up
4. Press Ctrl+C anytime to pause and see remaining time

## Requirements

- Python 3.6+
- `plyer` (optional, for desktop notifications)

## Pomodoro Technique

The Pomodoro Technique is a time management method:
1. Work for 25 minutes (one "Pomodoro")
2. Take a 5-minute break
3. After 4 Pomodoros, take a longer 15-30 minute break

This tool makes it easy to implement this technique!

## License

Free to use and modify.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Note**: This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository. The entire implementation is under 100 lines of Python code!
