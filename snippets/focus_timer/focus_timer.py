#!/usr/bin/env python3
"""
Pomodoro Focus Timer - Issue #771
A simple command-line Pomodoro timer to boost productivity.
"""

import time
import sys
import os

# Timer durations (in seconds)
FOCUS_TIME = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60  # 5 minutes
LONG_BREAK = 15 * 60  # 15 minutes

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    """Convert seconds to MM:SS format."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"

def play_sound():
    """Play a beep sound when timer completes."""
    print('\a')  # Terminal bell sound

def countdown(duration, session_type):
    """Run the countdown timer with live display."""
    clear_screen()
    start_time = time.time()
    end_time = start_time + duration
    
    try:
        while time.time() < end_time:
            remaining = end_time - time.time()
            if remaining < 0:
                remaining = 0
            
            # Display timer
            sys.stdout.write(f'\r{session_type}: {format_time(remaining)} ')
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Timer completed
        sys.stdout.write(f'\r{session_type}: 00:00 - Complete!\n')
        play_sound()
        
    except KeyboardInterrupt:
        print("\n\nTimer paused. Press Enter to continue or Ctrl+C to quit.")
        try:
            input()
            # Resume timer with remaining time
            remaining_time = end_time - time.time()
            if remaining_time > 0:
                countdown(remaining_time, session_type)
        except KeyboardInterrupt:
            print("\nTimer stopped by user.")
            sys.exit(0)

def run_pomodoro(cycles=4):
    """Run multiple Pomodoro cycles."""
    print("🍅 Pomodoro Focus Timer Started!")
    print(f"Running {cycles} focus sessions...\n")
    
    for cycle in range(1, cycles + 1):
        print(f"\n--- Cycle {cycle}/{cycles} ---")
        input("Press Enter to start focus session...")
        
        # Focus session
        countdown(FOCUS_TIME, "Focus Time")
        
        # Break time
        if cycle < cycles:
            print("\nTime for a short break!")
            input("Press Enter to start break...")
            countdown(SHORT_BREAK, "Short Break")
        else:
            print("\nGreat work! Time for a long break!")
            input("Press Enter to start long break...")
            countdown(LONG_BREAK, "Long Break")
    
    print("\n🎉 All Pomodoro cycles completed! Great job!")

if __name__ == "__main__":
    try:
        # Get number of cycles from user or use default
        cycles = int(sys.argv[1]) if len(sys.argv) > 1 else 4
        run_pomodoro(cycles)
    except ValueError:
        print("Usage: python focus_timer.py [number_of_cycles]")
        sys.exit(1)
