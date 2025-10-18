#!/usr/bin/env python3
"""
Word Guess with Hints - A word guessing game with synonym hints and first letter hints
Issue #1004 - 100 Lines of Python Code Challenge
"""

import random
import sys

# Word database with synonyms for hints
WORD_DATABASE = {
    "python": ["snake", "programming", "language", "code"],
    "computer": ["machine", "device", "system", "electronic"],
    "keyboard": ["input", "typing", "device", "keys"],
    "monitor": ["screen", "display", "visual", "output"],
    "algorithm": ["procedure", "method", "process", "formula"],
    "database": ["storage", "collection", "repository", "archive"],
    "network": ["connection", "internet", "web", "system"],
    "software": ["program", "application", "code", "system"],
    "hardware": ["equipment", "device", "machine", "physical"],
    "function": ["method", "procedure", "routine", "operation"],
    "variable": ["placeholder", "storage", "container", "element"],
    "debugging": ["fixing", "troubleshooting", "testing", "correcting"],
    "compiler": ["translator", "converter", "processor", "interpreter"],
    "memory": ["storage", "ram", "cache", "buffer"],
    "encryption": ["encoding", "security", "cipher", "protection"]
}

class WordGuessGame:
    def __init__(self):
        self.word = ""
        self.synonyms = []
        self.guesses_left = 7
        self.guessed_letters = set()
        self.hints_used = 0
        
    def select_random_word(self):
        """Select a random word from the database"""
        self.word = random.choice(list(WORD_DATABASE.keys()))
        self.synonyms = WORD_DATABASE[self.word]
        
    def display_word(self):
        """Display the word with guessed letters revealed"""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def get_synonym_hint(self):
        """Provide a synonym hint"""
        if self.synonyms:
            hint = self.synonyms[self.hints_used % len(self.synonyms)]
            self.hints_used += 1
            return hint
        return "No more synonyms available"
    
    def get_first_letter_hint(self):
        """Provide the first letter as a hint"""
        return self.word[0].upper()
    
    def is_word_guessed(self):
        """Check if the entire word has been guessed"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.lower()
        
        if letter in self.guessed_letters:
            return "already_guessed"
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            return "correct"
        else:
            self.guesses_left -= 1
            return "incorrect"
    
    def play(self):
        """Main game loop"""
        print("\n" + "="*50)
        print("   WORD GUESS WITH HINTS GAME")
        print("="*50)
        print("\nGuess the word letter by letter!")
        print("Type 'hint' for a synonym hint")
        print("Type 'first' for the first letter hint\n")
        
        self.select_random_word()
        
        while self.guesses_left > 0:
            print(f"\nWord: {self.display_word()}")
            print(f"Guesses left: {self.guesses_left}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
            
            if self.is_word_guessed():
                print(f"\n🎉 Congratulations! You guessed the word: {self.word.upper()}")
                print(f"Hints used: {self.hints_used}")
                return
            
            user_input = input("\nEnter a letter (or 'hint'/'first'): ").strip().lower()
            
            if user_input == "hint":
                hint = self.get_synonym_hint()
                print(f"💡 Synonym hint: {hint}")
                continue
            elif user_input == "first":
                print(f"💡 First letter hint: {self.get_first_letter_hint()}")
                continue
            elif len(user_input) != 1 or not user_input.isalpha():
                print("⚠️  Please enter a single letter!")
                continue
            
            result = self.make_guess(user_input)
            
            if result == "already_guessed":
                print("⚠️  You already guessed that letter!")
            elif result == "correct":
                print("✓ Correct!")
            else:
                print("✗ Wrong guess!")
        
        print(f"\n💀 Game Over! The word was: {self.word.upper()}")

if __name__ == "__main__":
    game = WordGuessGame()
    game.play()
    
    while True:
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again == 'y':
            game = WordGuessGame()
            game.play()
        else:
            print("Thanks for playing!")
            sys.exit(0)
