import random

def print_board(board):
    """Display the current board state."""
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(board, player):
    """Check if the player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != ' ' for cell in board)

def get_available_moves(board):
    """Return list of available positions."""
    return [i for i, cell in enumerate(board) if cell == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning."""
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def ai_move(board):
    """AI makes the best move using minimax."""
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    """Main game loop."""
    board = [' '] * 9
    print("Welcome to Command Line Tic-Tac-Toe AI!")
    print("You are X, AI is O. Positions are 1-9.")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    
    while True:
        print_board(board)
        # Player move
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move in get_available_moves(board):
                    board[move] = 'X'
                    break
                print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Please enter a number between 1 and 9.")
        
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # AI move
        print("AI is thinking...")
        ai_position = ai_move(board)
        board[ai_position] = 'O'
        print(f"AI chose position {ai_position + 1}")
        
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
