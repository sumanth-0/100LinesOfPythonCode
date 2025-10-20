import random

# --- Sudoku Solver and Generator ---
# Author: <Your Name>
# Description: Generates a Sudoku puzzle and solves it using backtracking.
# Lines: ~95

N = 9  # size of the grid

def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i in range(N):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(N):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()

def find_empty(board):
    """Find the next empty cell (row, col)."""
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None

def valid(board, num, pos):
    """Check if placing num at pos (row, col) is valid."""
    r, c = pos
    # Check row
    if num in board[r]:
        return False
    # Check column
    if num in [board[i][c] for i in range(N)]:
        return False
    # Check 3x3 box
    box_x, box_y = c // 3, r // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    """Solve Sudoku using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    r, c = empty
    for num in range(1, 10):
        if valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0  # Backtrack
    return False

def fill_diagonal_boxes(board):
    """Fill the diagonal 3x3 boxes for Sudoku generation."""
    for k in range(0, N, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[k + i][k + j] = nums.pop()

def remove_numbers(board, holes=40):
    """Remove numbers to create a puzzle."""
    count = holes
    while count > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            count -= 1

def generate_puzzle():
    """Generate a new Sudoku puzzle."""
    board = [[0] * 9 for _ in range(9)]
    fill_diagonal_boxes(board)
    solve(board)
    puzzle = [row[:] for row in board]
    remove_numbers(puzzle)
    return puzzle, board

if __name__ == "__main__":
    puzzle, solution = generate_puzzle()
    print("🧩 Generated Sudoku Puzzle:")
    print_board(puzzle)
    print("✅ Solved Sudoku:")
    print_board(solution)
