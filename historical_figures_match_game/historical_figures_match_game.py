# historical_figures_match_game.py

import random

# List of historical figures with their notable quotes or achievements
figures = [
    {"name": "Albert Einstein", "legacy": "Developed the theory of relativity"},
    {"name": "Marie Curie", "legacy": "Pioneered research on radioactivity"},
    {"name": "Mahatma Gandhi", "legacy": "Led India to independence through non-violent resistance"},
    {"name": "Leonardo da Vinci", "legacy": "Painted the Mona Lisa and contributed to Renaissance science and art"}
]

# Shuffle the legacies for matching challenge
def shuffle_legacies():
    legacies = [f["legacy"] for f in figures]
    random.shuffle(legacies)
    return legacies

# Function to start the matching game
def start_game():
    legacies = shuffle_legacies()
    score = 0
    
    print("Match each historical figure to their correct legacy.\n")
    for idx, legacy in enumerate(legacies, 1):
        print(f"{idx}. {legacy}")

    for figure in figures:
        print(f"\nWho is associated with: {figure['legacy']}?")
        answer = int(input("Enter the correct number: ")) - 1
        
        if figures[answer]["legacy"] == figure["legacy"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {figure['name']}")

    print(f"\nGame Over! Your final score: {score}/{len(figures)}")

# Run the game
if __name__ == "__main__":
    start_game()
