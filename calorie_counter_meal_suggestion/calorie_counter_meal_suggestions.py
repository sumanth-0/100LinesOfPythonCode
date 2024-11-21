# calorie_counter_meal_suggestions.py

def calculate_remaining_calories(goal, consumed):
    """Calculate remaining calories to reach the daily goal."""
    return max(0, goal - consumed)

def suggest_meals(remaining_calories):
    """Suggest meals based on remaining calories."""
    meal_suggestions = {
        range(0, 100): ["A small fruit like an apple or a handful of almonds."],
        range(100, 300): ["A light salad or a small sandwich."],
        range(300, 500): ["A bowl of soup or a plate of pasta."],
        range(500, 800): ["Grilled chicken with vegetables or a hearty stir-fry."],
        range(800, 1200): ["A full meal with rice, beans, and grilled protein."],
    }
    for calorie_range, suggestions in meal_suggestions.items():
        if remaining_calories in calorie_range:
            return suggestions
    return ["You've hit your goal! Consider a light snack or nothing more."]

def main():
    print("Welcome to the Calorie Counter!")
    daily_goal = int(input("Enter your daily calorie goal: "))
    consumed_calories = 0

    while True:
        print(f"\nCurrent calorie intake: {consumed_calories}/{daily_goal}")
        remaining = calculate_remaining_calories(daily_goal, consumed_calories)
        if remaining == 0:
            print("Congratulations! You've met your calorie goal for the day.")
            break

        print(f"Calories remaining: {remaining}")
        action = input("Choose an action - Add meal (a) / View suggestions (s) / Exit (e): ").lower()

        if action == "a":
            try:
                meal_calories = int(input("Enter calories for the meal: "))
                consumed_calories += meal_calories
            except ValueError:
                print("Please enter a valid number.")
        elif action == "s":
            print("\nMeal suggestions:")
            for suggestion in suggest_meals(remaining):
                print(f"- {suggestion}")
        elif action == "e":
            print("Goodbye! Stay healthy!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
