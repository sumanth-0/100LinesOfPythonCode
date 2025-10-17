import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10=J/Q/K, 11=Ace

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    # Handle Aces: if total > 21, treat Ace as 1 instead of 11
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

player = [deal_card(), deal_card()]
dealer = [deal_card(), deal_card()]

print(f"Your cards: {player}, current score: {calculate_score(player)}")
print(f"Dealer's first card: {dealer[0]}")

game_over = False

while not game_over:
    if calculate_score(player) > 21:
        print("You went over 21. You lose 😢")
        game_over = True
        break
    action = input("Type 'hit' to draw another card or 'stand' to pass: ")
    if action == "hit":
        player.append(deal_card())
        print(f"Your cards: {player}, current score: {calculate_score(player)}")
    else:
        game_over = True

while calculate_score(dealer) < 17:
    dealer.append(deal_card())

print(f"\nYour final hand: {player}, score: {calculate_score(player)}")
print(f"Dealer's final hand: {dealer}, score: {calculate_score(dealer)}")

if calculate_score(player) > 21:
    print("You lose 😢")
elif calculate_score(dealer) > 21 or calculate_score(player) > calculate_score(dealer):
    print("You win 🎉")
elif calculate_score(player) < calculate_score(dealer):
    print("You lose 😢")
else:
    print("It's a draw 🤝")
