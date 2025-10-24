"""
terminal_countdown.py
A simple terminal countdown timer with seconds and a completion message.
Usage:
    python terminal_countdown.py 10
"""

import time
import sys
import argparse

def countdown(seconds: int):
    """Display countdown timer in terminal."""
    try:
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\r⏳ Time left: {timer}", end="", flush=True)
            time.sleep(1)
        print("\r✅ Time’s up!                      ")
    except KeyboardInterrupt:
        print("\n⏹️ Countdown cancelled.")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Simple terminal countdown timer.")
    parser.add_argument("seconds", type=int, help="Countdown time in seconds")
    args = parser.parse_args()

    if args.seconds <= 0:
        print("Please enter a positive number of seconds.")
        sys.exit(1)

    print(f"Starting countdown for {args.seconds} seconds...")
    countdown(args.seconds)

if __name__ == "__main__":
    main()
