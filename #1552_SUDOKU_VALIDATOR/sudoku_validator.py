def is_unique(numbers):
    #Check if numbers are unique ignoring zeros.
    nums = [num for num in numbers if num != 0]
    return len(nums) == len(set(nums))

def is_valid_sudoku(grid):
    #Check rows
    for row in grid:
        if not is_unique(row):
            return False
    #Check columns
    for col in zip(*grid):
        if not is_unique(col):
            return False
    #Check 3x3 sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_unique(block):
                return False
    return True
file_path="sudoku.txt" 
grid=[]
with open(file_path, "r") as f:
    for line in f:
        row = list(map(int, line.split()))
        if len(row) != 9:
            raise ValueError("Each row must have exactly 9 numbers.")
        grid.append(row)

if len(grid) != 9:
    raise ValueError("The grid must have exactly 9 rows.")
if is_valid_sudoku(grid):
    print("The Sudoku grid is valid.")
else:
    print("The Sudoku grid is invalid.")
