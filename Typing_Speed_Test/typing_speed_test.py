import time
import random
import string

# Expanded list of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile and powerful programming language.",
    "Coding is both an art and a science.",
    "Practice makes perfect when it comes to typing.",
    "The early bird catches the worm, but the second mouse gets the cheese.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Where there's a will, there's a way.",
    "A journey of a thousand miles begins with a single step.",
    "Knowledge is power, but enthusiasm pulls the switch."
]

def generate_sentence():
    """Generate a random sentence from the list."""
    return random.choice(sentences)

def calculate_wpm(start_time, end_time, typed_chars):
    """Calculate words per minute."""
    time_elapsed = end_time - start_time
    minutes = time_elapsed / 60
    # Assume average word length of 5 characters
    return int((typed_chars / 5) / minutes)

def calculate_accuracy(original, typed):
    """Calculate accuracy percentage."""
    original_chars = set(original)
    correct_chars = sum(1 for char in typed if char in original_chars)
    return (correct_chars / len(original)) * 100

def run_typing_test():
    """Main function to run the typing test."""
    print("Welcome to the Typing Speed Test!")
    print("Type the following sentence:")
    
    test_sentence = generate_sentence()
    print(test_sentence)
    
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    wpm = calculate_wpm(start_time, end_time, len(user_input))
    accuracy = calculate_accuracy(test_sentence, user_input)
    
    print(f"\nYour typing speed: {wpm} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    # Offer to retry
    retry = input("Would you like to try again? (y/n): ").lower()
    if retry == 'y':
        run_typing_test()

if __name__ == "__main__":
    run_typing_test()
