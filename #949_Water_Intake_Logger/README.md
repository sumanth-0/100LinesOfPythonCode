# 💧 Water Intake Logger

A simple Python application to track your daily water consumption with visual progress tracking and helpful reminders.

## Features

- ✅ **Quick Add Buttons** - Easily log water intake with 250ml, 500ml, and 750ml preset buttons
- 📊 **Visual Progress Bar** - See your progress toward your daily goal at a glance
- 🎯 **Customizable Daily Goal** - Set your own hydration target (default: 2000ml)
- 🔔 **Smart Reminders** - Get notified when you're below 50% of your daily goal
- 💾 **Persistent Data** - Your intake history is automatically saved to a JSON file
- 🔄 **Reset Function** - Start fresh each day with the reset button
- 🖥️ **Clean GUI** - Simple and intuitive Tkinter interface

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone or download this repository
2. No additional dependencies needed - uses only Python standard library!

## Usage

Run the application:

```bash
python main.py
```

### How to Use

1. **Log Water Intake**: Click one of the quick-add buttons (250ml, 500ml, 750ml)
2. **Check Progress**: View your total intake and progress bar
3. **Change Goal**: Click "⚙️ Change Goal" to set a custom daily target
4. **Reset**: Click "🔄 Reset Today" to clear today's entries
5. **Reminders**: The app will remind you to drink more if you're below 50% of your goal

## File Structure

```
water-intake-logger/
├── main.py           # Application entry point (~8 lines)
├── logger.py         # Backend logic and data management (~102 lines)
├── gui.py            # Tkinter GUI interface (~108 lines)
├── water_data.json   # Auto-generated data storage
└── README.md         # This file
```

## Project Structure

### main.py
Entry point that launches the application.

### logger.py
Core backend functionality:
- Load/save data to JSON
- Track water intake with timestamps
- Calculate daily totals and progress
- Manage daily goals
- Check reminder status

### gui.py
Tkinter-based user interface:
- Clean, simple layout
- Quick-add buttons for common amounts
- Progress visualization
- Settings and reset functionality

## Data Storage

Water intake data is stored in `water_data.json` in the following format:

```json
{
    "goal": 2000,
    "entries": [
        {
            "date": "2025-10-15",
            "time": "09:30:45",
            "amount": 250
        }
    ]
}
```
**Stay hydrated!** 💧