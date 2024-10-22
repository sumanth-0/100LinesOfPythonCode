import random

def choose_word():
    return random.choice(["hangman", "python", "programming", "development", "challenge", "function", "variable", "algorithm"])

def display_hangman(tries):
    stages = [""" 
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  / \\
                   |
                """,
                """ 
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  /
                   |
                """,
                """ 
                   -----
                   |   |
                   |   O
                   |  /|
                   |  /
                   |
                """,
                """ 
                   -----
                   |   |
                   |   O
                   |   |
                   |  /
                   |
                """,
                """ 
                   -----
                   |   |
                   |   O
                   |
                   |
                   |
                """,
                """ 
                   -----
                   |   |
                   |
                   |
                   |
                   |
                """
    ]
    return stages[tries]

def play_game():
    word = choose_word()
    guessed_letters, guessed_words, tries = [], [], 6
    word_completion = "_" * len(word)
    
    while tries > 0 and "_" in word_completion:
        print(display_hangman(tries))
        print(word_completion)
        guess = input("Guess a letter or word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
        else:
            print("Invalid guess.")
    
    print("Congratulations!" if "_" not in word_completion else f"Sorry, the word was: {word}")

if __name__ == "__main__":
    play_game()
