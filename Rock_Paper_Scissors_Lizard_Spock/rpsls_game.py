#!/usr/bin/env python3
import random


def get_winner(player, computer):
    """Determine winner based on RPSLS rules."""
    rules = {
        'rock': ['lizard', 'scissors'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    
    if player == computer:
        return 'tie'
    elif computer in rules[player]:
        return 'player'
    else:
        return 'computer'


def get_action_description(winner, loser):
    """Get description of how winner beats loser."""
    actions = {
        ('rock', 'lizard'): 'Rock crushes Lizard',
        ('rock', 'scissors'): 'Rock crushes Scissors',
        ('paper', 'rock'): 'Paper covers Rock',
        ('paper', 'spock'): 'Paper disproves Spock',
        ('scissors', 'paper'): 'Scissors cuts Paper',
        ('scissors', 'lizard'): 'Scissors decapitates Lizard',
        ('lizard', 'spock'): 'Lizard poisons Spock',
        ('lizard', 'paper'): 'Lizard eats Paper',
        ('spock', 'scissors'): 'Spock smashes Scissors',
        ('spock', 'rock'): 'Spock vaporizes Rock'
    }
    return actions.get((winner, loser), '')


def display_choices():
    """Display available choices."""
    print("\nChoices:")
    print("1. Rock")
    print("2. Paper") 
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")


def get_player_choice():
    """Get and validate player choice."""
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5 or name): ").strip().lower()
            
            if choice in ['1', '2', '3', '4', '5']:
                return choices[int(choice) - 1]
            elif choice in choices:
                return choice
            else:
                print("Invalid choice! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Try again.")


def play_round():
    """Play a single round."""
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    
    display_choices()
    player_choice = get_player_choice()
    computer_choice = random.choice(choices)
    
    print(f"\nYou chose: {player_choice.title()}")
    print(f"Computer chose: {computer_choice.title()}")
    
    result = get_winner(player_choice, computer_choice)
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'player':
        action = get_action_description(player_choice, computer_choice)
        print(f"You win! {action}")
    else:
        action = get_action_description(computer_choice, player_choice)
        print(f"Computer wins! {action}")
    
    return result


def main():
    """Main game loop."""
    print("Rock-Paper-Scissors-Lizard-Spock")
    print("=" * 35)
    
    scores = {'player': 0, 'computer': 0, 'ties': 0}
    
    while True:
        result = play_round()
        scores[result if result != 'tie' else 'ties'] += 1
        
        print(f"\nScore - You: {scores['player']}, Computer: {scores['computer']}, Ties: {scores['ties']}")
        
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break
    
    print("\nFinal Score:")
    print(f"You: {scores['player']}")
    print(f"Computer: {scores['computer']}")
    print(f"Ties: {scores['ties']}")
    
    if scores['player'] > scores['computer']:
        print("You won overall!")
    elif scores['computer'] > scores['player']:
        print("Computer won overall!")
    else:
        print("Overall tie!")


if __name__ == "__main__":
    main()