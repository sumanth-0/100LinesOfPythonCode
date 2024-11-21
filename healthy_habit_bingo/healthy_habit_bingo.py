# healthy_habit_bingo.py

import random

HABITS = [
    "Drink 8 glasses of water",
    "Take a 10-minute walk",
    "Stretch for 5 minutes",
    "Eat a fruit or vegetable snack",
    "Meditate for 5 minutes",
    "Write in a gratitude journal",
    "Take a screen break for 15 minutes",
    "Sleep for 7-8 hours",
    "Do 10 push-ups or sit-ups",
    "Read for 10 minutes",
    "Avoid sugary drinks for a day",
    "Compliment someone",
    "Plan tomorrow's tasks",
    "Cook a healthy meal",
    "Practice deep breathing exercises",
    "Declutter a small area",
    "Spend time outdoors",
    "Limit social media for 1 hour",
    "Try a new recipe",
    "Call or text a friend"
]

def generate_bingo_board():
    """Generate a randomized 5x5 bingo board of healthy habits."""
    selected_habits = random.sample(HABITS, 25)
    return [selected_habits[i:i + 5] for i in range(0, 25, 5)]

def display_board(board):
    """Display the bingo board in a user-friendly format."""
    print("\nHealthy Habit Bingo Board:")
    print("-" * 33)
    for row in board:
        print("| " + " | ".join(f"{habit[:12]:12}" for habit in row) + " |")
        print("-" * 33)

def mark_habit(board, habit):
    """Mark a habit as completed on the bingo board."""
    for i, row in enumerate(board):
        if habit in row:
            board[i][row.index(habit)] = "✔ " + habit
            print(f"\nMarked '{habit}' as completed!")
            return
    print("\nHabit not found on the board. Please check your input.")

def main():
    """Main function to play Healthy Habit Bingo."""
    print("Welcome to Healthy Habit Bingo!")
    bingo_board = generate_bingo_board()
    display_board(bingo_board)

    while True:
        habit = input("\nEnter a habit to mark as completed (or type 'exit' to quit): ").strip()
        if habit.lower() == "exit":
            print("\nThanks for playing Healthy Habit Bingo! Stay healthy!")
            break
        mark_habit(bingo_board, habit)
        display_board(bingo_board)

if __name__ == "__main__":
    main()
