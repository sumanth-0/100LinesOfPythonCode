"""
Mini Blackjack Simulator
Author: Diya Satish Kumar
A simple text-based blackjack game where you play against the computer dealer.
"""

import random

def draw_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # J, Q, K = 10, A = 11
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    # Convert Ace from 11 to 1 if over 21
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def display_hand(name, hand):
    print(f"{name}'s hand: {hand} (Total: {calculate_score(hand)})")

def blackjack():
    print("♠️ ♥️ Welcome to Mini Blackjack! ♦️ ♣️\n")
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    display_hand("Your", player)
    print(f"Dealer's visible card: {dealer[0]}\n")

    # Player turn
    while True:
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == "h":
            player.append(draw_card())
            display_hand("Your", player)
            if calculate_score(player) > 21:
                print("💥 Bust! You went over 21. Dealer wins.")
                return
        elif choice == "s":
            break
        else:
            print("⚠️ Invalid choice. Enter 'h' or 's'.")

    # Dealer turn
    print("\n🂠 Dealer's turn...")
    display_hand("Dealer", dealer)
    while calculate_score(dealer) < 17:
        dealer.append(draw_card())
        display_hand("Dealer", dealer)

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print("\n🏁 Final Results:")
    display_hand("Your", player)
    display_hand("Dealer", dealer)

    if dealer_score > 21 or player_score > dealer_score:
        print("🎉 You win!")
    elif player_score < dealer_score:
        print("😞 Dealer wins!")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    blackjack()