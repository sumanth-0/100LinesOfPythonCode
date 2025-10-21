import random

# Word categories with emoji clues
WORD_CATEGORIES = {
    '✈️': ['airplane', 'airport', 'flight', 'pilot', 'travel'],
    '🍔': ['burger', 'pizza', 'sandwich', 'hotdog', 'fries'],
    '⚽': ['soccer', 'football', 'basketball', 'tennis', 'volleyball'],
    '🐾': ['dog', 'cat', 'rabbit', 'hamster', 'parrot'],
    '🎬': ['movie', 'cinema', 'actor', 'director', 'film'],
    '🎵': ['guitar', 'piano', 'drums', 'violin', 'trumpet'],
    '📚': ['book', 'library', 'reading', 'author', 'novel']
}

# Hangman stages using emojis
HANGMAN_STAGES = [
    '😀',  # Happy - 0 mistakes
    '🙂',  # Slightly smiling - 1 mistake
    '😐',  # Neutral - 2 mistakes
    '😟',  # Worried - 3 mistakes
    '😬',  # Grimacing - 4 mistakes
    '😱',  # Scared - 5 mistakes
    '😵'   # Dead - 6 mistakes (game over)
]

def select_word():
    """Select a random word and return it with its emoji clue"""
    emoji, words = random.choice(list(WORD_CATEGORIES.items()))
    word = random.choice(words)
    return word.upper(), emoji

def display_game_state(word, guessed_letters, mistakes):
    """Display the current state of the game"""
    print("\n" + "="*50)
    print(f"Hangman Status: {HANGMAN_STAGES[mistakes]}")
    print(f"Mistakes: {mistakes}/6")
    
    # Display the word with guessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"\nWord: {display}")
    print(f"\nGuessed letters: {', '.join(sorted(guessed_letters))}")
    print("="*50)

def get_guess(guessed_letters):
    """Get a valid guess from the player"""
    while True:
        guess = input("\nGuess a letter: ").upper()
        
        if len(guess) != 1:
            print("❌ Please enter a single letter!")
        elif not guess.isalpha():
            print("❌ Please enter a valid letter!")
        elif guess in guessed_letters:
            print("❌ You already guessed that letter!")
        else:
            return guess

def play_game():
    """Main game logic"""
    word, emoji_clue = select_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6
    
    print("\n" + "⭐"*20)
    print("HANGMAN - EMOJI EDITION")
    print("⭐"*20)
    print(f"\n🎯 Category Clue: {emoji_clue}")
    print(f"The word has {len(word)} letters.")
    
    while mistakes < max_mistakes:
        display_game_state(word, guessed_letters, mistakes)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"\n✅ Correct! '{guess}' is in the word!")
            
            # Check if word is complete
            if all(letter in guessed_letters for letter in word):
                print("\n" + "🎉"*20)
                print(f"🏆 CONGRATULATIONS! You won!")
                print(f"The word was: {word}")
                print("🎉"*20)
                return True
        else:
            mistakes += 1
            print(f"\n❌ Wrong! '{guess}' is not in the word.")
    
    # Game over
    print("\n" + "💀"*20)
    print(f"{HANGMAN_STAGES[mistakes]} GAME OVER!")
    print(f"The word was: {word}")
    print("💀"*20)
    return False

def main():
    """Main program loop"""
    while True:
        play_game()
        
        play_again = input("\n🎮 Play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing Hangman - Emoji Edition!")
            break

if __name__ == "__main__":
    main()
