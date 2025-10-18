import time

def set_quick_reminder(message: str, delay_seconds: int):
    """
    Sets a reminder that prints after a specified delay.
    The program will *block* (pause) during the delay.
    """
    print(f"⏰ Reminder set for '{message}'. Waiting for {delay_seconds} seconds...")

    # Pause the program's execution for the defined time
    time.sleep(delay_seconds)

    # After the delay, print the reminder
    print("\n*********************************")
    print(f"🚨 REMINDER: {message}")
    print("*********************************")

# --- Example Usage ---
# Set a reminder for "Take a break!" in 5 seconds

reminder_message = input("Please tell me what to remind you: ")

# Prompt for wait time (in seconds) and validate input
while True:
    try:
        wait_time_input = input("Enter wait time in seconds (e.g., 5): ")
        wait_time = int(wait_time_input)
        if wait_time <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for seconds.")

set_quick_reminder(reminder_message, wait_time)

# This line will only execute *after* the delay is over.
print("\nHey get back to your reminded work !!!")