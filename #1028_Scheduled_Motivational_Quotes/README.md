# 💪 Scheduled Motivational Quote Printer

A Python program that displays random motivational quotes at scheduled times throughout the day to keep you motivated and inspired!

## 🌟 Features

- **25+ Motivational Quotes** - Curated collection of inspiring quotes from famous personalities
- **Multiple Modes**:
  - Default schedule (9 AM, 12 PM, 3 PM, 6 PM)
  - Custom time schedule
  - Show quote immediately
  - Continuous mode (quote every X minutes)
- **Beautiful Formatting** - Clean, formatted output with timestamps
- **Easy Scheduling** - Simple time-based scheduling system
- **Keyboard Interrupt Handling** - Graceful exit with Ctrl+C

## 📋 Requirements

- Python 3.6+
- `schedule` library

## 🚀 Installation

Install the required package:
```bash
pip install schedule
```

## 💻 Usage

Run the program:
```bash
python main.py
```

### Mode Options

**1. Default Schedule**
- Quotes appear at 9:00 AM, 12:00 PM, 3:00 PM, and 6:00 PM
- Perfect for a standard workday

**2. Custom Times**
- Set your own schedule
- Enter times in HH:MM format (24-hour)
- Add as many times as you want

**3. Show Quote Now**
- Display a random quote immediately and exit
- Great for quick motivation

**4. Continuous Mode**
- Get quotes at regular intervals
- Specify interval in minutes
- Perfect for focused work sessions

## 📝 Example Output

```
================================================================================
⏰ TIME: 09:00:15
================================================================================

💡 The only way to do great work is to love what you do. - Steve Jobs

================================================================================
```

## 🎯 Example Usage Scenarios

### For Daily Motivation
```
Choose mode: 1 (Default schedule)
```
Get motivational quotes at key times during your day.

### For Study/Work Sessions
```
Choose mode: 4 (Continuous mode)
Enter interval: 30
```
Get a quote every 30 minutes during your work session.

### Quick Inspiration
```
Choose mode: 3 (Show quote now)
```
Get instant motivation whenever you need it.

## 🔧 How It Works

1. The program uses the `schedule` library for time-based job scheduling
2. Maintains a collection of 25+ motivational quotes
3. Randomly selects quotes to prevent repetition
4. Displays quotes with timestamp and formatting
5. Runs continuously in the background, checking for scheduled times

## 📚 Customization

You can easily add more quotes by editing the `MOTIVATIONAL_QUOTES` list in `main.py`:

```python
MOTIVATIONAL_QUOTES = [
    "Your custom quote here. - Author",
    # Add more quotes...
]
```

## ⚡ Tips

- Run in a background terminal to keep it active all day
- Use Task Scheduler (Windows) or cron (Linux/Mac) to auto-start on boot
- Combine with system notifications for even better experience
- Adjust times to match your daily routine

## 🤝 Contributing

Feel free to contribute more motivational quotes or features!

## 📄 License

This project is open source and available for educational purposes.

---

**Stay motivated! 💪**
