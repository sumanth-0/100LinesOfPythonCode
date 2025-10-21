import time
import sys
import select
from datetime import timedelta

def format_duration(seconds):
    """Convert seconds to hh:mm:ss format."""
    return str(timedelta(seconds=max(0, int(seconds))))

def print_menu():
    print("\n--- Productive Time Tracker ---")
    print("1. Start productive time")
    print("2. Start break")
    print("3. Show summary")
    print("4. Exit")

def wait_for_enter_with_countdown(duration_seconds, label="Time left"):
    end_time = time.time() + duration_seconds
    print(f"{label}: {format_duration(duration_seconds)} (Press ENTER to stop)", end="", flush=True)
    while True:
        remaining = int(end_time - time.time())
        print(f"\r{label}: {format_duration(remaining)} (Press ENTER to stop)", end="", flush=True)
        if remaining <= 0:
            print("\nTime is up!")
            break
        if sys.stdin in select.select([sys.stdin], [], [], 1)[0]:
            sys.stdin.readline()
            print("\nStopped by user.")
            break

def main():
    productive_times = []
    break_times = []
    mode = None  # 'work' or 'break'

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                expected_time = float(input("Wanted productive time (minutes): "))
                if expected_time <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if mode == 'work':
                print("You are already in productive mode!")
                continue
            mode = 'work'
            print("Productive time started.")
            start = time.time()
            wait_for_enter_with_countdown(expected_time * 60, label="Time left")
            end = time.time()
            productive_times.append(end - start)
            print(f"Productive time recorded: {format_duration(end - start)}")
            mode = None

        elif choice == '2':
            try:
                expected_time = float(input("Wanted break time (minutes): "))
                if expected_time <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if mode == 'break':
                print("You are already on a break!")
                continue
            mode = 'break'
            print("Break started.")
            start = time.time()
            wait_for_enter_with_countdown(expected_time * 60, label="Break left")
            end = time.time()
            break_times.append(end - start)
            print(f"Break recorded: {format_duration(end - start)}")
            mode = None

        elif choice == '3':
            total_work = sum(productive_times)
            total_break = sum(break_times)
            print("\n--- Summary ---")
            print(f"Total productive time: {format_duration(total_work)}")
            print(f"Total break time: {format_duration(total_break)}")
            print(f"Productive sessions: {len(productive_times)}")
            print(f"Break sessions: {len(break_times)}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()