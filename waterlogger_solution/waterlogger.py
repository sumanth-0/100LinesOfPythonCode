"""
Water Intake Logger
Author: Your Name
A simple Python tool to track your daily water consumption and suggest reminders.
"""

import time
from datetime import datetime

# --- Configuration ---
DAILY_GOAL = 3000  # in milliliters (3 liters)
REMINDER_INTERVAL = 2*60*60 # every 2 hours (in seconds)

# --- Data Storage ---
water_log = []  # each entry: (timestamp, amount_ml)

def log_intake(amount):
    """Logs water intake in ml with current timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    water_log.append((timestamp, amount))
    print(f"✅ Logged {amount} ml at {timestamp}")

def total_intake():
    """Returns total water consumed today."""
    return sum(amount for _, amount in water_log)

def show_summary():
    """Displays today's progress and remaining goal."""
    total = total_intake()
    remaining = max(0, DAILY_GOAL - total)
    print("\n💧 Daily Water Summary")
    print(f"Total consumed: {total} ml")
    print(f"Remaining: {remaining} ml")
    if total >= DAILY_GOAL:
        print("🎉 Great job! You’ve reached your daily goal!\n")
    else:
        print(f"🚰 Keep hydrating! You need {remaining} ml more.\n")

def reminder():
    """Suggests drinking water periodically."""
    print("🔔 Reminder: Time to drink some water!\n")

def main():
    print("💧 Welcome to the Water Intake Logger!")
    print(f"Your daily goal: {DAILY_GOAL} ml")
    print("Commands: [add <ml>] to log, [summary] to view, [quit] to exit.\n")

    last_reminder = time.time()
    while True:
        # Check if it’s time for a reminder
        if time.time() - last_reminder >= REMINDER_INTERVAL:
            reminder()
            last_reminder = time.time()

        command = input("> ").strip().lower()

        if command == "quit":
            show_summary()
            break
        elif command.startswith("add "):
            try:
                amount = int(command.split()[1])
                log_intake(amount)
            except (IndexError, ValueError):
                print("❌ Please enter a valid number, e.g., 'add 250'")
        elif command == "summary":
            show_summary()
        else:
            print("❓ Unknown command. Try 'add 250', 'summary', or 'quit'.")

if __name__ == "__main__":
    main()
