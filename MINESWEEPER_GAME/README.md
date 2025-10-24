# Minesweeper Game

A simple terminal-based Minesweeper game implemented in Python.

## How to Run

Navigate to MINESWEEPER_GAME directory
```bash
python3 minesweeper.py
```

## Gameplay

- The game prompts for board size (rows, columns) and number of mines.
- Use commands to play:
  - `r row col`: Reveal the cell at row, col (1-indexed)
  - `f row col`: Toggle flag on the cell
  - `q`: Quit the game
- Goal: Reveal all non-mine cells without hitting a mine.
- Numbers show adjacent mines; empty cells flood-fill.