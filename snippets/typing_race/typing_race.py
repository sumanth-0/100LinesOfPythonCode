import time
import random

def get_sample_texts():
    """Return a list of sample texts for typing practice."""
    return [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level programming language with dynamic semantics.",
        "Practice makes perfect when it comes to typing speed.",
        "Consistency is the key to improving your typing skills.",
        "Focus on accuracy first, then speed will naturally follow.",
        "The best time to plant a tree was twenty years ago. The second best time is now.",
        "Life is what happens when you're busy making other plans.",
        "In the middle of difficulty lies opportunity.",
        "The only way to do great work is to love what you do.",
        "Innovation distinguishes between a leader and a follower."
    ]

def calculate_wpm(text_length, time_taken):
    """Calculate words per minute based on characters typed and time taken."""
    words = text_length / 5  # Standard: 5 characters = 1 word
    minutes = time_taken / 60
    return round(words / minutes, 2) if minutes > 0 else 0

def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage."""
    if not original:
        return 0
    correct = sum(1 for o, t in zip(original, typed) if o == t)
    return round((correct / len(original)) * 100, 2)

def display_results(wpm, accuracy, time_taken):
    """Display the typing test results."""
    print("\n" + "="*50)
    print("TYPING TEST RESULTS")
    print("="*50)
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")
    print("="*50)
    
    if wpm >= 60 and accuracy >= 95:
        print("🏆 Excellent! You're a typing master!")
    elif wpm >= 40 and accuracy >= 85:
        print("👍 Great job! Keep practicing!")
    elif wpm >= 25:
        print("💪 Good effort! You're improving!")
    else:
        print("📚 Keep practicing to improve your speed!")

def typing_race():
    """Main function to run the typing race game."""
    print("\n" + "*"*50)
    print("WELCOME TO TYPING RACE!")
    print("*"*50)
    print("\nInstructions:")
    print("1. A random text will be displayed")
    print("2. Type it as quickly and accurately as possible")
    print("3. Press Enter when done")
    print("\nPress Enter to start...")
    input()
    
    # Select random text
    texts = get_sample_texts()
    target_text = random.choice(texts)
    
    print("\n" + "-"*50)
    print("TYPE THIS:")
    print("-"*50)
    print(target_text)
    print("-"*50)
    print("\nStart typing now!\n")
    
    # Start timing
    start_time = time.time()
    user_input = input(">>> ")
    end_time = time.time()
    
    # Calculate results
    time_taken = end_time - start_time
    wpm = calculate_wpm(len(user_input), time_taken)
    accuracy = calculate_accuracy(target_text, user_input)
    
    # Display results
    display_results(wpm, accuracy, time_taken)
    
    # Ask to play again
    print("\nWould you like to try again? (y/n): ", end="")
    if input().lower() == 'y':
        typing_race()

if __name__ == "__main__":
    typing_race()
