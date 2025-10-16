import random

# 1. ASCII stages for the hangman (7 stages for 6 guesses)
STAGES = [
    """
       -----
       |   |
           |
           |
           |
         ---
    """,
    """
       -----
       |   |
       O   |
           |
           |
         ---
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
         ---
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
         ---
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
         ---
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
         ---
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
         ---
    """
]

# 2. Word list
WORDS = ["python", "hacktoberfest", "terminal", "coding", "challenge", "hangman"]

def start_game():
    """Initializes and runs the Hangman game loop."""
    # Select a random word and set up game variables
    word_to_guess = random.choice(WORDS).lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = len(STAGES) - 1
    
    # 3. Game Loop
    while incorrect_guesses < max_incorrect:
        # Generate the current masked word (e.g., P _ T H _ N)
        display_word = "".join([
            letter if letter in guessed_letters else "_ " 
            for letter in word_to_guess
        ])

        # Check for Win Condition
        if "_ " not in display_word:
            print("\n" + display_word)
            print("\n🎉 CONGRATULATIONS! You guessed the word!")
            print(STAGES[incorrect_guesses])
            return

        # Display Game State
        print("\n" + "=" * 30)
        print(STAGES[incorrect_guesses])
        print(f"Word: {display_word}")
        print(f"Incorrect Guesses Left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed Letters: {sorted(list(guessed_letters))}")
        print("=" * 30)

        # 4. User Input and Validation
        guess = input("Guess a letter: ").lower().strip()

        # Input Validation
        if not guess.isalpha() or len(guess) != 1:
            print(" Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f" You already guessed the letter '{guess}'.")
            continue

        guessed_letters.add(guess)

        # Check Guess
        if guess in word_to_guess:
            print(f" Correct! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f" Incorrect. The letter '{guess}' is NOT in the word.")

    # 5. Lose Condition
    print("\n" + "=" * 30)
    print(STAGES[max_incorrect])
    print(" GAME OVER! The man is hanged.")
    print(f"The word was: {word_to_guess}")
    print("=" * 30)

if __name__ == "__main__":
    start_game()