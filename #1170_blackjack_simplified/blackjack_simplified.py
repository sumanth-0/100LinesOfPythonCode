import random

def create_deck():
    """Create and shuffle a standard 52-card deck."""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Calculate the value of a card."""
    rank = card[:-1]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    return int(rank)

def hand_value(hand):
    """Calculate total value of a hand, adjusting for Aces."""
    value = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[:-1] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(name, hand, hide_first=False):
    """Display a player's hand."""
    if hide_first:
        print(f"{name}'s hand: [Hidden] {' '.join(hand[1:])}")
    else:
        print(f"{name}'s hand: {' '.join(hand)} (Value: {hand_value(hand)})")

def player_turn(deck, player_hand):
    """Handle player's turn."""
    while True:
        display_hand("Player", player_hand)
        if hand_value(player_hand) > 21:
            print("Bust! You lose.")
            return False
        choice = input("Hit (h) or Stand (s)? ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            return True
        else:
            print("Invalid choice. Please enter 'h' or 's'.")

def dealer_turn(deck, dealer_hand):
    """Handle dealer's turn."""
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    display_hand("Dealer", dealer_hand)

def determine_winner(player_hand, dealer_hand):
    """Determine the winner."""
    player_val = hand_value(player_hand)
    dealer_val = hand_value(dealer_hand)
    
    if dealer_val > 21:
        print("Dealer busts! You win!")
    elif player_val > dealer_val:
        print(f"You win! {player_val} vs {dealer_val}")
    elif player_val < dealer_val:
        print(f"Dealer wins! {dealer_val} vs {player_val}")
    else:
        print(f"Push! Both have {player_val}")

def play_blackjack():
    """Main game loop."""
    print("=== Blackjack Simplified ===")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    display_hand("Dealer", dealer_hand, hide_first=True)
    display_hand("Player", player_hand)
    
    if hand_value(player_hand) == 21:
        print("Blackjack! You win!")
        return
    
    if player_turn(deck, player_hand):
        print("\nDealer's turn...")
        dealer_turn(deck, dealer_hand)
        determine_winner(player_hand, dealer_hand)

if __name__ == "__main__":
    while True:
        play_blackjack()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break
