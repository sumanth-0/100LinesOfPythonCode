# Tiny Sudoku Validator

A Python script that validates a 9x9 Sudoku grid based on standard Sudoku rules.

## Description

This tool checks if a given Sudoku puzzle is valid by verifying:
- Each row contains unique numbers (1-9, with 0 representing empty cells)
- Each column contains unique numbers
- Each 3x3 sub-grid contains unique numbers

## Features

- ✅ Validates complete or partial Sudoku grids
- ✅ Accepts input from command line or file
- ✅ Supports space or comma-separated values
- ✅ Provides detailed error messages for invalid grids
- ✅ Under 100 lines of Python code

## Requirements

- Python 3.x (no external dependencies required)

## Usage

### Interactive Mode

Run the script without arguments to enter grid values interactively:

```bash
python tiny_sudoku_validator.py
```

You'll be prompted to enter 9 rows of numbers (use 0 for empty cells):

```
Enter your 9x9 Sudoku grid (use 0 for empty cells):
Enter one row per line (space or comma-separated):
Example: 5 3 0 0 7 0 0 0 0

Row 1: 5 3 0 0 7 0 0 0 0
Row 2: 6 0 0 1 9 5 0 0 0
Row 3: 0 9 8 0 0 0 0 6 0
...
```

### File Input Mode

Provide a text file containing the Sudoku grid:

```bash
python tiny_sudoku_validator.py sudoku_grid.txt
```

#### File Format

Create a text file with 9 rows of 9 numbers each (space or comma-separated):

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

## Example Output

### Valid Grid

```
==================================================
✓ VALID: This Sudoku grid is valid!
==================================================
```

### Invalid Grid

```
==================================================
✗ INVALID: This Sudoku grid has errors:
  - Row 1 has duplicate numbers
  - Column 3 has duplicate numbers
  - 3x3 box at position (1,1) has duplicate numbers
==================================================
```

## How It Works

1. **Input Parsing**: Reads grid from file or user input
2. **Dimension Check**: Verifies the grid is exactly 9x9
3. **Row Validation**: Checks each row for duplicate non-zero numbers
4. **Column Validation**: Checks each column for duplicate non-zero numbers
5. **Box Validation**: Checks each 3x3 sub-grid for duplicate non-zero numbers
6. **Report**: Displays validation result with specific error messages

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) challenge.

## License

Feel free to use and modify this code for your own projects!

## Author

Created as a solution for issue #673 - Tiny Sudoku Validator
