import random

# List of words to choose from
word_list = [
    "hangman", "python", "programming",
    "development", "challenge", "function",
    "variable", "algorithm"
]

def choose_word():
    """Choose a random word from the word list."""
    return random.choice(word_list)

def display_hangman(tries):
    """Display the hangman based on the number of incorrect tries."""
    stages = [  # Final state: head, torso, both arms, and both legs
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        # Head, torso, both arms
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        # Head, torso, one arm
        """
           -----
           |   |
           |   O
           |  /|
           |  /
           |
        """,
        # Head, torso
        """
           -----
           |   |
           |   O
           |   |
           |  /
           |
        """,
        # Head
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        # Initial state
        """
           -----
           |   |
           |
           |
           |
           |
        """
    ]
    # Ensure tries is within the range of stages
    return stages[max(0, min(tries, len(stages) - 1))]

def play_game():
    """Play the Hangman game."""
    print("Welcome to Hangman!")
    word = choose_word()
    word_completion = "_" * len(word)  # Display underscores for each letter
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  # Number of incorrect tries allowed

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():  # Guessing a letter
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)

                # Update the word completion
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # Guessing a whole word
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess. Please try again.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Sorry, you've run out of tries. The word was: {word}")

if __name__ == "__main__":
    play_game()
