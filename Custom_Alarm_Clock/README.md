# Python Alarm Clock with Random Sounds

A lightweight, efficient alarm clock implementation in Python (under 100 lines) that supports multiple alarms with custom or random wake-up sounds. Perfect for daily use and learning Python's time management and sound handling capabilities.

## Features
- ⏰ Multiple alarm support
- 🎵 Custom sound selection
- 🎲 Random sound option
- ⌚ 24-hour time format
- 💻 Lightweight (< 100 lines)
- 📊 Sound file verification
- 🔄 Automatic test alarm
- 🛑 Clean exit with Ctrl+C

## Prerequisites
- Python 3.6+
- pygame library

## Quick Start
```bash
# 1. Install pygame
pip install pygame

# 2. Create project structure
mkdir alarm_clock
cd alarm_clock
mkdir sounds

# 3. Add sound files to the sounds directory
# (beep.mp3, birds.mp3, rooster.mp3)

# 4. Run the alarm clock
python alarm_clock.py
```

## Project Structure
```
alarm_clock/
│
├── alarm_clock.py
├── README.md
└── sounds/
    ├── beep.mp3
    ├── birds.mp3
    └── rooster.mp3
```

## Usage Examples

### Basic Run
```python
python alarm_clock.py
```
This will automatically set a test alarm for 1 minute from current time.

### Custom Implementation
```python
from alarm_clock import AlarmClock

clock = AlarmClock()
clock.add_alarm("07:00", "birds")    # Specific sound
clock.add_alarm("07:30")             # Random sound
clock.run()
```

### Time Format
- Use 24-hour format (HH:MM)
- Examples:
  - "07:00" = 7 AM
  - "13:30" = 1:30 PM
  - "00:00" = Midnight

## Sound Files
Place MP3 files in the `sounds` directory with these names:
- beep.mp3
- birds.mp3
- rooster.mp3

The program will verify sound files on startup and show their status:
```
Sound files status:
✅ beep: /path/to/beep.mp3
✅ birds: /path/to/birds.mp3
❌ rooster: /path/to/rooster.mp3  # Missing file
```

## Features Explanation

### Automatic Sound Verification
- Checks for sound files on startup
- Shows ✅ for found files
- Shows ❌ for missing files

### Smart Error Handling
- Fallback to system beep if sound file missing
- Clear error messages for troubleshooting
- Graceful exit with Ctrl+C

### Efficient Design
- Checks alarms every 30 seconds
- Low CPU usage
- Automatic cleanup of triggered alarms

## Troubleshooting

### No Sound Playing
1. Check sound file status in startup message
2. Verify pygame installation: `pip install --upgrade pygame`
3. Check system volume
4. Try different sound file formats

### Common Errors
- "Invalid time format": Use HH:MM format (e.g., "09:30")
- "Sound file not found": Add MP3 files to sounds directory
- "Error playing sound": Check file format and pygame installation

## Quick Tips
1. The program automatically sets a test alarm 1 minute ahead
2. Use Ctrl+C to cleanly exit the program
3. Missing sound files trigger system beep as fallback
4. Random sound selection if no specific tone specified
