import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Deck:
    def __init__(self):
        self.cards = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) == 0:
            print("\n🔄 Deck is empty. Reshuffling...")
            self.__init__()  
        return self.cards.pop()

def calculate_hand_value(hand):
    value = sum(values[rank] for rank, suit in hand)
    num_aces = sum(1 for rank, suit in hand if rank == 'A')
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hand(hand, name, hide_first=False):
    if hide_first:
        print(f"{name}'s hand: [Hidden], {hand[1][0]} of {hand[1][1]}")
    else:
        cards = ', '.join([f"{rank} of {suit}" for rank, suit in hand])
        print(f"{name}'s hand: {cards} (Value: {calculate_hand_value(hand)})")

def play_blackjack():
    deck = Deck()
    player_score = 0
    dealer_score = 0
    
    while True:
        print("\n===== New Round =====")
        player_hand = [deck.deal_card(), deck.deal_card()]
        dealer_hand = [deck.deal_card(), deck.deal_card()]

        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer", hide_first=True)

        while calculate_hand_value(player_hand) < 21:
            move = input("Do you want to [h]it or [s]tand? ").lower()
            if move == 'h':
                player_hand.append(deck.deal_card())
                display_hand(player_hand, "Player")
            elif move == 's':
                break
            else:
                print("Invalid input! Please enter 'h' or 's'.")

        player_value = calculate_hand_value(player_hand)
        if player_value > 21:
            print("You busted! Dealer wins.")
            dealer_score += 1
        else:
           
            print("\nDealer's turn:")
            display_hand(dealer_hand, "Dealer")
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.deal_card())
                display_hand(dealer_hand, "Dealer")

            dealer_value = calculate_hand_value(dealer_hand)
            
            
            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
                player_score += 1
            elif player_value < dealer_value:
                print("Dealer wins.")
                dealer_score += 1
            else:
                print("It's a tie!")

        print(f"\nScoreboard — Player: {player_score} | Dealer: {dealer_score}")

        again = input("\nPlay another round? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing Blackjack!")
            break


if __name__ == "__main__":
    play_blackjack()