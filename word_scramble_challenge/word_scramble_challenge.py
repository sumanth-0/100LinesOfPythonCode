#!/usr/bin/env python3
"""
Word Scramble Challenge Game

A fun and interactive game where players guess scrambled words.
Includes multiple difficulty levels, scoring system, and hints.

Author: Contributor
Date: October 2025
Issue: #1162
"""

import random
import time
import sys
from typing import List, Tuple, Dict


class WordScrambleGame:
    """
    Main game class for Word Scramble Challenge.
    """

    def __init__(self):
        """Initialize the game with word lists and settings."""
        self.easy_words = [
            "python", "coding", "program", "computer", "keyboard",
            "mouse", "screen", "laptop", "software", "hardware",
            "internet", "website", "browser", "email", "password"
        ]
        
        self.medium_words = [
            "algorithm", "database", "framework", "debugging",
            "compiler", "variable", "function", "interface",
            "encryption", "developer", "repository", "deployment",
            "middleware", "bandwidth", "firewall"
        ]
        
        self.hard_words = [
            "polymorphism", "encapsulation", "abstraction",
            "inheritance", "synchronization", "serialization",
            "authentication", "authorization", "concatenation",
            "instantiation", "implementation", "architecture",
            "configuration", "optimization", "virtualization"
        ]
        
        self.score = 0
        self.attempts = 0
        self.hints_used = 0
        self.difficulty = "easy"

    def scramble_word(self, word: str) -> str:
        """
        Scramble the letters of a word.
        
        Args:
            word: The word to scramble
            
        Returns:
            Scrambled version of the word
        """
        word_list = list(word)
        scrambled = word_list.copy()
        
        # Ensure scrambled word is different from original
        while ''.join(scrambled) == word and len(word) > 1:
            random.shuffle(scrambled)
        
        return ''.join(scrambled)

    def get_hint(self, word: str, revealed_positions: List[int]) -> str:
        """
        Generate a hint by revealing one more letter.
        
        Args:
            word: The original word
            revealed_positions: Already revealed letter positions
            
        Returns:
            Hint string with revealed letters
        """
        hint = ['_'] * len(word)
        
        for pos in revealed_positions:
            hint[pos] = word[pos]
        
        # Reveal one more letter
        unrevealed = [i for i in range(len(word)) if i not in revealed_positions]
        if unrevealed:
            new_pos = random.choice(unrevealed)
            revealed_positions.append(new_pos)
            hint[new_pos] = word[new_pos]
        
        return ' '.join(hint)

    def select_difficulty(self) -> None:
        """
        Allow player to select game difficulty.
        """
        print("\n" + "="*50)
        print("SELECT DIFFICULTY LEVEL")
        print("="*50)
        print("1. Easy (5-8 letter words)")
        print("2. Medium (8-10 letter words)")
        print("3. Hard (10+ letter words)")
        print("="*50)
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice == "1":
                self.difficulty = "easy"
                break
            elif choice == "2":
                self.difficulty = "medium"
                break
            elif choice == "3":
                self.difficulty = "hard"
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    def get_word_list(self) -> List[str]:
        """
        Get word list based on difficulty.
        
        Returns:
            List of words for current difficulty
        """
        if self.difficulty == "easy":
            return self.easy_words
        elif self.difficulty == "medium":
            return self.medium_words
        else:
            return self.hard_words

    def play_round(self) -> bool:
        """
        Play one round of the game.
        
        Returns:
            True if player wants to continue, False otherwise
        """
        word_list = self.get_word_list()
        word = random.choice(word_list)
        scrambled = self.scramble_word(word)
        revealed_positions = []
        
        print("\n" + "="*50)
        print(f"ROUND {self.attempts + 1}")
        print("="*50)
        print(f"Scrambled word: {scrambled.upper()}")
        print(f"Word length: {len(word)} letters")
        print("\nCommands: 'hint' for a clue, 'skip' to skip, 'quit' to exit")
        print("="*50)
        
        max_guesses = 3
        guesses = 0
        
        while guesses < max_guesses:
            guess = input("\nYour guess: ").lower().strip()
            
            if guess == "quit":
                return False
            elif guess == "skip":
                print(f"\nThe word was: {word.upper()}")
                self.attempts += 1
                return True
            elif guess == "hint":
                if self.hints_used < 3:
                    hint = self.get_hint(word, revealed_positions)
                    print(f"\nHint: {hint}")
                    self.hints_used += 1
                else:
                    print("\nNo more hints available!")
                continue
            
            guesses += 1
            
            if guess == word:
                points = (max_guesses - guesses + 1) * 10
                if self.difficulty == "medium":
                    points *= 2
                elif self.difficulty == "hard":
                    points *= 3
                
                self.score += points
                print(f"\n🎉 Correct! You earned {points} points!")
                print(f"Total score: {self.score}")
                self.attempts += 1
                return True
            else:
                remaining = max_guesses - guesses
                if remaining > 0:
                    print(f"\n❌ Wrong! {remaining} guess(es) remaining.")
                else:
                    print(f"\n❌ Out of guesses! The word was: {word.upper()}")
        
        self.attempts += 1
        return True

    def display_stats(self) -> None:
        """
        Display final game statistics.
        """
        print("\n" + "="*50)
        print("GAME STATISTICS")
        print("="*50)
        print(f"Total Score: {self.score}")
        print(f"Words Attempted: {self.attempts}")
        print(f"Hints Used: {self.hints_used}")
        print(f"Difficulty: {self.difficulty.upper()}")
        print("="*50)

    def run(self) -> None:
        """
        Main game loop.
        """
        print("\n" + "*"*50)
        print("    WORD SCRAMBLE CHALLENGE    ")
        print("*"*50)
        print("\nWelcome! Unscramble words to earn points.")
        print("Correct guesses earn more points with fewer attempts!")
        
        self.select_difficulty()
        
        while True:
            if not self.play_round():
                break
            
            continue_game = input("\nPlay another round? (yes/no): ").lower()
            if continue_game not in ['yes', 'y']:
                break
        
        self.display_stats()
        print("\nThanks for playing! 🎮\n")


def main():
    """
    Entry point for the game.
    """
    game = WordScrambleGame()
    game.run()


if __name__ == "__main__":
    main()
