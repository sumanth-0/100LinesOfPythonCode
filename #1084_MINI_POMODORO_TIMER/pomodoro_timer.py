#!/usr/bin/env python3
"""
Mini Pomodoro Timer CLI
A simple command-line Pomodoro timer to boost productivity.
"""

import time
import sys
import os
from datetime import datetime

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display the Pomodoro timer banner."""
    print("="*50)
    print("          🍅 MINI POMODORO TIMER 🍅          ")
    print("="*50)

def format_time(seconds):
    """Format seconds into MM:SS format."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"

def countdown(duration, session_type):
    """Run a countdown timer for the specified duration."""
    clear_screen()
    print_banner()
    print(f"\n{session_type} Session Started!")
    print(f"Duration: {format_time(duration)}\n")
    
    start_time = time.time()
    end_time = start_time + duration
    
    try:
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            sys.stdout.write(f"\r⏱️  Time Remaining: {format_time(remaining)}")
            sys.stdout.flush()
            time.sleep(1)
        
        print(f"\n\n✅ {session_type} Session Complete!")
        print("\a")  # System beep
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Timer interrupted by user.")
        sys.exit(0)

def get_user_choice():
    """Get user's menu choice."""
    print("\n1. Start Pomodoro (25 minutes)")
    print("2. Start Short Break (5 minutes)")
    print("3. Start Long Break (15 minutes)")
    print("4. Custom Timer")
    print("5. Exit")
    
    choice = input("\nSelect an option (1-5): ").strip()
    return choice

def custom_timer():
    """Allow user to set a custom timer duration."""
    while True:
        try:
            minutes = int(input("\nEnter duration in minutes (1-60): "))
            if 1 <= minutes <= 60:
                return minutes * 60
            else:
                print("Please enter a value between 1 and 60.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the Pomodoro timer."""
    session_count = 0
    
    while True:
        clear_screen()
        print_banner()
        print(f"\nCompleted Sessions: {session_count}")
        print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
        
        choice = get_user_choice()
        
        if choice == '1':
            countdown(25 * 60, "Pomodoro")
            session_count += 1
            input("\nPress Enter to continue...")
        elif choice == '2':
            countdown(5 * 60, "Short Break")
            input("\nPress Enter to continue...")
        elif choice == '3':
            countdown(15 * 60, "Long Break")
            input("\nPress Enter to continue...")
        elif choice == '4':
            duration = custom_timer()
            countdown(duration, "Custom")
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("\nThank you for using Pomodoro Timer! Stay productive! 🚀")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please select 1-5.")
            time.sleep(2)

if __name__ == "__main__":
    main()
