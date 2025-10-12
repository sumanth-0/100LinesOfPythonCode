# Minesweeper Text Version

A classic text-based Minesweeper game implemented in Python.

## Description

This is a command-line implementation of the classic Minesweeper game. Players must reveal cells on an 8x8 grid while avoiding hidden mines. Use logic and deduction to flag potential mines and clear safe cells to win!

## Features

- 8x8 game board with 10 randomly placed mines
- Reveal cells with the 'r' command
- Flag/unflag suspected mines with the 'f' command
- Automatic reveal of adjacent empty cells
- Win/lose detection
- Clear visual representation using ASCII characters

## How to Play

1. Run the game:
   ```bash
   python minesweeper_text_version.py
   ```

2. Commands:
   - `r row col` - Reveal a cell at the specified coordinates
   - `f row col` - Flag/unflag a cell as a potential mine
   - `q` - Quit the game

3. Board symbols:
   - `.` - Unrevealed cell
   - `F` - Flagged cell
   - `*` - Mine (shown after game over)
   - Numbers (1-8) - Count of adjacent mines
   - Empty space - No adjacent mines

## Gameplay Tips

- Start by revealing cells in corners or edges
- Use numbers to deduce mine locations
- Flag cells you're certain contain mines
- If a cell shows 0, all adjacent cells are safe and will auto-reveal

## Example

```
=== Text-based Minesweeper ===
Board: 8x8, Mines: 10
Commands: 'r row col' to reveal, 'f row col' to flag/unflag, 'q' to quit

    0  1  2  3  4  5  6  7
 0  .  .  .  .  .  .  .  .
 1  .  .  .  .  .  .  .  .
 2  .  .  .  .  .  .  .  .
 3  .  .  .  .  .  .  .  .
 4  .  .  .  .  .  .  .  .
 5  .  .  .  .  .  .  .  .
 6  .  .  .  .  .  .  .  .
 7  .  .  .  .  .  .  .  .

Enter command: r 0 0
```

## Requirements

- Python 3.x
- No external dependencies required

## Contributing

This project is part of the 100LinesOfPythonCode repository. Contributions and improvements are welcome!

## Related Issue

This implementation addresses issue #765 in the 100LinesOfPythonCode repository.
