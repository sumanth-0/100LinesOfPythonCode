#!/usr/bin/env python3
"""
Treasure Hunt Grid Game

A fun game where players navigate through a grid to find hidden treasures
while avoiding traps and obstacles. The goal is to collect all treasures
and reach the exit with the highest score possible.

Author: Contributor
Issue: #1163
"""

import random
import os
import time
from typing import List, Tuple, Dict

class TreasureHuntGrid:
    def __init__(self, width: int = 10, height: int = 10):
        """
        Initialize the treasure hunt grid game.
        
        Args:
            width: Grid width (default: 10)
            height: Grid height (default: 10)
        """
        self.width = width
        self.height = height
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.player_pos = (0, 0)
        self.treasures = set()
        self.traps = set()
        self.obstacles = set()
        self.exit_pos = (height - 1, width - 1)
        self.score = 0
        self.moves = 0
        self.treasures_collected = 0
        self.game_over = False
        self.won = False
        
        # Game symbols
        self.symbols = {
            'player': 'P',
            'treasure': 'T',
            'trap': 'X',
            'obstacle': '#',
            'exit': 'E',
            'empty': '.'
        }
        
        self.setup_game()
    
    def setup_game(self):
        """Set up the game grid with treasures, traps, and obstacles."""
        total_cells = self.width * self.height
        
        # Generate treasures (10-15% of grid)
        treasure_count = max(3, total_cells // 8)
        self.generate_items(treasure_count, 'treasure')
        
        # Generate traps (5-10% of grid)
        trap_count = max(2, total_cells // 15)
        self.generate_items(trap_count, 'trap')
        
        # Generate obstacles (15-20% of grid)
        obstacle_count = max(4, total_cells // 7)
        self.generate_items(obstacle_count, 'obstacle')
        
        self.update_grid_display()
    
    def generate_items(self, count: int, item_type: str):
        """Generate random positions for items on the grid."""
        placed = 0
        max_attempts = count * 10
        attempts = 0
        
        while placed < count and attempts < max_attempts:
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            pos = (row, col)
            
            # Don't place items on player start, exit, or existing items
            if (pos != self.player_pos and pos != self.exit_pos and
                pos not in self.treasures and pos not in self.traps and
                pos not in self.obstacles):
                
                if item_type == 'treasure':
                    self.treasures.add(pos)
                elif item_type == 'trap':
                    self.traps.add(pos)
                elif item_type == 'obstacle':
                    self.obstacles.add(pos)
                
                placed += 1
            
            attempts += 1
    
    def update_grid_display(self):
        """Update the visual representation of the grid."""
        # Reset grid to empty
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = self.symbols['empty']
        
        # Place items on grid
        for pos in self.treasures:
            self.grid[pos[0]][pos[1]] = self.symbols['treasure']
        
        for pos in self.traps:
            self.grid[pos[0]][pos[1]] = self.symbols['trap']
        
        for pos in self.obstacles:
            self.grid[pos[0]][pos[1]] = self.symbols['obstacle']
        
        # Place exit
        self.grid[self.exit_pos[0]][self.exit_pos[1]] = self.symbols['exit']
        
        # Place player
        self.grid[self.player_pos[0]][self.player_pos[1]] = self.symbols['player']
    
    def display_grid(self):
        """Display the current state of the grid."""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("\n" + "="*50)
        print(" 🏴‍☠️  TREASURE HUNT GRID GAME  🏴‍☠️")
        print("="*50)
        
        print(f"Score: {self.score} | Moves: {self.moves} | Treasures: {self.treasures_collected}/{len(self.treasures) + self.treasures_collected}")
        print("\nLegend: P=Player, T=Treasure, X=Trap, #=Obstacle, E=Exit\n")
        
        # Display column numbers
        print("   ", end="")
        for col in range(self.width):
            print(f"{col:2}", end=" ")
        print()
        
        # Display grid with row numbers
        for row in range(self.height):
            print(f"{row:2} ", end="")
            for col in range(self.width):
                cell = self.grid[row][col]
                if cell == 'T':
                    print("💰", end=" ")
                elif cell == 'X':
                    print("💥", end=" ")
                elif cell == '#':
                    print("🧱", end=" ")
                elif cell == 'E':
                    print("🚪", end=" ")
                elif cell == 'P':
                    print("🤠", end=" ")
                else:
                    print("⬜", end=" ")
            print()
        
        print("\n📍 Controls: WASD (W=Up, A=Left, S=Down, D=Right), Q=Quit")
    
    def move_player(self, direction: str) -> bool:
        """Move player in the specified direction."""
        if self.game_over:
            return False
        
        row, col = self.player_pos
        new_row, new_col = row, col
        
        direction = direction.upper()
        if direction == 'W':  # Up
            new_row = max(0, row - 1)
        elif direction == 'S':  # Down
            new_row = min(self.height - 1, row + 1)
        elif direction == 'A':  # Left
            new_col = max(0, col - 1)
        elif direction == 'D':  # Right
            new_col = min(self.width - 1, col + 1)
        else:
            return False
        
        new_pos = (new_row, new_col)
        
        # Check if new position is blocked by obstacle
        if new_pos in self.obstacles:
            print("🧱 Blocked by obstacle! Try another direction.")
            time.sleep(1)
            return False
        
        # Move player to new position
        self.player_pos = new_pos
        self.moves += 1
        
        # Check what's at the new position
        self.check_position_effects()
        
        # Update grid display
        self.update_grid_display()
        
        return True
    
    def check_position_effects(self):
        """Check and handle effects at current player position."""
        pos = self.player_pos
        
        # Check for treasure
        if pos in self.treasures:
            self.treasures.remove(pos)
            self.treasures_collected += 1
            treasure_points = random.randint(10, 50)
            self.score += treasure_points
            print(f"💰 Treasure found! +{treasure_points} points!")
            time.sleep(1)
        
        # Check for trap
        elif pos in self.traps:
            self.traps.remove(pos)
            trap_damage = random.randint(5, 25)
            self.score = max(0, self.score - trap_damage)
            print(f"💥 Trap triggered! -{trap_damage} points!")
            time.sleep(1)
        
        # Check for exit
        elif pos == self.exit_pos:
            if len(self.treasures) == 0:
                self.won = True
                self.game_over = True
                bonus = max(0, 100 - self.moves)
                self.score += bonus
                print(f"🎉 Congratulations! You escaped with all treasures!")
                print(f"🏆 Move efficiency bonus: +{bonus} points!")
            else:
                print(f"🚪 Exit found, but {len(self.treasures)} treasures remain!")
                print("Collect all treasures before escaping!")
            time.sleep(2)
    
    def get_game_stats(self) -> Dict[str, int]:
        """Get current game statistics."""
        return {
            'score': self.score,
            'moves': self.moves,
            'treasures_collected': self.treasures_collected,
            'treasures_remaining': len(self.treasures),
            'traps_remaining': len(self.traps)
        }
    
    def play_game(self):
        """Main game loop."""
        print("🏴‍☠️ Welcome to Treasure Hunt Grid! 🏴‍☠️")
        print("\nObjective: Collect all treasures and reach the exit (bottom-right)!")
        print("Be careful of traps and obstacles!")
        input("\nPress Enter to start...")
        
        while not self.game_over:
            self.display_grid()
            
            try:
                move = input("\nEnter your move (WASD or Q to quit): ").strip().upper()
                
                if move == 'Q':
                    print("\n👋 Thanks for playing!")
                    break
                
                if move in ['W', 'A', 'S', 'D']:
                    self.move_player(move)
                else:
                    print("Invalid move! Use W/A/S/D or Q to quit.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Game interrupted. Thanks for playing!")
                break
        
        # Game ended
        if self.won:
            self.display_grid()
            print("\n🏆 VICTORY! 🏆")
            print(f"Final Score: {self.score}")
            print(f"Total Moves: {self.moves}")
            print(f"Treasures Collected: {self.treasures_collected}")
        
        return self.get_game_stats()

def main():
    """Main function to run the treasure hunt grid game."""
    print("🏴‍☠️ Treasure Hunt Grid Game Setup 🏴‍☠️\n")
    
    try:
        # Get grid size from user
        print("Choose grid size (recommended: 8-15):")
        width = int(input("Enter grid width (default 10): ") or 10)
        height = int(input("Enter grid height (default 10): ") or 10)
        
        # Validate input
        width = max(5, min(20, width))
        height = max(5, min(20, height))
        
        print(f"\nCreating {width}x{height} treasure hunt grid...\n")
        
        # Create and start game
        game = TreasureHuntGrid(width, height)
        stats = game.play_game()
        
        print("\n" + "="*40)
        print(" FINAL GAME STATISTICS")
        print("="*40)
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
    except ValueError:
        print("Invalid input! Using default grid size (10x10)")
        game = TreasureHuntGrid()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\nGame setup interrupted. Goodbye!")

if __name__ == "__main__":
    main()
