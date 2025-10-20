"""
Rock-Paper-Scissors-Lizard-Spock
Beat the computer in this extended version of Rock Paper Scissor
"""

import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WIN_RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif computer in WIN_RULES[player]:
        return "You win !!"
    else:
        return "Computer wins !!"

def main():
    print("=== Rock-Paper-Scissors-Lizard-Spock ===\n")
    while True:
        print("Choices:", ", ".join(CHOICES))
        player = input("Enter your choice: ").strip().lower()
        if player not in CHOICES:
            print("Invalid choice! Try again.\n")
            continue
        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")
        print(determine_winner(player, computer), "\n")
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye ✨")
            break

if __name__ == "__main__":
    main()
