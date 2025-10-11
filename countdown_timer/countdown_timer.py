"""
Countdown Timer
Displays a countdown in minutes and seconds in the terminal.
"""

import time

def countdown(minutes):
    total_seconds = minutes * 60
    try:
        while total_seconds >= 0:
            mins, secs = divmod(total_seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\r⏱️  {timer}", end="")
            time.sleep(1)
            total_seconds -= 1
        print("\n✅ Time's up!")
    except KeyboardInterrupt:
        print("\n⏸️ Countdown stopped by user.")

def main():
    print("\n⏳ Countdown Timer ⏳")
    while True:
        print("\nMenu:")
        print("1️⃣  Start Countdown")
        print("2️⃣  Exit")
        choice = input("Choose an option (1-2): ").strip()
        if choice == "1":
            try:
                minutes = int(input("Enter time in minutes: ").strip())
                if minutes > 0:
                    countdown(minutes)
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            print("Goodbye! ⏱️")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
