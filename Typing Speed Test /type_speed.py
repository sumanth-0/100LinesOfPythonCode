import random
import time

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The only thing we have to fear is fear itself."
]

def generate_sentence():
    """Randomly selects a sentence from the list."""
    return random.choice(sentences)

def calculate_wpm(start_time, end_time, words):
    """Calculates the words per minute."""
    time_taken = end_time - start_time  # Time in seconds
    minutes = time_taken / 60  # Convert to minutes
    wpm = words / minutes if minutes > 0 else 0  # Words per minute
    return wpm

def typing_test():
    print("Welcome to the Typing Speed Test!")
    sentence = generate_sentence()
    print(f"\nType the following sentence as fast as you can:\n\n\"{sentence}\"\n")

    input("Press Enter when you are ready to start...")

    start_time = time.time()  # Record the start time
    user_input = input("Start typing: ")
    end_time = time.time()  # Record the end time

    # Count the number of words typed
    words_typed = len(user_input.split())
    wpm = calculate_wpm(start_time, end_time, words_typed)

    print(f"\nYou typed {words_typed} words in {end_time - start_time:.2f} seconds.")
    print(f"Your typing speed is {wpm:.2f} words per minute.")

if __name__ == "__main__":
    typing_test()
