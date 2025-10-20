#!/usr/bin/env python3
"""
Memory Card Pairs Game
A terminal-based card matching game where players flip cards to find matching pairs.
Tracks the number of turns taken to complete the game.
"""

import random
import os
import time


class MemoryCardGame:
    """Memory Card Pairs game with turn tracking."""
    
    def __init__(self, pairs=8):
        """Initialize the game with the specified number of pairs.
        
        Args:
            pairs: Number of card pairs (default: 8)
        """
        self.pairs = pairs
        self.total_cards = pairs * 2
        self.cards = self._create_deck()
        self.revealed = [False] * self.total_cards
        self.matched = [False] * self.total_cards
        self.turns = 0
        self.attempts = 0
        
    def _create_deck(self):
        """Create and shuffle a deck of card pairs.
        
        Returns:
            List of shuffled cards
        """
        symbols = ['🎮', '🎯', '🎨', '🎭', '🎪', '🎸', '🎺', '🎻', 
                   '🏀', '⚽', '🎾', '🏈', '⚾', '🎳', '🏐', '🏓']
        deck = symbols[:self.pairs] * 2
        random.shuffle(deck)
        return deck
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_board(self, first_pick=None, second_pick=None):
        """Display the current state of the game board.
        
        Args:
            first_pick: Index of first picked card (optional)
            second_pick: Index of second picked card (optional)
        """
        print("\n" + "="*50)
        print("   MEMORY CARD PAIRS GAME")
        print("="*50)
        print(f"Turns: {self.turns} | Attempts: {self.attempts}")
        print("="*50 + "\n")
        
        # Display cards in a grid
        cols = 4
        for i in range(0, self.total_cards, cols):
            # Display card numbers
            row_nums = ""
            for j in range(i, min(i + cols, self.total_cards)):
                row_nums += f" {j+1:2d}  "
            print(row_nums)
            
            # Display card content
            row_cards = ""
            for j in range(i, min(i + cols, self.total_cards)):
                if self.matched[j]:
                    row_cards += "  ✓  "  # Matched pair
                elif j == first_pick or j == second_pick:
                    row_cards += f" {self.cards[j]}  "  # Temporarily revealed
                elif self.revealed[j]:
                    row_cards += f" {self.cards[j]}  "  # Revealed
                else:
                    row_cards += " [?] "  # Hidden
            print(row_cards)
            print()
    
    def get_valid_input(self, prompt, exclude=None):
        """Get valid card selection from user.
        
        Args:
            prompt: Input prompt message
            exclude: List of indices to exclude from selection
            
        Returns:
            Valid card index (0-based)
        """
        exclude = exclude or []
        while True:
            try:
                choice = input(prompt)
                if choice.lower() == 'quit':
                    return None
                    
                idx = int(choice) - 1
                
                if idx < 0 or idx >= self.total_cards:
                    print(f"Please enter a number between 1 and {self.total_cards}")
                elif self.matched[idx]:
                    print("This card is already matched. Choose another.")
                elif idx in exclude:
                    print("You already picked this card. Choose a different one.")
                else:
                    return idx
            except ValueError:
                print("Invalid input. Please enter a number or 'quit' to exit.")
    
    def play_turn(self):
        """Play a single turn (flip two cards).
        
        Returns:
            True if game continues, False if game ends
        """
        self.display_board()
        
        # First card selection
        print("\nSelect the first card:")
        first_idx = self.get_valid_input("Enter card number (or 'quit' to exit): ")
        if first_idx is None:
            return False
        
        self.display_board(first_pick=first_idx)
        
        # Second card selection
        print(f"\nYou selected: {self.cards[first_idx]}")
        print("Select the second card:")
        second_idx = self.get_valid_input("Enter card number: ", exclude=[first_idx])
        if second_idx is None:
            return False
        
        self.display_board(first_pick=first_idx, second_pick=second_idx)
        self.attempts += 1
        
        # Check for match
        print(f"\nYou selected: {self.cards[first_idx]} and {self.cards[second_idx]}")
        
        if self.cards[first_idx] == self.cards[second_idx]:
            print("🎉 It's a match!")
            self.matched[first_idx] = True
            self.matched[second_idx] = True
        else:
            print("❌ No match. Try again!")
        
        self.turns += 1
        time.sleep(2)
        
        return True
    
    def is_game_complete(self):
        """Check if all pairs have been matched.
        
        Returns:
            True if game is complete, False otherwise
        """
        return all(self.matched)
    
    def play(self):
        """Main game loop."""
        print("\n" + "="*50)
        print("   WELCOME TO MEMORY CARD PAIRS!")
        print("="*50)
        print("\nMatch all pairs of cards to win!")
        print("Type 'quit' at any time to exit.\n")
        input("Press Enter to start...")
        
        while True:
            self.clear_screen()
            
            if not self.play_turn():
                print("\nThanks for playing! Goodbye!")
                break
            
            if self.is_game_complete():
                self.clear_screen()
                self.display_board()
                print("\n" + "="*50)
                print("   🎊 CONGRATULATIONS! YOU WON! 🎊")
                print("="*50)
                print(f"\nYou completed the game in {self.turns} turns!")
                print(f"Total attempts: {self.attempts}")
                print("\nThanks for playing!\n")
                break


def main():
    """Main entry point for the game."""
    game = MemoryCardGame(pairs=8)
    game.play()


if __name__ == "__main__":
    main()
