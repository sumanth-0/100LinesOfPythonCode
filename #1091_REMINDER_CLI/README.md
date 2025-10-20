# Reminder CLI

A simple command-line Python program to set reminders based on **minutes, hours, days, or a specific day and time**.  

## Features

- Supports fractional times, e.g., `in 0.5 minutes` or `in 1.25 hours`.  
- Allows reminders for specific days and times, e.g., `Tuesday at 9pm`.  
- Automatically calculates the time until the reminder.  
- Runs entirely in the terminal — no GUI required.  

## How to Use

1. Run the script:  
   ```bash
   python main.py

2.	Enter what you want to be reminded of.

3.	Enter when you want to be reminded:
- Minutes: in 5 minutes
- Hours: in 1.5 hours
- Days: in 2 days
- Day and time: Tuesday at 9pm

4.	Wait for the reminder — the program will print your message when the time is up.

## Notes
- If using a day and time without specifying AM/PM, the program will ask you to clarify.
- The program sleeps until the reminder triggers, so it must remain running.

## Example
What would you like to be reminded of? Feed the cat
When would you like to be reminded? in 0.5 minutes
Alright, I’ll remind you about 'Feed the cat' in 0.5 minutes.
*waits 30 seconds*
Hey! Reminder: Feed the cat

## Requirements

- **Python 3.6+**  
- Standard library modules (already included with Python):
  - `time`
  - `re`
  - `datetime`