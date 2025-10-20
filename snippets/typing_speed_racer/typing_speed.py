import time
import random

# Sample texts for typing test
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog near the riverbank.",
    "Python programming is an excellent skill to learn for any developer.",
    "Artificial intelligence is transforming the way we live and work today.",
    "Practice makes perfect when it comes to improving your typing speed.",
    "The journey of a thousand miles begins with a single step forward.",
    "Success is not final failure is not fatal it is courage that counts.",
    "Technology continues to evolve at an unprecedented rate every year.",
    "Learning new skills requires dedication patience and consistent effort."
]

def select_text():
    """Select a random text sample"""
    return random.choice(SAMPLE_TEXTS)

def calculate_wpm(text, time_taken):
    """Calculate Words Per Minute"""
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes if minutes > 0 else 0
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage"""
    if not original or not typed:
        return 0
    
    original_chars = list(original)
    typed_chars = list(typed)
    
    correct = 0
    total = max(len(original_chars), len(typed_chars))
    
    for i in range(min(len(original_chars), len(typed_chars))):
        if original_chars[i] == typed_chars[i]:
            correct += 1
    
    accuracy = (correct / total) * 100 if total > 0 else 0
    return round(accuracy, 2)

def display_text(text):
    """Display the text to type"""
    print("\n" + "="*70)
    print("TYPE THE FOLLOWING TEXT:")
    print("="*70)
    print(f"\n{text}")
    print("\n" + "="*70)

def get_rating(wpm, accuracy):
    """Get performance rating based on WPM and accuracy"""
    if wpm >= 70 and accuracy >= 95:
        return "🌟 Expert! Outstanding performance!"
    elif wpm >= 50 and accuracy >= 90:
        return "🎖️ Advanced! Great typing skills!"
    elif wpm >= 30 and accuracy >= 80:
        return "💪 Intermediate! Keep practicing!"
    elif wpm >= 15 and accuracy >= 70:
        return "👶 Beginner! You're making progress!"
    else:
        return "🚀 Keep trying! Practice makes perfect!"

def display_results(wpm, accuracy, time_taken, original, typed):
    """Display test results"""
    print("\n" + "="*70)
    print("     🏁 TEST RESULTS 🏁")
    print("="*70)
    print(f"\n⏱️  Time taken: {time_taken:.2f} seconds")
    print(f"⚡ Typing speed: {wpm} WPM")
    print(f"🎯 Accuracy: {accuracy}%")
    print(f"\n{get_rating(wpm, accuracy)}")
    
    # Show errors if any
    if typed != original:
        print("\n" + "-"*70)
        print("❌ MISTAKES FOUND:")
        print(f"Original: {original}")
        print(f"You typed: {typed}")
    
    print("="*70)

def run_test():
    """Run a typing speed test"""
    print("\n" + "🎮"*35)
    print("     🔥 TYPING SPEED RACER 🔥")
    print("🎮"*35)
    
    text = select_text()
    display_text(text)
    
    input("\nPress ENTER when you're ready to start...")
    print("\n🚦 GO! Start typing NOW!\n")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm = calculate_wpm(text, time_taken)
    accuracy = calculate_accuracy(text, user_input)
    
    display_results(wpm, accuracy, time_taken, text, user_input)

def main():
    """Main program loop"""
    while True:
        run_test()
        
        play_again = input("\n🔄 Try again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for using Typing Speed Racer!")
            print("Keep practicing to improve your speed and accuracy!")
            break

if __name__ == "__main__":
    main()
