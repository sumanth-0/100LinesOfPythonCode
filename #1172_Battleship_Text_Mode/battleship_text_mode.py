import random

def create_board(size=5):
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_ships(board, num_ships=3):
    ships = []
    for _ in range(num_ships):
        while True:
            row, col = random.randint(0, len(board)-1), random.randint(0, len(board)-1)
            if board[row][col] == ' ':
                board[row][col] = 'S'
                ships.append((row, col))
                break
    return ships

def print_board(board, hide_ships=True):
    print('\n  ' + ' '.join([str(i) for i in range(len(board))]))
    for idx, row in enumerate(board):
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append(' ')
            else:
                display_row.append(cell)
        print(f"{idx} {' '.join(display_row)}")
    print()

def get_guess():
    while True:
        try:
            guess = input("Enter coordinates (row col): ").split()
            if len(guess) != 2:
                raise ValueError
            row, col = int(guess[0]), int(guess[1])
            return row, col
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers separated by space.")

def play_game():
    print("\n=== BATTLESHIP TEXT MODE ===")
    print("Find and sink all enemy ships!\n")
    
    size = 5
    num_ships = 3
    board = create_board(size)
    ships = place_ships(board, num_ships)
    guesses = 0
    max_guesses = 15
    hits = 0
    
    print(f"Board size: {size}x{size}")
    print(f"Ships to find: {num_ships}")
    print(f"Maximum guesses: {max_guesses}\n")
    
    while guesses < max_guesses and hits < num_ships:
        print(f"Guesses remaining: {max_guesses - guesses}")
        print(f"Ships hit: {hits}/{num_ships}")
        print_board(board)
        
        row, col = get_guess()
        
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Out of bounds! Try again.")
            continue
        
        guesses += 1
        
        if board[row][col] == 'S':
            print("\n💥 HIT! You sunk a battleship!\n")
            board[row][col] = 'X'
            hits += 1
        elif board[row][col] in ['X', 'O']:
            print("\n⚠️  Already guessed this location!\n")
        else:
            print("\n💧 MISS!\n")
            board[row][col] = 'O'
    
    print("\n=== GAME OVER ===")
    print(f"Final board (ships revealed):")
    print_board(board, hide_ships=False)
    
    if hits == num_ships:
        print(f"🎉 VICTORY! You found all ships in {guesses} guesses!")
    else:
        print(f"💀 DEFEAT! You ran out of guesses. Ships hit: {hits}/{num_ships}")

if __name__ == "__main__":
    play_game()
