#!/usr/bin/env python3
"""
Tiny Sudoku Validator
Validates a 9x9 Sudoku grid based on standard Sudoku rules.
"""

import sys


def validate_sudoku(grid):
    """
    Validate a 9x9 Sudoku grid.
    
    Args:
        grid: A 9x9 list of lists containing integers 0-9 (0 represents empty cells)
    
    Returns:
        tuple: (is_valid, error_messages)
    """
    errors = []
    
    # Check grid dimensions
    if len(grid) != 9:
        return False, ["Grid must have exactly 9 rows"]
    
    for i, row in enumerate(grid):
        if len(row) != 9:
            return False, [f"Row {i+1} must have exactly 9 columns"]
    
    # Check rows
    for i, row in enumerate(grid):
        numbers = [num for num in row if num != 0]
        if len(numbers) != len(set(numbers)):
            errors.append(f"Row {i+1} has duplicate numbers")
    
    # Check columns
    for col in range(9):
        numbers = [grid[row][col] for row in range(9) if grid[row][col] != 0]
        if len(numbers) != len(set(numbers)):
            errors.append(f"Column {col+1} has duplicate numbers")
    
    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            numbers = []
            for i in range(3):
                for j in range(3):
                    num = grid[box_row*3 + i][box_col*3 + j]
                    if num != 0:
                        numbers.append(num)
            if len(numbers) != len(set(numbers)):
                errors.append(f"3x3 box at position ({box_row+1},{box_col+1}) has duplicate numbers")
    
    return len(errors) == 0, errors


def parse_grid_from_input(input_text):
    """
    Parse a Sudoku grid from text input.
    Accepts space or comma-separated values, one row per line.
    """
    grid = []
    lines = [line.strip() for line in input_text.strip().split('\n') if line.strip()]
    
    for line in lines:
        # Handle both space and comma separation
        row = line.replace(',', ' ').split()
        row = [int(x) if x.isdigit() else 0 for x in row]
        grid.append(row)
    
    return grid


def main():
    print("Tiny Sudoku Validator")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        # Read from file
        try:
            with open(sys.argv[1], 'r') as f:
                input_text = f.read()
            print(f"Reading grid from file: {sys.argv[1]}")
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
            return
    else:
        # Read from user input
        print("\nEnter your 9x9 Sudoku grid (use 0 for empty cells):")
        print("Enter one row per line (space or comma-separated):")
        print("Example: 5 3 0 0 7 0 0 0 0\n")
        
        lines = []
        for i in range(9):
            line = input(f"Row {i+1}: ")
            lines.append(line)
        input_text = '\n'.join(lines)
    
    grid = parse_grid_from_input(input_text)
    is_valid, errors = validate_sudoku(grid)
    
    print("\n" + "=" * 50)
    if is_valid:
        print("✓ VALID: This Sudoku grid is valid!")
    else:
        print("✗ INVALID: This Sudoku grid has errors:")
        for error in errors:
            print(f"  - {error}")
    print("=" * 50)


if __name__ == "__main__":
    main()
