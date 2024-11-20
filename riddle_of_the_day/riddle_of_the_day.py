# riddle_of_the_day.py

import json
import datetime
import random

RIDDLES_FILE = "riddles.json"
ANSWER_FILE = "current_answer.json"

def load_riddles():
    """Load riddles from a file."""
    if not os.path.exists(RIDDLES_FILE):
        with open(RIDDLES_FILE, "w") as file:
            json.dump([
                {"question": "What has to be broken before you can use it?", "answer": "An egg"},
                {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "An echo"},
                {"question": "The more of me you take, the more you leave behind. What am I?", "answer": "Footsteps"}
            ], file)
    with open(RIDDLES_FILE, "r") as file:
        return json.load(file)

def save_current_answer(riddle):
    """Save the current riddle's answer for future reference."""
    with open(ANSWER_FILE, "w") as file:
        json.dump(riddle, file)

def load_current_answer():
    """Load the current riddle's answer."""
    if os.path.exists(ANSWER_FILE):
        with open(ANSWER_FILE, "r") as file:
            return json.load(file)
    return None

def get_daily_riddle():
    """Pick and display a riddle for the day."""
    riddles = load_riddles()
    today = datetime.date.today()
    random.seed(today.toordinal())  # Ensure same riddle every day
    riddle = random.choice(riddles)
    save_current_answer(riddle)
    return riddle["question"]

def reveal_answer():
    """Reveal the answer to yesterday's riddle."""
    riddle = load_current_answer()
    if riddle:
        return f"Yesterday's riddle answer: {riddle['answer']}"
    return "No riddle was set for yesterday."

def main():
    print("Welcome to the Riddle of the Day!")
    while True:
        print("\nOptions: [1] Get Today's Riddle  [2] Reveal Yesterday's Answer  [3] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"\nToday's Riddle: {get_daily_riddle()}")
        elif choice == "2":
            print(reveal_answer())
        elif choice == "3":
            print("Goodbye! See you tomorrow for more riddles!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
