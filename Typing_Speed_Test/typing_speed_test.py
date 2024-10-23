import time
import random
import string

# Expanded list of sample sentences and short paragraphs
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile and powerful programming language.",
    "Coding is both an art and a science.",
    "Practice makes perfect when it comes to typing.",
    "The early bird catches the worm, but the second mouse gets the cheese.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Where there's a will, there's a way.",
    "A journey of a thousand miles begins with a single step.",
    "Knowledge is power, but enthusiasm pulls the switch.",
    "The sun was setting behind the mountains, painting the sky in vibrant hues of orange and pink. A gentle breeze rustled through the trees, carrying the sweet scent of blooming flowers. It was a perfect evening for a leisurely stroll through the park.",
    "In the bustling city, people hurried along the sidewalks, their footsteps echoing off the tall buildings. Cars honked in the distance, and the aroma of fresh coffee wafted from nearby cafes. Despite the chaos, there was an undeniable energy that pulsed through the streets.",
    "The old bookstore stood at the corner, its windows dusty and shelves overflowing with forgotten tales. As you stepped inside, the musty smell of aged paper enveloped you. Each book held a world waiting to be explored, a silent invitation to embark on countless adventures.",
]

def generate_text():
    """Generate a random text from the list."""
    return random.choice(texts)

def calculate_wpm(start_time, end_time, typed_chars):
    """Calculate words per minute."""
    time_elapsed = end_time - start_time
    minutes = time_elapsed / 60
    # Assume average word length of 5 characters
    return int((typed_chars / 5) / minutes)

def calculate_accuracy(original, typed):
    """Calculate accuracy percentage."""
    min_length = min(len(original), len(typed))
    correct_chars = sum(1 for o, t in zip(original[:min_length], typed[:min_length]) if o == t)
    return (correct_chars / len(original)) * 100

def run_typing_test():
    """Main function to run the typing test."""
    print("Welcome to the Typing Speed Test!")
    print("Type the following text:")
    
    test_text = generate_text()
    print(test_text)
    print("\nPress Enter when you're ready to start...")
    input()
    
    print("Start typing now:")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    wpm = calculate_wpm(start_time, end_time, len(user_input))
    accuracy = calculate_accuracy(test_text, user_input)
    
    print(f"\nYour typing speed: {wpm} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    # Offer to retry
    retry = input("Would you like to try again? (y/n): ").lower()
    if retry == 'y':
        run_typing_test()

if __name__ == "__main__":
    run_typing_test()
