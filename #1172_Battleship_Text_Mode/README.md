# Battleship Text Mode

A classic text-based Battleship game implementation in Python.

## Description

This is a single-player Battleship game where you try to find and sink randomly placed ships on a 5x5 grid. The game features:

- **Board Size**: 5x5 grid
- **Number of Ships**: 3 ships to find
- **Maximum Guesses**: 15 attempts to sink all ships
- **Visual Feedback**: 
  - `X` marks hits
  - `O` marks misses
  - Ships are hidden until revealed

## Features

- Random ship placement for replayability
- Input validation for coordinates
- Clear visual board representation
- Game statistics tracking (guesses remaining, ships hit)
- Win/loss conditions
- Final board reveal showing all ship locations

## How to Play

1. Run the script:
   ```bash
   python battleship_text_mode.py
   ```

2. The game will display a 5x5 grid with coordinates (0-4 for both rows and columns)

3. Enter your guess as two numbers separated by a space:
   ```
   Enter coordinates (row col): 2 3
   ```

4. The game will tell you if you:
   - **HIT** 💥: Successfully found a ship
   - **MISS** 💧: No ship at that location
   - Already guessed that location ⚠️

5. Continue guessing until you:
   - **WIN** 🎉: Find all 3 ships within 15 guesses
   - **LOSE** 💀: Run out of guesses before finding all ships

## Example Gameplay

```
=== BATTLESHIP TEXT MODE ===
Find and sink all enemy ships!

Board size: 5x5
Ships to find: 3
Maximum guesses: 15

Guesses remaining: 15
Ships hit: 0/3

  0 1 2 3 4
0
1
2
3
4

Enter coordinates (row col): 2 3
💥 HIT! You sunk a battleship!
```

## Code Structure

The game consists of several key functions:

- `create_board(size)`: Creates an empty game board
- `place_ships(board, num_ships)`: Randomly places ships on the board
- `print_board(board, hide_ships)`: Displays the board with optional ship hiding
- `get_guess()`: Gets and validates player input
- `play_game()`: Main game loop

## Requirements

- Python 3.6+
- No external dependencies required

## Technical Details

- **Lines of Code**: 100 lines (fits project requirements)
- **Standard Library Only**: Uses only `random` module
- **Input Validation**: Handles invalid inputs gracefully
- **Game State Management**: Tracks guesses, hits, and board state

## Contributing

This script was created as part of the 100 Lines of Python Code project. Feel free to suggest improvements while keeping the 100-line constraint!

## License

Part of the 100LinesOfPythonCode repository.
