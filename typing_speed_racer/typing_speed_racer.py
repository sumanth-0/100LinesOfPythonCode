#!/usr/bin/env python3
"""
Typing Speed Racer - A Competitive Typing Speed Game

This program calculates the user's typing speed in Words Per Minute (WPM)
and accuracy by comparing the typed text to a sample text. It includes
performance ratings and error detection to help users improve their typing skills.

Features:
- Multiple sample texts of varying difficulty
- Real-time WPM calculation
- Accuracy percentage tracking
- Performance rating system
- Detailed error analysis
- Competitive scoring system

Author: Created for issue #1161
Date: October 18, 2025
"""

import time
import random
from difflib import SequenceMatcher

# Sample texts for typing practice
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet.",
    "Python is a high-level programming language that emphasizes code readability and simplicity.",
    "Practice makes perfect. The more you type, the faster and more accurate you will become over time.",
    "Competitive typing requires focus, speed, and precision. Master all three to become a typing champion.",
    "In the digital age, efficient typing skills are essential for productivity and communication excellence."
]

def calculate_wpm(text_length, time_taken):
    """
    Calculate Words Per Minute (WPM) based on characters typed.
    Standard: 5 characters = 1 word
    
    Args:
        text_length (int): Number of characters typed
        time_taken (float): Time taken in seconds
    
    Returns:
        float: Words per minute
    """
    if time_taken == 0:
        return 0
    words = text_length / 5  # Standard: 5 characters = 1 word
    minutes = time_taken / 60
    return round(words / minutes, 2)

def calculate_accuracy(original, typed):
    """
    Calculate typing accuracy as a percentage.
    
    Args:
        original (str): The original sample text
        typed (str): The text typed by the user
    
    Returns:
        float: Accuracy percentage
    """
    if len(original) == 0:
        return 0
    
    matcher = SequenceMatcher(None, original, typed)
    similarity = matcher.ratio()
    return round(similarity * 100, 2)

def get_performance_rating(wpm, accuracy):
    """
    Determine performance rating based on WPM and accuracy.
    
    Args:
        wpm (float): Words per minute
        accuracy (float): Accuracy percentage
    
    Returns:
        str: Performance rating
    """
    if wpm >= 60 and accuracy >= 95:
        return "🏆 EXPERT - Outstanding performance!"
    elif wpm >= 45 and accuracy >= 90:
        return "⭐ ADVANCED - Excellent typing skills!"
    elif wpm >= 30 and accuracy >= 85:
        return "✓ INTERMEDIATE - Good progress!"
    elif wpm >= 15 and accuracy >= 75:
        return "📚 BEGINNER - Keep practicing!"
    else:
        return "🎯 NOVICE - Practice makes perfect!"

def analyze_errors(original, typed):
    """
    Analyze and count typing errors.
    
    Args:
        original (str): The original sample text
        typed (str): The text typed by the user
    
    Returns:
        tuple: (total_errors, error_details)
    """
    errors = 0
    error_details = []
    
    min_len = min(len(original), len(typed))
    
    for i in range(min_len):
        if original[i] != typed[i]:
            errors += 1
            if errors <= 5:  # Show first 5 errors only
                error_details.append(f"Position {i+1}: Expected '{original[i]}', got '{typed[i]}'")
    
    # Count extra or missing characters
    if len(typed) < len(original):
        errors += len(original) - len(typed)
        error_details.append(f"Missing {len(original) - len(typed)} characters")
    elif len(typed) > len(original):
        errors += len(typed) - len(original)
        error_details.append(f"Extra {len(typed) - len(original)} characters typed")
    
    return errors, error_details

def display_results(sample_text, typed_text, time_taken):
    """
    Display comprehensive typing test results.
    
    Args:
        sample_text (str): The original sample text
        typed_text (str): The text typed by the user
        time_taken (float): Time taken in seconds
    """
    print("\n" + "="*70)
    print("                    🏁 TYPING SPEED RACER - RESULTS 🏁")
    print("="*70)
    
    wpm = calculate_wpm(len(typed_text), time_taken)
    accuracy = calculate_accuracy(sample_text, typed_text)
    errors, error_details = analyze_errors(sample_text, typed_text)
    
    print(f"\n⏱️  Time Taken: {time_taken:.2f} seconds")
    print(f"🚀 Typing Speed: {wpm} WPM")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"❌ Total Errors: {errors}")
    
    if error_details:
        print("\n📋 Error Analysis:")
        for detail in error_details:
            print(f"   - {detail}")
    
    print(f"\n{get_performance_rating(wpm, accuracy)}")
    print("="*70)

def main():
    """
    Main function to run the Typing Speed Racer game.
    """
    print("\n" + "="*70)
    print("        🏁 WELCOME TO TYPING SPEED RACER! 🏁")
    print("="*70)
    print("\nTest your typing speed and accuracy!")
    print("Type the displayed text as quickly and accurately as possible.")
    print("="*70)
    
    while True:
        # Select a random sample text
        sample_text = random.choice(SAMPLE_TEXTS)
        
        print("\n📝 Sample Text:")
        print(f"\n{sample_text}\n")
        print("-"*70)
        
        input("Press ENTER when you're ready to start typing...")
        
        print("\n🏁 START TYPING NOW!\n")
        
        # Start timer
        start_time = time.time()
        
        # Get user input
        typed_text = input(">>> ")
        
        # End timer
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Display results
        display_results(sample_text, typed_text, time_taken)
        
        # Ask if user wants to continue
        print("\nWant to race again? (y/n): ", end="")
        choice = input().lower()
        
        if choice != 'y':
            print("\n🏆 Thanks for playing Typing Speed Racer!")
            print("Keep practicing to improve your speed and accuracy!\n")
            break
        
        print("\n" + "="*70)

if __name__ == "__main__":
    main()
