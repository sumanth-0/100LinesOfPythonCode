import random
import time
from typing import List, Tuple

class WordScrambleGame:
    """A word scramble game where players unscramble words to score points."""
    
    def __init__(self):
        """Initialize the game with a word list and game statistics."""
        self.words = [
            "python", "programming", "computer", "algorithm", "function",
            "variable", "database", "network", "software", "hardware",
            "interface", "development", "debugging", "repository", "framework",
            "library", "syntax", "compiler", "interpreter", "execution"
        ]
        self.score = 0
        self.attempts = 0
        self.correct_answers = 0
        self.start_time = None
        
    def scramble_word(self, word: str) -> str:
        """Scramble a word by shuffling its letters."""
        word_list = list(word)
        random.shuffle(word_list)
        scrambled = ''.join(word_list)
        # Ensure the scrambled word is different from the original
        while scrambled == word and len(word) > 1:
            random.shuffle(word_list)
            scrambled = ''.join(word_list)
        return scrambled
    
    def display_welcome(self):
        """Display welcome message and game instructions."""
        print("\n" + "="*50)
        print("   WELCOME TO WORD SCRAMBLE GAME!")
        print("="*50)
        print("\nInstructions:")
        print("- Unscramble the letters to form the correct word")
        print("- Type your answer and press Enter")
        print("- Type 'hint' for a hint (costs 5 points)")
        print("- Type 'skip' to skip the current word")
        print("- Type 'quit' to end the game\n")
        
    def get_hint(self, word: str) -> str:
        """Provide a hint by revealing the first letter of the word."""
        return f"Hint: The word starts with '{word[0].upper()}'"
    
    def play_round(self, word: str) -> bool:
        """Play a single round of the game."""
        scrambled = self.scramble_word(word)
        print(f"\nScrambled word: {scrambled.upper()}")
        print(f"Word length: {len(word)} letters")
        
        hint_used = False
        
        while True:
            user_input = input("Your answer: ").lower().strip()
            
            if user_input == 'quit':
                return False
            
            elif user_input == 'skip':
                print(f"Skipped! The correct word was: {word.upper()}")
                self.attempts += 1
                return True
            
            elif user_input == 'hint':
                if not hint_used:
                    print(self.get_hint(word))
                    self.score = max(0, self.score - 5)
                    hint_used = True
                else:
                    print("You already used a hint for this word!")
            
            elif user_input == word:
                points = 10 if not hint_used else 5
                self.score += points
                self.correct_answers += 1
                self.attempts += 1
                print(f"\n✓ Correct! You earned {points} points!")
                print(f"Current score: {self.score}")
                return True
            
            else:
                print("✗ Incorrect! Try again.")
    
    def display_statistics(self):
        """Display game statistics at the end."""
        elapsed_time = time.time() - self.start_time
        accuracy = (self.correct_answers / self.attempts * 100) if self.attempts > 0 else 0
        
        print("\n" + "="*50)
        print("   GAME OVER - FINAL STATISTICS")
        print("="*50)
        print(f"Total Score: {self.score}")
        print(f"Words Attempted: {self.attempts}")
        print(f"Correct Answers: {self.correct_answers}")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"Time Played: {elapsed_time:.1f} seconds")
        print("\nThanks for playing!\n")
    
    def play(self):
        """Main game loop."""
        self.display_welcome()
        self.start_time = time.time()
        
        # Shuffle words for random order
        game_words = self.words.copy()
        random.shuffle(game_words)
        
        for word in game_words:
            if not self.play_round(word):
                break
        
        self.display_statistics()

def main():
    """Entry point for the word scramble game."""
    game = WordScrambleGame()
    game.play()

if __name__ == "__main__":
    main()
