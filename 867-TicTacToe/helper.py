import tkinter as tk

PLAYER = "X"
AI = "O"
def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif winner == "Tie":
        return 0
    if is_max:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score
    
def best_move(board):
    move = None
    best_score_val = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score_val:
                    best_score_val = score
                    move = (i, j)
    return move

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Tie"
    return None
