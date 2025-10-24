import random

# Words list
WORDS = ["python", "hangman", "developer", "challenge", "keyboard", "computer"]

HANGMAN = [
"""
  +---+
      |
      |
      |
     ===""",
"""
  +---+
  O   |
      |
      |
     ===""",
"""
  +---+
  O   |
  |   |
      |
     ===""",
"""
  +---+
  O   |
 /|   |
      |
     ===""",
"""
  +---+
  O   |
 /|\\  |
      |
     ===""",
"""
  +---+
  O   |
 /|\\  |
 /    |
     ===""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ==="""
]

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0
    print("Welcome to Hangman!")
    while wrong < len(HANGMAN)-1:
        display = "".join([c if c in guessed else "_" for c in word])
        print(HANGMAN[wrong])
        print("Word:", " ".join(display))
        if "_" not in display:
            print("🎉 You Won!")
            return
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            guessed.add(guess)
        else:
            guessed.add(guess)
            wrong += 1
    print(HANGMAN[wrong])
    print("💀 You Lost! The word was:", word)

if __name__ == "__main__":
    play()
