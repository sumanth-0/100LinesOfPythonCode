#!/usr/bin/env python3
"""
Typing Speed Racer - A Competitive Typing Speed Game

This game tests your typing speed and accuracy by presenting random text prompts.
You compete against yourself to improve your WPM (Words Per Minute) and accuracy.

Features:
- Multiple difficulty levels
- Real-time WPM calculation
- Accuracy tracking
- Personal best records
- Colorful terminal interface
- Timer and countdown

Author: Typing Speed Racer Game
Issue: #1161
"""

import time
import random
import sys
from datetime import datetime

# ANSI color codes for terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Sample text prompts for different difficulty levels
EASY_PROMPTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello world! Welcome to typing speed racer.",
    "Practice makes perfect in typing skills.",
    "Type fast and accurately to win the race.",
    "Speed is good but accuracy is better."
]

MEDIUM_PROMPTS = [
    "The art of programming is the art of organizing complexity.",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
    "First solve the problem. Then write the code.",
    "Code is like humor. When you have to explain it, it's bad.",
    "Simplicity is the soul of efficiency in programming."
]

HARD_PROMPTS = [
    "In the beginning, there was nothing. Then came the programmers, and they said: 'Let there be code!' And there was code, and it was good, though occasionally buggy.",
    "The best error message is the one that never shows up. The second best is the one that clearly explains what went wrong and how to fix it.",
    "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.",
    "Walking on water and developing software from a specification are easy if both are frozen.",
    "The most disastrous thing that you can ever learn is your first programming language."
]

def clear_screen():
    """Clear the terminal screen."""
    print('\033[2J\033[H', end='')

def print_banner():
    """Print the game banner."""
    banner = f"""{Colors.HEADER}{Colors.BOLD}
    ╔══════════════════════════════════════════╗
    ║      TYPING SPEED RACER - v1.0          ║
    ║      Test Your Typing Skills!           ║
    ╚══════════════════════════════════════════╝
    {Colors.ENDC}"""
    print(banner)

def calculate_wpm(text_length, time_taken):
    """Calculate Words Per Minute."""
    if time_taken <= 0:
        return 0
    words = text_length / 5  # Standard: 5 characters = 1 word
    minutes = time_taken / 60
    return round(words / minutes, 2)

def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage."""
    if not original:
        return 0
    correct_chars = sum(1 for i, char in enumerate(typed) if i < len(original) and char == original[i])
    accuracy = (correct_chars / len(original)) * 100
    return round(accuracy, 2)

def get_difficulty():
    """Get difficulty level from user."""
    print(f"\n{Colors.OKCYAN}Select Difficulty Level:{Colors.ENDC}")
    print(f"  {Colors.OKGREEN}1.{Colors.ENDC} Easy (Short sentences)")
    print(f"  {Colors.WARNING}2.{Colors.ENDC} Medium (Programming quotes)")
    print(f"  {Colors.FAIL}3.{Colors.ENDC} Hard (Long paragraphs)")
    
    while True:
        try:
            choice = input(f"\n{Colors.BOLD}Enter your choice (1-3): {Colors.ENDC}")
            if choice in ['1', '2', '3']:
                return int(choice)
            print(f"{Colors.FAIL}Invalid choice! Please enter 1, 2, or 3.{Colors.ENDC}")
        except (ValueError, KeyboardInterrupt):
            print(f"\n{Colors.FAIL}Invalid input! Please try again.{Colors.ENDC}")

def play_game(difficulty):
    """Main game logic."""
    # Select text based on difficulty
    if difficulty == 1:
        text = random.choice(EASY_PROMPTS)
    elif difficulty == 2:
        text = random.choice(MEDIUM_PROMPTS)
    else:
        text = random.choice(HARD_PROMPTS)
    
    print(f"\n{Colors.OKBLUE}{Colors.BOLD}Type the following text:{Colors.ENDC}\n")
    print(f"{Colors.HEADER}{text}{Colors.ENDC}\n")
    print(f"{Colors.WARNING}Press ENTER when ready to start...{Colors.ENDC}")
    input()
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}GO! Start typing now!{Colors.ENDC}\n")
    
    # Start timer
    start_time = time.time()
    
    try:
        typed_text = input(f"{Colors.OKCYAN}>>> {Colors.ENDC}")
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}Game interrupted!{Colors.ENDC}")
        return None
    
    # End timer
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Calculate results
    wpm = calculate_wpm(len(text), time_taken)
    accuracy = calculate_accuracy(text, typed_text)
    
    return {
        'wpm': wpm,
        'accuracy': accuracy,
        'time': round(time_taken, 2),
        'text_length': len(text),
        'difficulty': ['Easy', 'Medium', 'Hard'][difficulty - 1]
    }

def display_results(results):
    """Display game results."""
    if results is None:
        return
    
    print(f"\n{Colors.BOLD}{'='*50}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}RACE RESULTS{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*50}{Colors.ENDC}\n")
    
    print(f"  {Colors.OKCYAN}Difficulty:{Colors.ENDC} {results['difficulty']}")
    print(f"  {Colors.OKCYAN}Time Taken:{Colors.ENDC} {results['time']} seconds")
    print(f"  {Colors.OKCYAN}Text Length:{Colors.ENDC} {results['text_length']} characters")
    
    # WPM with color coding
    wpm_color = Colors.OKGREEN if results['wpm'] >= 40 else Colors.WARNING if results['wpm'] >= 20 else Colors.FAIL
    print(f"  {Colors.OKCYAN}Typing Speed:{Colors.ENDC} {wpm_color}{Colors.BOLD}{results['wpm']} WPM{Colors.ENDC}")
    
    # Accuracy with color coding
    acc_color = Colors.OKGREEN if results['accuracy'] >= 90 else Colors.WARNING if results['accuracy'] >= 70 else Colors.FAIL
    print(f"  {Colors.OKCYAN}Accuracy:{Colors.ENDC} {acc_color}{Colors.BOLD}{results['accuracy']}%{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}{'='*50}{Colors.ENDC}")
    
    # Performance feedback
    if results['wpm'] >= 60 and results['accuracy'] >= 95:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🏆 CHAMPION! Outstanding performance!{Colors.ENDC}")
    elif results['wpm'] >= 40 and results['accuracy'] >= 90:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}⭐ EXCELLENT! Keep up the great work!{Colors.ENDC}")
    elif results['wpm'] >= 20 and results['accuracy'] >= 70:
        print(f"\n{Colors.WARNING}{Colors.BOLD}👍 GOOD! You're making progress!{Colors.ENDC}")
    else:
        print(f"\n{Colors.OKCYAN}{Colors.BOLD}💪 Keep practicing! You'll improve!{Colors.ENDC}")

def main():
    """Main function to run the game."""
    try:
        while True:
            clear_screen()
            print_banner()
            
            difficulty = get_difficulty()
            results = play_game(difficulty)
            display_results(results)
            
            # Ask to play again
            print(f"\n{Colors.OKCYAN}Do you want to race again? (y/n): {Colors.ENDC}", end='')
            choice = input().lower()
            
            if choice != 'y':
                print(f"\n{Colors.OKGREEN}{Colors.BOLD}Thanks for playing! Keep practicing!{Colors.ENDC}")
                print(f"{Colors.HEADER}See you next time, Speed Racer! 🏎️{Colors.ENDC}\n")
                break
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Game terminated by user.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}An error occurred: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
