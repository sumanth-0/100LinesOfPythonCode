"""
🎮 Hangman Game with ASCII Art (Moderate Difficulty)
Author: Dhruv Lad
A terminal-based hangman game with a large random word list.
"""
import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# 🧩 Expanded word list (60+ words, moderate difficulty) you can use your own words
WORDS = [
    "python", "algorithm", "variable", "function", "recursion", "encryption", "database", "compiler", "binary", "syntax", "debugging","parameter", "interface", "developer","gravity", "molecule", "quantum", "neutron", "photosynthesis", "volcano", "microscope","eclipse", "relativity", "evolution", "telescope", "bacteria", "planet", "asteroid","matrix", "inception", "avatar", "interstellar", "titanic", "terminator", "gladiator","joker", "avengers", "parasite", "scarface", "godfather", "elephant", "kangaroo","dolphin", "rhinoceros", "penguin", "flamingo", "armadillo", "tortoise", "porcupine","hippopotamus", "alligator", "sahara", "antarctica", "amazon", "everest", "bermuda","pacific", "himalayas", "iceland", "caribbean"
]

def get_word():
    """Return a random word from the list."""
    return random.choice(WORDS).upper()

def display(word, guessed):
    """Display current word progress."""
    return ' '.join([ch if ch in guessed else '_' for ch in word])

def main():
    word = get_word()
    guessed, wrong = [], 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("🎯 Welcome to Hangman! Guess the word.")
    while wrong < max_attempts:
        print(HANGMAN_PICS[wrong])
        print("Word:", display(word, guessed))
        print("Guessed letters:", ' '.join(sorted(guessed)) or "None")

        guess = input("Enter a letter: ").upper()
        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabet letter.")
            continue
        if guess in guessed:
            print("⚠️ Already guessed that letter!")
            continue

        guessed.append(guess)
        if guess not in word:
            wrong += 1
            print("❌ Wrong guess!")
        else:
            print("✅ Good guess!")

        if all(ch in guessed for ch in word):
            print(f"\n🎉 You won! The word was {word}.")
            break
    else:
        print(HANGMAN_PICS[-1])
        print(f"\n💀 You lost! The word was {word}.")

if __name__ == "__main__":
    main()
