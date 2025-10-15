# Sleep Log Tracker

A simple and efficient Python application to track your sleep patterns by recording sleep start and end times, calculating duration, and analyzing sleep quality.

## 🎯 Features

- **Sleep Session Recording**: Record sleep start and end times with automatic timestamps
- **Duration Calculation**: Automatically calculates sleep duration in hours
- **Cross-Midnight Support**: Handles sleep sessions that span across midnight
- **Sleep Quality Rating**: Rate your sleep quality on a scale of 1-10
- **Data Persistence**: Saves all sleep data to a JSON file for long-term tracking
- **Recent Logs View**: View your recent sleep sessions with detailed information
- **Sleep Statistics**: Get comprehensive statistics about your sleep patterns
- **Compact Design**: Under 100 lines of code, following project requirements

## 🚀 How to Run

```bash
python sleep_log_tracker.py
```

## 🎮 How to Use

### Main Menu Options

1. **💤 Start Sleep** - Record when you go to bed
2. **⏰ End Sleep** - Record when you wake up (automatically calculates duration)
3. **⭐ Rate Sleep** - Rate your most recent sleep session (1-10 scale)
4. **📊 View Logs** - Display your recent sleep history
5. **📈 Statistics** - Show comprehensive sleep analytics
6. **🚪 Exit** - Close the application

### Example Usage

```
🌙 Sleep Log Tracker 🌙

1. 💤 Start Sleep  2. ⏰ End Sleep  3. ⭐ Rate Sleep
4. 📊 View Logs    5. 📈 Statistics  6. 🚪 Exit

Choose (1-6): 1
💤 Sleep started at 2024-01-15 23:30:00

Choose (1-6): 2
⏰ Sleep ended at 2024-01-16 07:15:00. Duration: 7.75 hours

Choose (1-6): 3
Rate sleep (1-10): 8
⭐ Sleep rated: 8/10
```

## 📊 Sample Output

### Recent Logs View
```
📊 Recent Sleep Logs:
==============================
💤 23:30:00 - 07:15:00 (7.75h) ⭐8/10
💤 22:45:00 - 06:30:00 (7.75h) ⭐7/10
💤 00:15:00 - Currently sleeping...
```

### Statistics View
```
📈 Sleep Statistics:
====================
📊 Sessions: 15
⏱️  Avg duration: 7.4h
🌙 Longest: 9.2h
☀️  Shortest: 5.5h
⭐ Avg quality: 7.3/10
```

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Dependencies**: Built-in modules only (json, os, datetime)
- **Data Storage**: JSON file (`sleep_log.json`)
- **Code Style**: Follows PEP 8 guidelines
- **Lines of Code**: Under 100 lines (compliant with project requirements)
- **Architecture**: Object-oriented design with clean method separation

## 📁 File Structure

```
Sleep_Log_Tracker/
├── sleep_log_tracker.py    # Main application file
├── README.md               # This documentation
└── sleep_log.json          # Data file (created automatically)
```

## 📈 Data Format

The application stores data in JSON format:

```json
[
  {
    "start": "2024-01-15 23:30:00",
    "end": "2024-01-16 07:15:00",
    "duration": 7.75,
    "quality": 8
  }
]
```

## 🌟 Key Features

### Cross-Midnight Sleep Tracking
Intelligently handles sleep sessions that cross midnight, ensuring accurate duration calculations.

### Automatic Time Stamping
Uses current time when recording sleep start/end times if no specific time is provided.

### Quality Rating System
Rate your sleep quality on a 1-10 scale:
- 1-3: Poor sleep
- 4-6: Average sleep  
- 7-8: Good sleep
- 9-10: Excellent sleep

### Comprehensive Statistics
Get insights into your sleep patterns including average duration, longest/shortest sessions, and quality ratings.

## 🎯 Use Cases

- **Sleep Hygiene Tracking**: Monitor your sleep schedule consistency
- **Health Monitoring**: Track sleep duration for health goals
- **Pattern Recognition**: Identify trends in your sleep quality
- **Sleep Optimization**: Use data to improve your sleep habits

## 🤝 Contributing

This project is part of the 100LinesOfPythonCode repository. Feel free to suggest improvements!

## 📄 Requirements

- Python 3.6 or higher
- No external dependencies required

## 🔒 Privacy

All sleep data is stored locally in a JSON file on your computer. No data is transmitted externally.

## 🌙 About

This Sleep Log Tracker was created to address GitHub issue #948 in the 100LinesOfPythonCode repository, providing a simple yet effective way to track sleep patterns and improve sleep quality through data-driven insights.
