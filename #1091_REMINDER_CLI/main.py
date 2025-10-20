import time
import re
from datetime import datetime, timedelta

now = datetime.now()

# Convert days into numbers
days_dict = {
    "monday": 0, "tuesday": 1, "wednesday": 2,
    "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
}

def set_reminder():
    # User inputs
    reminder = input("What would you like to be reminded of? ")
    user_input = input("When would you like to be reminded? You can specify in minutes, hours, days or a day and time. ")

    # Check for time formats
    minutes_match = re.search(r"(\d*\.?\d+)\s*(?=minutes?)", user_input, re.IGNORECASE)
    hours_match = re.search(r"(\d*\.?\d+)\s*(?=hours?)", user_input, re.IGNORECASE)
    days_match = re.search(r"(\d*\.?\d+)\s*(?=days?)", user_input, re.IGNORECASE)
    day_time_match = re.search(r"\b(?:(mon|tues|wednes|thurs|fri|satur|sun)day)\b.*?\bat\s*([0-9]{1,2}(?::[0-9]{2})?\s*(?:am|pm)?)", user_input, re.IGNORECASE)

    # Determine the reminder time
    if minutes_match:  # Check for minutes
        minutes = float(minutes_match.group(1))
        print(f"Alright, I’ll remind you about '{reminder}' in {minutes} minutes.")
    elif hours_match:  # Check for hours
        hours = float(hours_match.group(1))
        minutes = hours * 60
        print(f"Alright, I’ll remind you about '{reminder}' in {hours} hours.")
    elif days_match:  # Check for days
        days = float(days_match.group(1))
        minutes = days * 24 * 60
        print(f"Alright, I’ll remind you about '{reminder}' in {days} days.")
    elif day_time_match:  # Check for specific day and time
        target_day = day_time_match.group(1).capitalize() + "day"
        target_time = day_time_match.group(2).strip()

        if not re.search(r"(am|pm)", target_time, re.IGNORECASE):
            if ":" not in target_time:
                target_time += ":00"
            am_pm_refine = input(f"Do you mean {target_time} AM or PM? ")
            if re.search(r"(am)", am_pm_refine, re.IGNORECASE):
                target_time += " AM"
            else:
                target_time += " PM"

        # Calculate delta to target day and time
        target_day_num = days_dict[target_day.lower()]
        today_num = now.weekday()
        days_ahead = (target_day_num - today_num) % 7
        if days_ahead == 0:  # Checks if today or in a week's time is the intended reminder day
            if datetime.strptime(target_time, "%I:%M %p").time() <= now.time():
                days_ahead = 7

        target_datetime = (
        now.replace(hour=0, minute=0, second=0, microsecond=0)
        + timedelta(days=days_ahead)
        )
        target_time_obj = datetime.strptime(target_time, "%I:%M %p").time()
        target_datetime = target_datetime.replace(
            hour=target_time_obj.hour, minute=target_time_obj.minute
        )
        minutes = (target_datetime - now).total_seconds() / 60
        print(f"Alright, I’ll remind you about '{reminder}' on {target_day} at {target_time}.")
    else:
        print("Couldn’t understand the time. Try 'in 10 minutes' or 'on Tuesday at 9pm'.")

    time.sleep(minutes * 60)

    print(f"Hey! Reminder: {reminder}")

# Run reminder function
print(set_reminder())