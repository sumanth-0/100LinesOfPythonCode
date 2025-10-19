#!/usr/bin/env python3
"""
Eye Rest Notifier - A simple console-based reminder application
to help prevent eye strain by reminding users to take regular breaks.

Follows the 20-20-20 rule: Every 20 minutes, look at something 20 feet away
for at least 20 seconds to reduce eye strain.
"""

import time
import sys
from datetime import datetime
import os


class EyeRestNotifier:
    """A console-based eye rest reminder application."""
    
    def __init__(self, interval_minutes=20, rest_duration_seconds=20):
        """
        Initialize the Eye Rest Notifier.
        
        Args:
            interval_minutes: Time interval between reminders (default: 20)
            rest_duration_seconds: Suggested rest duration (default: 20)
        """
        self.interval = interval_minutes * 60  # Convert to seconds
        self.rest_duration = rest_duration_seconds
        self.running = True
        self.total_breaks = 0
        
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_banner(self):
        """Display the application banner."""
        print("="*60)
        print(" " * 15 + "EYE REST NOTIFIER")
        print("="*60)
        print(f"Interval: {self.interval//60} minutes")
        print(f"Rest Duration: {self.rest_duration} seconds")
        print(f"Total Breaks Completed: {self.total_breaks}")
        print("="*60)
        
    def countdown_timer(self, seconds, message):
        """Display a countdown timer."""
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\r{message} {timer}", end="", flush=True)
            time.sleep(1)
        print()  # New line after countdown
        
    def notify_user(self):
        """Send notification to take a break."""
        self.clear_screen()
        print("\n" + "*"*60)
        print(" " * 15 + "TIME FOR EYE REST!")
        print("*"*60)
        print("\n⏰ It's been 20 minutes! Time to rest your eyes.")
        print("\n👀 Follow the 20-20-20 rule:")
        print("   Look at something 20 feet away for 20 seconds")
        print("\n" + "-"*60)
        
        self.countdown_timer(self.rest_duration, "Rest time remaining:")
        
        print("\n✓ Great job! Your eyes thank you.")
        self.total_breaks += 1
        print("\nPress Enter to continue...")
        input()
        
    def run(self):
        """Main application loop."""
        try:
            self.clear_screen()
            self.display_banner()
            print("\n[Started at {}]".format(datetime.now().strftime("%H:%M:%S")))
            print("\nPress Ctrl+C to stop the notifier.\n")
            
            while self.running:
                next_break = datetime.now().timestamp() + self.interval
                
                # Wait until next break
                while datetime.now().timestamp() < next_break:
                    remaining = int(next_break - datetime.now().timestamp())
                    mins, secs = divmod(remaining, 60)
                    print(f"\rNext break in: {mins:02d}:{secs:02d}", end="", flush=True)
                    time.sleep(1)
                    
                print()  # New line
                self.notify_user()
                self.clear_screen()
                self.display_banner()
                
        except KeyboardInterrupt:
            self.stop()
            
    def stop(self):
        """Stop the notifier gracefully."""
        self.running = False
        print("\n\n" + "="*60)
        print(" " * 15 + "SESSION SUMMARY")
        print("="*60)
        print(f"Total breaks taken: {self.total_breaks}")
        print("Thank you for taking care of your eyes! 👋")
        print("="*60 + "\n")
        sys.exit(0)


def main():
    """Entry point for the application."""
    notifier = EyeRestNotifier(interval_minutes=20, rest_duration_seconds=20)
    notifier.run()


if __name__ == "__main__":
    main()
