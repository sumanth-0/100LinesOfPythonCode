# Sudoku Validator

This Python script checks whether a given Sudoku grid is valid according to standard Sudoku rules.It ensures that each row, column,and 3x3 sub-grid contains unique numbers(ignoring zeros, which represent empty cells).

## Prerequisites

- Python 3.x
- A text file (`sudoku.txt`) containing the Sudoku grid you want to validate.  
  - Each row must contain **exactly 9 numbers**, separated by spaces.
  - The file must have **exactly 9 rows**.

Example `sudoku.txt`:

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## How it Works

1. The script reads the Sudoku grid from `sudoku.txt`.
2. It checks each **row**, **column**, and **3x3 sub-grid** for uniqueness (excluding zeros).
3. If all rules are satisfied, the grid is considered valid.

## Usage

1. Place your Sudoku grid in a file named `sudoku.txt` in the same folder as the script.
2. Run the script:

```bash
python sudoku_validator.py
```