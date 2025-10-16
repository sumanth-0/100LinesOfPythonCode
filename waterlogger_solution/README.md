#  Water Intake Logger

A simple Python command-line tool to help you track your daily water consumption and get reminders to stay hydrated.

## About

This tool lets you log your water intake throughout the day, tracks your progress against a daily goal, and sends periodic reminders to drink more water. It's designed to be straightforward and run directly from your terminal.

## Features

  * **Log Water:** Record how much water you drink (in milliliters).
  * **Daily Goal:** Set a target and see how close you are to reaching it.
  * **Reminders:** Get gentle nudges to hydrate at set intervals.
  * **Summary:** View your current total intake.

## Getting Started

### Requirements

  * Python 3.6 or newer

### How to Run

1.  Save the code as `water_logger.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using:
    ```bash
    python water_logger.py
    ```

## Usage

Once running, use these commands:

  * **`add <amount_ml>`**: Log water intake. (e.g., `add 250`)
  * **`summary`**: See your progress for the day.
  * **`quit`**: Exit the program.

## Configuration

You can easily change your daily goal and reminder interval by editing these lines in `water_logger.py`:

```python
DAILY_GOAL = 3000  # in milliliters (e.g., 3000 ml = 3 liters)
REMINDER_INTERVAL = 2 * 60 * 60 # every 2 hours (in seconds)
```


-----