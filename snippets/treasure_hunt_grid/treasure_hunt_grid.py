import random

# Constants
GRID_SIZE = 5
NUM_TREASURES = 3

def create_grid(size):
    """Create an empty grid"""
    return [['~' for _ in range(size)] for _ in range(size)]

def place_treasures(size, num_treasures):
    """Randomly place treasures on the grid"""
    treasures = set()
    while len(treasures) < num_treasures:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        treasures.add((x, y))
    return treasures

def display_grid(grid, revealed=None):
    """Display the current state of the grid"""
    print("\n    ", end="")
    for col in range(len(grid)):
        print(f" {col} ", end="")
    print("\n   +" + "---+" * len(grid))
    
    for row_idx, row in enumerate(grid):
        print(f" {row_idx} |", end="")
        for col_idx, cell in enumerate(row):
            if revealed and (row_idx, col_idx) in revealed:
                print(f" {cell} ", end="|")
            else:
                print(" ~ ", end="|")
        print("\n   +" + "---+" * len(grid))

def get_coordinates():
    """Get valid coordinates from user"""
    while True:
        try:
            coord = input("\nEnter coordinates (row col): ")
            row, col = map(int, coord.split())
            
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                return row, col
            else:
                print(f"❌ Invalid! Row and column must be between 0 and {GRID_SIZE - 1}")
        except ValueError:
            print("❌ Invalid input! Please enter two numbers separated by a space.")

def calculate_distance(pos1, pos2):
    """Calculate Manhattan distance between two positions"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_hint(guess, treasures):
    """Provide a hint based on proximity to nearest treasure"""
    min_distance = min(calculate_distance(guess, treasure) for treasure in treasures)
    
    if min_distance == 0:
        return "🎰 TREASURE FOUND!"
    elif min_distance == 1:
        return "🔥 Very Hot! Treasure is 1 step away!"
    elif min_distance == 2:
        return "🔥 Hot! Treasure is 2 steps away!"
    elif min_distance <= 3:
        return "🔶 Warm! Getting closer..."
    else:
        return "❄️ Cold! Treasure is far away..."

def play_game():
    """Main game logic"""
    print("\n" + "="*50)
    print("     🏴‍☠️ TREASURE HUNT GRID 🏴‍☠️")
    print("="*50)
    print(f"\nFind all {NUM_TREASURES} hidden treasures!")
    print(f"Grid size: {GRID_SIZE}x{GRID_SIZE}")
    print("\n📍 Hints: 🔥 = Hot, 🔶 = Warm, ❄️ = Cold")
    
    grid = create_grid(GRID_SIZE)
    treasures = place_treasures(GRID_SIZE, NUM_TREASURES)
    found_treasures = set()
    revealed = set()
    attempts = 0
    
    while len(found_treasures) < NUM_TREASURES:
        display_grid(grid, revealed)
        
        print(f"\n🎯 Progress: {len(found_treasures)}/{NUM_TREASURES} treasures found")
        print(f"🎯 Attempts: {attempts}")
        
        row, col = get_coordinates()
        guess = (row, col)
        attempts += 1
        
        if guess in revealed:
            print("⚠️ You already tried this spot!")
            continue
        
        revealed.add(guess)
        
        if guess in treasures:
            found_treasures.add(guess)
            grid[row][col] = 'X'
            print(f"\n🎉 {get_hint(guess, treasures)}")
        else:
            hint = get_hint(guess, treasures - found_treasures)
            print(f"\n{hint}")
    
    display_grid(grid, revealed)
    print("\n" + "="*50)
    print("🎆 CONGRATULATIONS! You found all treasures!")
    print(f"🎆 Total attempts: {attempts}")
    print("="*50)

def main():
    """Main program loop"""
    while True:
        play_game()
        
        play_again = input("\n🎮 Play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing Treasure Hunt Grid!")
            break

if __name__ == "__main__":
    main()
