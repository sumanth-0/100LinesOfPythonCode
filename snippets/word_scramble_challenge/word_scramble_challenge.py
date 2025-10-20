#!/usr/bin/env python3
"""
Word Scramble Challenge Game
A fun word guessing game where players unscramble words within a time limit.
"""

import random
import time
import sys

# Word categories with words
WORD_CATEGORIES = {
    "animals": [
        "elephant", "giraffe", "penguin", "kangaroo", "dolphin",
        "butterfly", "octopus", "leopard", "flamingo", "cheetah"
    ],
    "countries": [
        "australia", "brazil", "canada", "denmark", "egypt",
        "france", "germany", "india", "japan", "mexico"
    ],
    "fruits": [
        "strawberry", "pineapple", "watermelon", "blueberry", "raspberry",
        "mango", "banana", "orange", "apple", "grape"
    ],
    "technology": [
        "computer", "keyboard", "monitor", "software", "internet",
        "database", "algorithm", "program", "network", "hardware"
    ]
}

class WordScrambleGame:
    """Main game class for Word Scramble Challenge"""
    
    def __init__(self):
        self.score = 0
        self.rounds_played = 0
        self.correct_answers = 0
        
    def scramble_word(self, word):
        """Scramble the letters of a word"""
        word_list = list(word)
        scrambled = word_list[:]
        
        # Keep scrambling until it's different from original
        while ''.join(scrambled) == word:
            random.shuffle(scrambled)
        
        return ''.join(scrambled)
    
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("\n" + "="*50)
        print("  WORD SCRAMBLE CHALLENGE")
        print("="*50)
        print("\nWelcome to the Word Scramble Challenge!")
        print("\nInstructions:")
        print("- Unscramble the word within the time limit")
        print("- Each correct answer earns you 10 points")
        print("- Type 'hint' for a hint (costs 3 points)")
        print("- Type 'skip' to skip the current word")
        print("- Type 'quit' to exit the game")
        print("="*50 + "\n")
    
    def get_hint(self, word):
        """Provide a hint by revealing first and last letter"""
        if len(word) <= 2:
            return f"Hint: {word[0]}..."
        return f"Hint: {word[0]}...{word[-1]}"
    
    def play_round(self, category, word):
        """Play a single round of the game"""
        scrambled = self.scramble_word(word)
        self.rounds_played += 1
        
        print(f"\nRound {self.rounds_played}")
        print(f"Category: {category.upper()}")
        print(f"Scrambled word: {scrambled.upper()}")
        print(f"Word length: {len(word)} letters")
        
        start_time = time.time()
        time_limit = 30  # 30 seconds per word
        
        while True:
            remaining_time = int(time_limit - (time.time() - start_time))
            
            if remaining_time <= 0:
                print(f"\n⏰ Time's up! The correct word was: {word.upper()}")
                return False
            
            print(f"\nTime remaining: {remaining_time}s")
            guess = input("Your answer: ").strip().lower()
            
            if guess == "quit":
                return "quit"
            elif guess == "skip":
                print(f"\nSkipped! The correct word was: {word.upper()}")
                return False
            elif guess == "hint":
                if self.score >= 3:
                    self.score -= 3
                    print(f"\n💡 {self.get_hint(word)}")
                    print(f"Score: {self.score}")
                else:
                    print("\n❌ Not enough points for a hint!")
            elif guess == word:
                self.score += 10
                self.correct_answers += 1
                print("\n✅ Correct! +10 points")
                print(f"Score: {self.score}")
                return True
            else:
                print("\n❌ Incorrect! Try again.")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        # Ask for number of rounds
        while True:
            try:
                num_rounds = input("How many rounds would you like to play? (1-20): ")
                num_rounds = int(num_rounds)
                if 1 <= num_rounds <= 20:
                    break
                print("Please enter a number between 1 and 20.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Play the specified number of rounds
        for _ in range(num_rounds):
            category = random.choice(list(WORD_CATEGORIES.keys()))
            word = random.choice(WORD_CATEGORIES[category])
            
            result = self.play_round(category, word)
            
            if result == "quit":
                break
            
            time.sleep(1)  # Brief pause between rounds
        
        # Display final results
        print("\n" + "="*50)
        print("  GAME OVER")
        print("="*50)
        print(f"\nRounds played: {self.rounds_played}")
        print(f"Correct answers: {self.correct_answers}")
        print(f"Final score: {self.score}")
        
        if self.rounds_played > 0:
            accuracy = (self.correct_answers / self.rounds_played) * 100
            print(f"Accuracy: {accuracy:.1f}%")
        
        print("\nThanks for playing Word Scramble Challenge!")
        print("="*50 + "\n")

def main():
    """Entry point for the game"""
    game = WordScrambleGame()
    game.play_game()

if __name__ == "__main__":
    main()
