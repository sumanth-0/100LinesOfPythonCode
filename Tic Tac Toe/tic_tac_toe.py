# Function to display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if a player wins
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get user input (adjusted to use 1, 2, 3)
        try:
            row = int(input(f"Player {current_player}, enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1, 2, or 3): ")) - 1

            # Check if the input is valid
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter numbers between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the cell is already taken
        if board[row][col] != " ":
            print("This spot is taken! Try again.")
            continue

        # Place the move on the board
        board[row][col] = current_player

        # Check if the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if it's a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
