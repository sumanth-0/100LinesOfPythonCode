import random

def create_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()
    while len(mine_positions) < mines:
        pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        mine_positions.add(pos)
    for r, c in mine_positions:
        board[r][c] = -1
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != -1:
                    board[nr][nc] += 1
    return board, mine_positions

def print_board(board, revealed, flagged, rows, cols):
    print("\n   ", end="")
    for c in range(cols):
        print(f"{c:2}", end=" ")
    print()
    for r in range(rows):
        print(f"{r:2} ", end="")
        for c in range(cols):
            if flagged[r][c]:
                print(" F", end=" ")
            elif not revealed[r][c]:
                print(" .", end=" ")
            elif board[r][c] == -1:
                print(" *", end=" ")
            elif board[r][c] == 0:
                print("  ", end=" ")
            else:
                print(f"{board[r][c]:2}", end=" ")
        print()

def reveal(board, revealed, r, c, rows, cols):
    if revealed[r][c] or board[r][c] == -1:
        return
    revealed[r][c] = True
    if board[r][c] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not revealed[nr][nc]:
                    reveal(board, revealed, nr, nc, rows, cols)

def play_minesweeper():
    rows, cols, mines = 8, 8, 10
    board, mine_positions = create_board(rows, cols, mines)
    revealed = [[False] * cols for _ in range(rows)]
    flagged = [[False] * cols for _ in range(rows)]
    game_over = False
    
    print("=== Text-based Minesweeper ===")
    print(f"Board: {rows}x{cols}, Mines: {mines}")
    print("Commands: 'r row col' to reveal, 'f row col' to flag/unflag, 'q' to quit")
    
    while not game_over:
        print_board(board, revealed, flagged, rows, cols)
        cmd = input("\nEnter command: ").strip().lower().split()
        
        if not cmd or cmd[0] == 'q':
            print("Game quit!")
            break
        
        if len(cmd) != 3 or cmd[0] not in ['r', 'f']:
            print("Invalid command! Use 'r row col' or 'f row col'")
            continue
        
        try:
            action, r, c = cmd[0], int(cmd[1]), int(cmd[2])
        except ValueError:
            print("Invalid coordinates!")
            continue
        
        if not (0 <= r < rows and 0 <= c < cols):
            print(f"Coordinates out of range! Use 0-{rows-1} for rows, 0-{cols-1} for cols")
            continue
        
        if action == 'f':
            flagged[r][c] = not flagged[r][c]
        elif action == 'r':
            if flagged[r][c]:
                print("Unflag first!")
                continue
            if board[r][c] == -1:
                revealed[r][c] = True
                print_board(board, revealed, flagged, rows, cols)
                print("\nBOOM! You hit a mine! Game Over.")
                game_over = True
            else:
                reveal(board, revealed, r, c, rows, cols)
                if sum(sum(row) for row in revealed) == rows * cols - mines:
                    print_board(board, revealed, flagged, rows, cols)
                    print("\nCongratulations! You won!")
                    game_over = True

if __name__ == "__main__":
    play_minesweeper()
