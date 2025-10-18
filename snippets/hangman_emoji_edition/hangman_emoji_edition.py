import random
import string

# Emoji representations for hangman stages
HANGMAN_STAGES = [
    "😊",  # 0 wrong guesses
    "😐",  # 1 wrong guess
    "😟",  # 2 wrong guesses
    "😰",  # 3 wrong guesses
    "😱",  # 4 wrong guesses
    "💀"   # 5 wrong guesses - game over
]

# Word categories with emoji themes
WORD_CATEGORIES = {
    "🍎 Fruits": ["apple", "banana", "orange", "grape", "mango", "peach", "cherry"],
    "🐶 Animals": ["elephant", "giraffe", "dolphin", "penguin", "tiger", "rabbit"],
    "🌍 Countries": ["america", "france", "japan", "brazil", "india", "egypt"],
    "🎮 Gaming": ["minecraft", "fortnite", "pokemon", "zelda", "mario", "sonic"]
}

def display_hangman(wrong_guesses):
    """Display hangman emoji based on wrong guesses"""
    stage = min(wrong_guesses, len(HANGMAN_STAGES) - 1)
    print(f"\n{HANGMAN_STAGES[stage]} Status: {wrong_guesses}/5 wrong guesses")

def display_word(word, guessed_letters):
    """Display word with guessed letters and blanks"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_category_choice():
    """Let player choose a category"""
    print("\n🎯 Choose a category:")
    categories = list(WORD_CATEGORIES.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("\nEnter category number (1-4): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print("❌ Invalid choice. Try again!")
        except ValueError:
            print("❌ Please enter a number!")

def play_hangman():
    """Main game function"""
    print("🎪 Welcome to Hangman - Emoji Edition! 🎪")
    print("Guess the word letter by letter!")
    
    # Choose category and word
    category = get_category_choice()
    word = random.choice(WORD_CATEGORIES[category]).lower()
    
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 5
    
    print(f"\n✨ Category: {category}")
    print(f"Word length: {len(word)} letters")
    
    while wrong_guesses < max_wrong:
        display_hangman(wrong_guesses)
        print(f"\n{display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
        
        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You won! 🎉")
            print(f"The word was: {word}")
            return True
        
        # Get guess
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"✅ Great! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌ Sorry! '{guess}' is not in the word.")
    
    # Game over
    display_hangman(wrong_guesses)
    print(f"\n💀 Game Over! The word was: {word}")
    return False

if __name__ == "__main__":
    play_hangman()
    
    while True:
        play_again = input("\n🔄 Play again? (yes/no): ").lower()
        if play_again == "yes":
            print("\n" + "="*50)
            play_hangman()
        else:
            print("\n👋 Thanks for playing! Goodbye!")
            break
