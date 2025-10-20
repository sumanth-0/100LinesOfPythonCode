#!/usr/bin/env python3
"""
Emoji Memory Match Game
A fun memory card matching game with emojis!

How to play:
- Match pairs of emoji cards
- Remember the positions of emojis
- Clear the board to win!
"""

import random
import time
import os
import sys

class EmojiMemoryGame:
    def __init__(self, grid_size=4):
        """
        Initialize the emoji memory match game.
        
        Args:
            grid_size (int): Size of the grid (grid_size x grid_size)
        """
        self.grid_size = grid_size
        self.total_pairs = (grid_size * grid_size) // 2
        
        # Collection of emojis to use in the game
        self.emoji_pool = [
            '🎮', '🎯', '🎨', '🎭', '🎪', '🎸', '🎺', '🎻',
            '⚽', '🏀', '🏈', '⚾', '🎾', '🏐', '🏉', '🎱',
            '🍎', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍒',
            '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼',
            '🌸', '🌺', '🌻', '🌹', '🌷', '🌼', '💐', '🏵️',
            '⭐', '✨', '💫', '🌟', '🔥', '💧', '⚡', '❄️'
        ]
        
        self.board = []
        self.revealed = []
        self.matched = []
        self.attempts = 0
        self.matches_found = 0
        self.start_time = None
        
        self.initialize_board()
    
    def initialize_board(self):
        """Create and shuffle the game board."""
        # Select random emojis for pairs
        selected_emojis = random.sample(self.emoji_pool, self.total_pairs)
        
        # Create pairs
        cards = selected_emojis * 2
        
        # Shuffle the cards
        random.shuffle(cards)
        
        # Create the grid
        self.board = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                index = i * self.grid_size + j
                row.append(cards[index])
            self.board.append(row)
        
        # Initialize revealed and matched grids
        self.revealed = [[False] * self.grid_size for _ in range(self.grid_size)]
        self.matched = [[False] * self.grid_size for _ in range(self.grid_size)]
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_board(self, show_positions=None):
        """Display the current game board."""
        self.clear_screen()
        print("\n" + "="*50)
        print("   🎮 EMOJI MEMORY MATCH GAME 🎮")
        print("="*50 + "\n")
        
        print(f"Attempts: {self.attempts} | Matches: {self.matches_found}/{self.total_pairs}")
        print("\n   ", end="")
        
        # Print column numbers
        for j in range(self.grid_size):
            print(f"  {j}  ", end="")
        print("\n")
        
        # Print the board
        for i in range(self.grid_size):
            print(f" {i} ", end="")
            for j in range(self.grid_size):
                if self.matched[i][j]:
                    print("  ✓  ", end="")
                elif show_positions and (i, j) in show_positions:
                    print(f" {self.board[i][j]}  ", end="")
                elif self.revealed[i][j]:
                    print(f" {self.board[i][j]}  ", end="")
                else:
                    print("  ?  ", end="")
            print()
        print()
    
    def get_valid_position(self, prompt):
        """Get a valid position from the user."""
        while True:
            try:
                position = input(prompt).strip()
                if position.lower() == 'quit':
                    return None
                
                row, col = map(int, position.split())
                
                if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                    if not self.matched[row][col] and not self.revealed[row][col]:
                        return (row, col)
                    else:
                        print("That card is already matched or revealed. Try again.")
                else:
                    print(f"Invalid position. Use row and column (0-{self.grid_size-1}).")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column separated by space (e.g., '0 1').")
    
    def play(self):
        """Main game loop."""
        print("\n" + "="*50)
        print("   Welcome to Emoji Memory Match!")
        print("="*50)
        print(f"\nGrid Size: {self.grid_size}x{self.grid_size}")
        print(f"Total Pairs to Match: {self.total_pairs}")
        print("\nInstructions:")
        print("- Enter row and column numbers separated by space (e.g., '0 1')")
        print("- Match all emoji pairs to win!")
        print("- Type 'quit' to exit the game.")
        input("\nPress Enter to start...")
        
        self.start_time = time.time()
        
        while self.matches_found < self.total_pairs:
            self.display_board()
            
            # Get first card
            print("Select first card:")
            pos1 = self.get_valid_position("Enter position (row col): ")
            if pos1 is None:
                print("\nGame ended. Thanks for playing!")
                return
            
            # Show first card
            self.display_board([pos1])
            
            # Get second card
            print("Select second card:")
            pos2 = self.get_valid_position("Enter position (row col): ")
            if pos2 is None:
                print("\nGame ended. Thanks for playing!")
                return
            
            if pos1 == pos2:
                print("You selected the same card twice! Try again.")
                time.sleep(1)
                continue
            
            # Show both cards
            self.display_board([pos1, pos2])
            self.attempts += 1
            
            # Check for match
            row1, col1 = pos1
            row2, col2 = pos2
            
            if self.board[row1][col1] == self.board[row2][col2]:
                print("\n✨ MATCH FOUND! ✨")
                self.matched[row1][col1] = True
                self.matched[row2][col2] = True
                self.matches_found += 1
                time.sleep(1.5)
            else:
                print("\n❌ No match. Try again!")
                time.sleep(2)
        
        # Game completed
        self.display_board()
        elapsed_time = time.time() - self.start_time
        
        print("\n" + "="*50)
        print("   🎉 CONGRATULATIONS! YOU WON! 🎉")
        print("="*50)
        print(f"\nTotal Attempts: {self.attempts}")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
        print(f"Efficiency: {(self.total_pairs / self.attempts * 100):.1f}%")
        print("\nThanks for playing!\n")

def main():
    """Main function to run the game."""
    print("\n" + "="*50)
    print("   EMOJI MEMORY MATCH GAME")
    print("="*50)
    
    # Get grid size from user
    while True:
        try:
            size = input("\nSelect grid size (2, 4, or 6) [default: 4]: ").strip()
            if not size:
                size = 4
            else:
                size = int(size)
            
            if size in [2, 4, 6]:
                break
            else:
                print("Please choose 2, 4, or 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Create and start the game
    game = EmojiMemoryGame(grid_size=size)
    game.play()
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        main()
    else:
        print("\nGoodbye! 👋\n")

if __name__ == "__main__":
    main()
