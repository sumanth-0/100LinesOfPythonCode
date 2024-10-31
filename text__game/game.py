import random
import time
# Initialize grid size and symbols
GRID_SIZE = 5
TREASURE_SYMBOL = "T"
PLAYER_SYMBOL = "P"
TRAP_SYMBOL = "X"
EMPTY_SYMBOL = "."

# Initialize player position and score
player_pos = [0, 0]
score = 0
moves = 0

# Generate random positions for treasures and traps
def generate_grid():
    grid = [[EMPTY_SYMBOL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    treasure_count = random.randint(3, 6)
    trap_count = random.randint(2, 4)

    # Place treasures randomly
    for _ in range(treasure_count):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        grid[x][y] = TREASURE_SYMBOL

    # Place traps randomly
    for _ in range(trap_count):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if grid[x][y] == EMPTY_SYMBOL:
            grid[x][y] = TRAP_SYMBOL

    # Place player at starting position
    grid[player_pos[0]][player_pos[1]] = PLAYER_SYMBOL
    return grid

# Display the dungeon grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print(f"\nScore: {score} | Moves: {moves}")

# Move player and update position
def move_player(direction, grid):
    global score, moves
    x, y = player_pos
    grid[x][y] = EMPTY_SYMBOL

    if direction == "W": x -= 1
    elif direction == "S": x += 1
    elif direction == "A": y -= 1
    elif direction == "D": y += 1

    # Stay within bounds
    x = max(0, min(x, GRID_SIZE-1))
    y = max(0, min(y, GRID_SIZE-1))

    # Check cell content
    cell = grid[x][y]
    if cell == TREASURE_SYMBOL:
        print("You found a treasure! +10 points!")
        score += 10
    elif cell == TRAP_SYMBOL:
        print("Oh no! You hit a trap! -5 points!")
        score -= 5

    # Update player position and grid
    player_pos[0], player_pos[1] = x, y
    grid[x][y] = PLAYER_SYMBOL
    moves += 1

# Main game loop
def play_game():
    grid = generate_grid()
    print("Welcome to the Dungeon Treasure Hunt!")
    print("Collect all treasures (T) and avoid traps (X). Use W, A, S, D to move.")
    while True:
        display_grid(grid)
        move = input("Enter move (W/A/S/D) or Q to quit: ").upper()
        if move == "Q":
            print("Thanks for playing!")
            break
        elif move in ["W", "A", "S", "D"]:
            move_player(move, grid)
        else:
            print("Invalid move. Please enter W, A, S, D, or Q.")

        if score >= 30:
            print("Congratulations! You've collected enough treasures!")
            break
        elif score < -10:
            print("Game Over! You've hit too many traps!")
            break

# Start the game
play_game()