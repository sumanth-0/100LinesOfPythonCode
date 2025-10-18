import random
import time

# Word Guess Countdown Game
# A fun game where you guess a word with a countdown timer!

WORD_LIST = [
    'python', 'javascript', 'programming', 'computer', 'algorithm',
    'database', 'network', 'software', 'hardware', 'keyboard',
    'function', 'variable', 'string', 'integer', 'boolean',
    'developer', 'engineer', 'debugging', 'compilation', 'execution'
]

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_hint(word, guessed_letters):
    """Provide a hint by revealing a random unguessed letter."""
    unguessed = [letter for letter in word if letter not in guessed_letters]
    if unguessed:
        return random.choice(unguessed)
    return None

def play_game():
    """Main game logic for Word Guess Countdown."""
    print("\n" + "="*50)
    print("   WORD GUESS COUNTDOWN GAME")
    print("="*50)
    print("\nGuess the word before time runs out!")
    print("You have 60 seconds and 10 wrong guesses allowed.\n")
    
    # Select random word
    word = random.choice(WORD_LIST).lower()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 10
    time_limit = 60  # seconds
    start_time = time.time()
    hints_used = 0
    max_hints = 2
    
    while True:
        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = max(0, int(time_limit - elapsed_time))
        
        if remaining_time == 0:
            print("\n⏰ TIME'S UP! Game Over!")
            print(f"The word was: {word.upper()}")
            break
        
        # Display current game state
        print("\n" + "-"*50)
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Time remaining: {remaining_time}s | Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Hints available: {max_hints - hints_used}")
        
        # Check if word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print("\n" + "="*50)
            print("🎉 CONGRATULATIONS! You guessed the word!")
            print(f"Word: {word.upper()}")
            print(f"Time taken: {int(elapsed_time)} seconds")
            print(f"Wrong guesses: {wrong_guesses}")
            print("="*50)
            break
        
        # Check if too many wrong guesses
        if wrong_guesses >= max_wrong_guesses:
            print("\n❌ Too many wrong guesses! Game Over!")
            print(f"The word was: {word.upper()}")
            break
        
        # Get user input
        user_input = input("\nEnter a letter (or 'hint' for help, 'quit' to exit): ").lower().strip()
        
        if user_input == 'quit':
            print(f"\nThanks for playing! The word was: {word.upper()}")
            break
        
        if user_input == 'hint':
            if hints_used < max_hints:
                hint_letter = get_hint(word, guessed_letters)
                if hint_letter:
                    print(f"💡 Hint: The word contains the letter '{hint_letter.upper()}'")
                    hints_used += 1
            else:
                print("❌ No more hints available!")
            continue
        
        if len(user_input) != 1 or not user_input.isalpha():
            print("⚠️  Please enter a single letter!")
            continue
        
        if user_input in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        guessed_letters.add(user_input)
        
        if user_input in word:
            print(f"✅ Correct! '{user_input.upper()}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{user_input.upper()}' is not in the word.")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nPlay again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Word Guess Countdown! Goodbye! 👋")
            break
