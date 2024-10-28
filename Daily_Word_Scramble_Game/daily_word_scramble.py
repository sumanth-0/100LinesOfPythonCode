import random

class WordScrambleGame:
    """Class to manage the word scramble game."""
    def __init__(self, words):
        self.words = words
        self.current_word = ""
        self.scrambled_word = ""
        self.hints = {
            "apple": "A fruit that keeps the doctor away.",
            "banana": "A yellow fruit that monkeys love.",
            "grape": "Small round fruit, often in bunches.",
            "orange": "A citrus fruit that is round and orange.",
            "lemon": "A sour yellow fruit often used in drinks."
        }
        self.streak = 0

    def choose_word(self):
        """Select a random word and scramble it."""
        self.current_word = random.choice(self.words)
        self.scrambled_word = ''.join(random.sample(self.current_word, len(self.current_word)))

    def get_hint(self):
        """Provide a hint for the current word."""
        return self.hints.get(self.current_word, "No hint available.")

    def check_guess(self, guess):
        """Check if the user's guess is correct."""
        if guess.lower() == self.current_word:
            self.streak += 1
            return True
        else:
            self.streak = 0
            return False


def main():
    """Run the daily word scramble game."""
    words = ["apple", "banana", "grape", "orange", "lemon"]
    game = WordScrambleGame(words)

    print("Welcome to the Daily Word Scramble Game!\n")
    
    while True:
        game.choose_word()
        print(f"Scrambled Word: {game.scrambled_word}")
        print(f"Hint: {game.get_hint()}")
        
        guess = input("Your guess (or type 'exit' to quit): ")
        if guess.lower() == 'exit':
            break

        if game.check_guess(guess):
            print("Correct! Well done!")
            print(f"Current Streak: {game.streak}\n")
        else:
            print(f"Incorrect! The correct word was '{game.current_word}'.")
            print(f"Current Streak Reset to: {game.streak}\n")


if __name__ == "__main__":
    main()
