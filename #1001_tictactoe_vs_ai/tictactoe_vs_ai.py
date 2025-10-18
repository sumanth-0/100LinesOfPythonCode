import random

def print_board(b):
    print("\n".join([" | ".join(r) for r in b]))
    print()

def check_winner(b, p):
    #Check rows, cols, diagonals
    for i in range(3):
        if all(b[i][j]==p for j in range(3)): return True
        if all(b[j][i]==p for j in range(3)): return True
    if all(b[i][i]==p for i in range(3)): return True
    if all(b[i][2-i]==p for i in range(3)): return True
    return False

def moves_left(b):
    return [(i,j) for i in range(3) for j in range(3) if b[i][j]==' ']

def main():
    board = [[' ']*3 for _ in range(3)]
    print("Tic-Tac-Toe! You are X, computer is O.\n")
    print_board(board)

    while True:
        #Player move
        try:
            r,c = map(int, input("Enter row and col (1-3 each): ").split())
            r, c = r-1, c-1
            if (r,c) not in moves_left(board):
                print("Invalid move!\n"); continue
        except:
            print("Invalid input!\n"); continue
        board[r][c] = 'X'

        print_board(board)
        if check_winner(board,'X'):
            print("You win!"); break
        if not moves_left(board):
            print("Draw!"); break

        #Computers random move
        r,c = random.choice(moves_left(board))
        board[r][c] = 'O'
        print("Computer moves:")
        print_board(board)

        if check_winner(board,'O'):
            print("Computer wins!"); break
        if not moves_left(board):
            print("Draw!"); break

if __name__ == "__main__":
    main()
