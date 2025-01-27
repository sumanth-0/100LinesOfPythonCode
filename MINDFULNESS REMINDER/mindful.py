import time
import random

# List of mindful reminders
reminders = [
    "Take a deep breath.",
    "Stretch for a minute.",
    "Relax your shoulders.",
    "Drink a sip of water.",
    "Close your eyes and rest for a few seconds.",
    "Smile! It's good for you.",
    "Stand up and shake your legs.",
    "Focus on your breathing for 10 seconds."
]

# Function to display reminders
def send_reminder():
    reminder = random.choice(reminders)
    print(f"Mindful Moment: {reminder}")

# Schedule reminders
def start_reminders(interval_minutes=30):
    print("Welcome to the Mindful Moments App! 🌼")
    try:
        while True:
            send_reminder()
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds
    except KeyboardInterrupt:
        print("\nStopping reminders. Stay mindful!")

# Start reminders with a 30-minute interval
start_reminders(interval_minutes=30)
