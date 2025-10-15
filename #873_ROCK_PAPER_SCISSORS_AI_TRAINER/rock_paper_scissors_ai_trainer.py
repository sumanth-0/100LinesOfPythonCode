"""
Rock-Paper-Scissors AI Trainer
Author: Diya Satish Kumar
Play RPS against an AI that predicts your next move using simple frequency logic.
"""

import random

moves = ["rock", "paper", "scissors"]

def get_ai_move(history):
    if not history:
        return random.choice(moves)
    # Predict user's most frequent move
    prediction = max(set(history), key=history.count)
    # AI plays the winning move
    if prediction == "rock":
        return "paper"
    elif prediction == "paper":
        return "scissors"
    else:
        return "rock"

def decide_winner(player, ai):
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "player"
    else:
        return "ai"

def main():
    print("🪨📄✂️ Rock-Paper-Scissors AI Trainer 🧠")
    print("Type 'quit' to exit.\n")

    history, score = [], {"player": 0, "ai": 0, "draw": 0}

    while True:
        player = input("Your move (rock/paper/scissors): ").lower().strip()
        if player == "quit":
            break
        if player not in moves:
            print("⚠️ Invalid input! Try again.\n")
            continue

        ai = get_ai_move(history)
        history.append(player)
        winner = decide_winner(player, ai)

        if winner == "player":
            print(f"✅ You win! (AI chose {ai})")
            score["player"] += 1
        elif winner == "ai":
            print(f"🤖 AI wins! (AI chose {ai})")
            score["ai"] += 1
        else:
            print(f"🤝 It's a draw! (AI also chose {ai})")
            score["draw"] += 1

        print(f"Score → You: {score['player']} | AI: {score['ai']} | Draws: {score['draw']}\n")

    print("\n🏁 Final Scoreboard:")
    print(f"You: {score['player']} | AI: {score['ai']} | Draws: {score['draw']}")
    print("Thanks for playing! 🎉")

if __name__ == "__main__":
    main()
