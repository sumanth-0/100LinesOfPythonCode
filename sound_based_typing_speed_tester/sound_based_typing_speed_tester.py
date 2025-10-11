#!/usr/bin/env python3
"""
Sound-Based Typing Speed Tester
A typing speed test that plays sounds for each keypress or checkpoint.
"""
import time
import random
import sys
from threading import Thread

# Try importing pygame for sound, fallback to basic beep
try:
    import pygame
    pygame.mixer.init()
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("Note: pygame not available. Using system beep instead.")

def beep():
    """Play a sound or beep."""
    if SOUND_AVAILABLE:
        try:
            sound = pygame.mixer.Sound(buffer=bytes([i % 256 for i in range(1000)]))
            sound.play()
        except:
            print('\a', end='', flush=True)
    else:
        print('\a', end='', flush=True)

def get_sample_text():
    """Return a random sample text for typing."""
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "Practice makes perfect when learning to type.",
        "Speed and accuracy are both important skills.",
        "Typing fast requires good technique and focus."
    ]
    return random.choice(texts)

def calculate_wpm(text, elapsed_time):
    """Calculate words per minute."""
    words = len(text.split())
    minutes = elapsed_time / 60
    return round(words / minutes if minutes > 0 else 0, 2)

def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage."""
    if not original:
        return 0
    correct = sum(1 for o, t in zip(original, typed) if o == t)
    return round((correct / len(original)) * 100, 2)

def typing_test():
    """Main typing test function."""
    print("\n" + "="*60)
    print("  SOUND-BASED TYPING SPEED TESTER")
    print("="*60)
    print("\nInstructions:")
    print("- Type the text shown below as fast and accurately as you can")
    print("- A sound will play for each keypress")
    print("- Press Enter when done\n")
    
    sample_text = get_sample_text()
    print(f"Text to type:\n{sample_text}\n")
    
    input("Press Enter when ready to start...")
    print("\nStart typing NOW!\n")
    
    start_time = time.time()
    
    # Get user input with sound feedback
    typed_text = ""
    try:
        if sys.platform == "win32":
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    char = msvcrt.getch().decode('utf-8', errors='ignore')
                    if char == '\r':  # Enter key
                        break
                    typed_text += char
                    beep()
                    print(char, end='', flush=True)
        else:
            typed_text = input()
            for _ in typed_text:
                beep()
    except KeyboardInterrupt:
        print("\n\nTest interrupted!")
        return
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    # Calculate results
    wpm = calculate_wpm(typed_text, elapsed)
    accuracy = calculate_accuracy(sample_text, typed_text)
    
    # Display results
    print("\n\n" + "="*60)
    print("  RESULTS")
    print("="*60)
    print(f"Time taken: {elapsed:.2f} seconds")
    print(f"Words per minute (WPM): {wpm}")
    print(f"Accuracy: {accuracy}%")
    print(f"Characters typed: {len(typed_text)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    typing_test()
