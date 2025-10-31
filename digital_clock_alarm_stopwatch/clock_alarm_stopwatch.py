import time, os  # Import required modules

# Function to clear the console screen (works on Windows, Mac, Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display a live digital clock
def show_clock():
    while True:
        clear()
        t = time.strftime("%H:%M:%S")  # Get current time
        print("========== CLOCK ==========")
        print("Current Time:", t)
        print("===========================")
        b = input("Press 'b' to go back: ")  # Wait for user input
        if b.lower() == 'b':  # Return to main menu
            break

# Function to set and run an alarm
def set_alarm():
    # Get alarm time from user
    h = int(input("Hour (0-23): "))
    m = int(input("Minute (0-59): "))
    s = int(input("Second (0-59): "))
    print(f"Alarm set for {h:02d}:{m:02d}:{s:02d}")
    
    # Continuously check time until alarm time matches
    while True:
        t = time.localtime()
        if (t.tm_hour, t.tm_min, t.tm_sec) == (h, m, s):
            print("\n⏰ ALARM! WAKE UP! ⏰")
            for _ in range(3):  # Beep message 3 times
                print("BEEP! BEEP! BEEP!")
                time.sleep(1)
            break
        # Option to cancel alarm manually
        if input("Press 'b' + Enter to cancel or Enter to wait: ") == 'b': 
            print("Alarm cancelled.")
            break
        time.sleep(1)
    input("Press Enter to return...")

# Function to start a stopwatch
def stopwatch():
    sec = 0
    start = input("Press Enter to start or 'b' to go back: ")
    if start.lower() == 'b': 
        return
    while True:
        clear()
        # Display elapsed time in HH:MM:SS format
        print("====== STOPWATCH ======")
        print(f"Time: {sec//3600:02d}:{(sec//60)%60:02d}:{sec%60:02d}")
        print("=======================")
        print("Press 'b' + Enter to stop.")
        time.sleep(1)
        sec += 1
        # Check for stop key depending on OS
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit() and msvcrt.getch().decode().lower() == 'b':
                break
        else:
            if input() == 'b':
                break
    input("Stopped. Press Enter to return...")

# Main menu function
def main():
    while True:
        clear()
        print("==== DIGITAL TIME UTILITY ====")
        print("1. Clock\n2. Alarm\n3. Stopwatch\n4. Exit")
        choice = input("Enter your choice: ")
        # Match-case statement for menu selection
        match choice:
            case '1': show_clock()
            case '2': set_alarm()
            case '3': stopwatch()
            case '4':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")
                time.sleep(1)

# Program execution starts here
if __name__ == "__main__":
    main()
