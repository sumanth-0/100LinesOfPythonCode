"""
Word Jumble Solver
Author: Diya Satish Kumar
A fun Python game that challenges players to unscramble jumbled words.
"""

import random

def get_jumbled_word(word):
    return ''.join(random.sample(word, len(word)))

def play_game():
    words = ["python", "developer", "keyboard", "coding", "challenge", "programming"]
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