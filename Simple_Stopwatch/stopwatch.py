import time

def stopwatch():
    """A simple stopwatch program to start, stop, and reset time."""
    print("Simple Stopwatch")
    print("Commands:")
    print("  'start' - Start the stopwatch")
    print("  'stop'  - Stop the stopwatch")
    print("  'reset' - Reset the stopwatch")
    print("  'exit'  - Exit the program")

    running = False
    start_time = 0
    elapsed_time = 0

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "start":
            if not running:
                start_time = time.time() - elapsed_time
                running = True
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")

        elif command == "stop":
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch stopped at {elapsed_time:.2f} seconds.")
            else:
                print("Stopwatch is not running.")

        elif command == "reset":
            elapsed_time = 0
            if running:
                start_time = time.time()
            print("Stopwatch reset.")

        elif command == "exit":
            print("Exiting the stopwatch.")
            break

        else:
            print("Invalid command. Please try again.")

        if running:
            current_time = time.time() - start_time
            print(f"Elapsed time: {current_time:.2f} seconds", end='\r')

if __name__ == "__main__":
    stopwatch()
