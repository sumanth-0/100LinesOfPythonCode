# Number Maze Game

A terminal-based number maze navigation game where you navigate through a maze using W/A/S/D keys to reach the goal.

## Description

Navigate through a number-based maze where you can only move to adjacent cells with specific number relationships. The game features random maze generation, difficulty levels, and move tracking.

## Features

- **Number-Based Movement Rules**: Move only to adjacent cells where the number difference is ≤ 3
- **Terminal-Based Interface**: Clean, ASCII-based display with player position (@) and goal (*)
- **Multiple Difficulty Levels**:
  - Easy: 6x8 grid
  - Medium: 8x10 grid
  - Hard: 10x12 grid
- **Move Counter**: Track your performance
- **Random Maze Generation**: Each game is unique

## How to Play

### Installation

No external dependencies required! Just Python 3.x.

```bash
python number_maze_game.py
```

### Controls

- **W**: Move up
- **A**: Move left
- **S**: Move down
- **D**: Move right
- **Q**: Quit game

### Rules

1. You start at the top-left corner (marked with @)
2. Your goal is to reach the bottom-right corner (marked with *)
3. You can only move to adjacent cells (up, down, left, right)
4. The number difference between your current cell and the target cell must be ≤ 3
5. Plan your route carefully!

### Example Gameplay

```
==================================================
              NUMBER MAZE GAME
==================================================

Goal: Navigate to the bottom-right corner (marked with *)
Rules: Move to adjacent cells where the number difference is ≤ 3
Controls: W(up) A(left) S(down) D(right) Q(quit)

 @ 7 4 2 5 8 3 6 1 9
 5 3 6 1 7 4 8 2 5 3
 2 8 1 4 6 9 3 7 4 1
 7 4 5 2 8 3 6 1 9 5
 3 6 9 7 1 4 8 2 5 3
 8 2 4 5 3 7 1 6 9 4
 1 5 7 3 6 2 4 8 3 7
 4 9 2 6 8 5 7 1 4 *

Moves: 0
Current Position: (0, 0)
Current Number: 5

Enter your move:
```

## Game Mechanics

### Maze Generation

- Each cell is assigned a random number between 1-9
- The starting cell is always set to 5 for balanced gameplay
- The goal cell is marked with 9

### Movement Validation

- Checks if the target position is within maze boundaries
- Calculates the absolute difference between current and target numbers
- Only allows movement if the difference is ≤ 3

## Code Structure

The game is implemented as a single Python class:

- `NumberMazeGame`: Main game class
  - `generate_maze()`: Creates a random number maze
  - `display_maze()`: Renders the current game state
  - `is_valid_move()`: Validates movement rules
  - `move_player()`: Handles player movement
  - `check_win()`: Checks for win condition
  - `play()`: Main game loop

## Contributing

This project was created as part of the 100 Lines of Python Code initiative. Feel free to:

- Report bugs
- Suggest improvements
- Add new features (e.g., different maze algorithms, power-ups, obstacles)

## Related Issue

Resolves issue #869 - Number Maze Game

## License

Part of the 100LinesOfPythonCode repository.
