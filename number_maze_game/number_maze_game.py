#!/usr/bin/env python3
"""
Number Maze Game

Navigate through a number-based maze where you can only move to adjacent cells
with specific number relationships. Use W/A/S/D keys to reach the goal.
"""

import random
import os
import sys

class NumberMazeGame:
    """A terminal-based number maze navigation game."""
    
    def __init__(self, rows=8, cols=10):
        """Initialize the maze game.
        
        Args:
            rows: Number of rows in the maze
            cols: Number of columns in the maze
        """
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.player_pos = [0, 0]
        self.goal_pos = [rows - 1, cols - 1]
        self.moves = 0
        self.generate_maze()
    
    def generate_maze(self):
        """Generate a random number maze."""
        # Create maze with random numbers 1-9
        self.maze = [[random.randint(1, 9) for _ in range(self.cols)] 
                     for _ in range(self.rows)]
        
        # Set player starting position
        self.player_pos = [0, 0]
        self.maze[0][0] = 5  # Starting number
        
        # Set goal position
        self.maze[self.rows - 1][self.cols - 1] = 9  # Goal number
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_maze(self):
        """Display the current maze state."""
        self.clear_screen()
        print("\n" + "="*50)
        print("NUMBER MAZE GAME".center(50))
        print("="*50)
        print("\nGoal: Navigate to the bottom-right corner (marked with *)")
        print("Rules: Move to adjacent cells where the number difference is ≤ 3")
        print("Controls: W(up) A(left) S(down) D(right) Q(quit)\n")
        
        # Display maze
        for i in range(self.rows):
            row_str = ""
            for j in range(self.cols):
                if [i, j] == self.player_pos:
                    row_str += " @ "
                elif [i, j] == self.goal_pos:
                    row_str += " * "
                else:
                    row_str += f" {self.maze[i][j]} "
            print(row_str)
        
        print(f"\nMoves: {self.moves}")
        print(f"Current Position: ({self.player_pos[0]}, {self.player_pos[1]})")
        print(f"Current Number: {self.maze[self.player_pos[0]][self.player_pos[1]]}")
    
    def is_valid_move(self, new_row, new_col):
        """Check if a move is valid.
        
        Args:
            new_row: Target row position
            new_col: Target column position
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        # Check if within bounds
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return False
        
        # Check if number difference is acceptable (≤ 3)
        current_num = self.maze[self.player_pos[0]][self.player_pos[1]]
        target_num = self.maze[new_row][new_col]
        
        if abs(current_num - target_num) <= 3:
            return True
        return False
    
    def move_player(self, direction):
        """Move the player in the specified direction.
        
        Args:
            direction: One of 'w', 'a', 's', 'd'
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        new_row, new_col = self.player_pos[0], self.player_pos[1]
        
        if direction == 'w':  # Up
            new_row -= 1
        elif direction == 's':  # Down
            new_row += 1
        elif direction == 'a':  # Left
            new_col -= 1
        elif direction == 'd':  # Right
            new_col += 1
        else:
            return False
        
        if self.is_valid_move(new_row, new_col):
            self.player_pos = [new_row, new_col]
            self.moves += 1
            return True
        else:
            print("\nInvalid move! Number difference too large or out of bounds.")
            input("Press Enter to continue...")
            return False
    
    def check_win(self):
        """Check if player has reached the goal.
        
        Returns:
            bool: True if player won, False otherwise
        """
        return self.player_pos == self.goal_pos
    
    def play(self):
        """Main game loop."""
        print("Welcome to Number Maze Game!")
        print("Loading...")
        
        while True:
            self.display_maze()
            
            if self.check_win():
                print("\n" + "="*50)
                print("CONGRATULATIONS! YOU WON!".center(50))
                print("="*50)
                print(f"\nYou completed the maze in {self.moves} moves!")
                break
            
            # Get player input
            try:
                move = input("\nEnter your move: ").lower().strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\nGame interrupted. Goodbye!")
                break
            
            if move == 'q':
                print("\nThanks for playing! Goodbye!")
                break
            elif move in ['w', 'a', 's', 'd']:
                self.move_player(move)
            else:
                print("\nInvalid input! Use W/A/S/D to move or Q to quit.")
                input("Press Enter to continue...")

def main():
    """Main function to start the game."""
    print("\nNumber Maze Game")
    print("================\n")
    
    # Ask for difficulty
    print("Select difficulty:")
    print("1. Easy (6x8)")
    print("2. Medium (8x10)")
    print("3. Hard (10x12)")
    
    try:
        choice = input("\nEnter choice (1-3, default 2): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nGoodbye!")
        return
    
    if choice == '1':
        game = NumberMazeGame(6, 8)
    elif choice == '3':
        game = NumberMazeGame(10, 12)
    else:
        game = NumberMazeGame(8, 10)
    
    game.play()

if __name__ == "__main__":
    main()
