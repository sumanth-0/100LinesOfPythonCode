import random
import time

def print_separator():
    """Print a visual separator."""
    print("=" * 50)

def display_banner():
    """Display the game banner."""
    print_separator()
    print("   COIN FLIP TOURNAMENT".center(50))
    print_separator()

def flip_coin():
    """Simulate a coin flip and return 'Heads' or 'Tails'."""
    return random.choice(['Heads', 'Tails'])

def animate_flip():
    """Animate the coin flipping."""
    print("\nFlipping", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    time.sleep(0.3)
    print()

def play_match(player1, player2, match_num):
    """Play a single match between two players."""
    print(f"\nMatch {match_num}: {player1} vs {player2}")
    print(f"{player1} chooses: ", end="")
    p1_choice = input("(H for Heads, T for Tails): ").strip().upper()
    
    while p1_choice not in ['H', 'T']:
        print("Invalid choice! Please enter H or T: ", end="")
        p1_choice = input().strip().upper()
    
    p1_choice = 'Heads' if p1_choice == 'H' else 'Tails'
    p2_choice = 'Tails' if p1_choice == 'Heads' else 'Heads'
    
    print(f"{player2} automatically gets: {p2_choice}")
    
    animate_flip()
    result = flip_coin()
    print(f"Result: {result}!")
    
    if result == p1_choice:
        print(f"🏆 {player1} wins!")
        return player1
    else:
        print(f"🏆 {player2} wins!")
        return player2

def run_tournament():
    """Run the main tournament."""
    display_banner()
    
    # Get number of players
    while True:
        try:
            num_players = int(input("\nEnter number of players (must be power of 2, e.g., 2, 4, 8): "))
            if num_players > 0 and (num_players & (num_players - 1)) == 0:
                break
            else:
                print("Please enter a power of 2 (2, 4, 8, 16, etc.)")
        except ValueError:
            print("Please enter a valid number!")
    
    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter name: ").strip()
        players.append(name)
    
    round_num = 1
    match_counter = 1
    
    # Tournament rounds
    while len(players) > 1:
        print_separator()
        print(f"\n   ROUND {round_num}".center(50))
        print(f"   {len(players)} players remaining".center(50))
        print_separator()
        
        winners = []
        for i in range(0, len(players), 2):
            winner = play_match(players[i], players[i+1], match_counter)
            winners.append(winner)
            match_counter += 1
        
        players = winners
        round_num += 1
    
    # Tournament winner
    print_separator()
    print(f"\n🎉 TOURNAMENT CHAMPION: {players[0]} 🎉".center(50))
    print_separator()

if __name__ == "__main__":
    run_tournament()
