import random
import string

# Word bank with hints
WORD_BANK = {
    'python': 'A popular programming language named after a comedy group',
    'javascript': 'A scripting language commonly used for web development',
    'algorithm': 'A step-by-step procedure for solving a problem',
    'database': 'An organized collection of structured information',
    'function': 'A reusable block of code that performs a specific task',
    'variable': 'A container for storing data values',
    'programming': 'The process of creating a set of instructions for a computer',
    'computer': 'An electronic device for processing data',
    'keyboard': 'An input device with keys for typing',
    'software': 'Programs and operating information used by a computer',
    'hardware': 'The physical components of a computer system',
    'internet': 'A global network connecting millions of computers',
    'debugging': 'The process of finding and fixing errors in code',
    'compiler': 'A program that translates source code into machine code',
    'developer': 'A person who creates software applications'
}

class HangmanGame:
    def __init__(self):
        self.word = ''
        self.hint = ''
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect = 6
        self.hint_used = False
        
    def choose_word(self):
        """Randomly select a word from the word bank"""
        self.word, self.hint = random.choice(list(WORD_BANK.items()))
        return self.word
    
    def display_word(self):
        """Display the word with guessed letters revealed"""
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display.strip()
    
    def display_hangman(self):
        """Display the hangman ASCII art based on incorrect guesses"""
        stages = [
            """
               --------
               |      |
               |
               |
               |
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |
               |
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |      |
               |
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     /
               |
            --------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |
            --------
            """
        ]
        return stages[self.incorrect_guesses]
    
    def get_hint(self):
        """Provide a hint to the player"""
        if not self.hint_used:
            self.hint_used = True
            return f"\nHint: {self.hint}"
        return "\nYou've already used your hint!"
    
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.lower()
        
        if letter in self.guessed_letters:
            return "You already guessed that letter!"
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            return f"Good guess! '{letter}' is in the word."
        else:
            self.incorrect_guesses += 1
            return f"Sorry, '{letter}' is not in the word."
    
    def is_won(self):
        """Check if the player has won"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_lost(self):
        """Check if the player has lost"""
        return self.incorrect_guesses >= self.max_incorrect
    
    def play(self):
        """Main game loop"""
        print("\n" + "="*50)
        print("Welcome to Hangman with Hints!")
        print("="*50)
        
        self.choose_word()
        
        while True:
            print(self.display_hangman())
            print(f"\nWord: {self.display_word()}")
            print(f"Incorrect guesses remaining: {self.max_incorrect - self.incorrect_guesses}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
            
            choice = input("\nEnter a letter, 'hint' for a hint, or 'quit' to exit: ").lower().strip()
            
            if choice == 'quit':
                print(f"\nThanks for playing! The word was: {self.word}")
                break
            elif choice == 'hint':
                print(self.get_hint())
                continue
            elif len(choice) != 1 or choice not in string.ascii_lowercase:
                print("\nPlease enter a single letter!")
                continue
            
            result = self.make_guess(choice)
            print(f"\n{result}")
            
            if self.is_won():
                print(self.display_hangman())
                print(f"\nWord: {self.display_word()}")
                print("\n" + "="*50)
                print("Congratulations! You won!")
                print(f"The word was: {self.word}")
                print("="*50)
                break
            elif self.is_lost():
                print(self.display_hangman())
                print("\n" + "="*50)
                print("Game Over! You lost!")
                print(f"The word was: {self.word}")
                print("="*50)
                break

def main():
    """Main function to run the game"""
    while True:
        game = HangmanGame()
        game.play()
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Hangman with Hints!")
            break

if __name__ == "__main__":
    main()
