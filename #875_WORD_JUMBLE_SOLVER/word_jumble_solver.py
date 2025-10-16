"""
Word Jumble Solver
Author: Diya Satish Kumar
A fun Python game that challenges players to unscramble jumbled words.
Now loads words from an external text file.
"""

import random

def load_words(filename):
    """Reads words from a text file (one word per line)."""
    try:
        with open(filename, "r") as file:
            # Strip spaces and remove empty lines
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("⚠️ No words found in the file.")
            exit()
        return words
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        exit()

def get_jumbled_word(word):
    """Returns a shuffled version of the given word."""
    return ''.join(random.sample(word, len(word)))

def play_game():
    words = load_words("words.txt")  # ← reads from your text file
    score = 0

    print("🔤 Welcome to the Word Jumble Game!")
    print("Unscramble the letters to form a valid word.\nType 'quit' to exit.\n")

    while True:
        word = random.choice(words)
        jumbled = get_jumbled_word(word)
        print(f"Jumbled word: {jumbled}")

        guess = input("Your guess: ").lower()
        if guess == "quit":
            print(f"\n🏁 Final Score: {score}")
            break
        elif guess == word:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct word was '{word}'.\n")

if __name__ == "__main__":
    play_game()
