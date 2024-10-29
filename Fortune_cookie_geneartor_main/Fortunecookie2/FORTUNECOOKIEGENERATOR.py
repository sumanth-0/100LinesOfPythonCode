import random

# Fortune messages categorized by types
fortunes = {
    "humorous": [
        "Keep your friends close, but your snacks closer, {name}.",
        "{name}, a wise person once said: 'Never trust a fortune cookie.'",
        "Today is the perfect day to procrastinate, {name}.",
        "{name}, remember: a sense of humor is your best accessory!",
        "When life gives you lemons, {name}, trade them for cookies."
    ],
    "inspirational": [
        "An unexpected event will bring you good fortune, {name}!",
        "Happiness is on the horizon, {name}. Prepare to be delighted!",
        "Your potential is endless, {name}. Believe in yourself!",
        "You will achieve your goals if you start today, {name}!",
        "{name}, remember: Success is no accident. It's hard work and persistence!"
    ],
    "advice": [
        "{name}, remember: a watched pot never boils, but a watched cookie gets eaten!",
        "Start where you are, use what you have, and do what you can, {name}.",
        "Patience is a virtue, {name}. Good things are worth waiting for.",
        "The key to happiness, {name}, is keeping a smile on your face.",
        "Balance is key, {name}. Find joy in both work and play."
    ]
}

# Function to generate a random fortune
def generate_fortune(name, category):
    selected_fortunes = fortunes.get(category, [])
    if not selected_fortunes:
        return "Invalid category selected."
    fortune = random.choice(selected_fortunes)
    return fortune.format(name=name)

# Main program logic
def main():
    print("Welcome to the Fortune Cookie Generator!")
    name = input("Please enter your name: ").strip()

    # Ensure the user entered a name
    if not name:
        print("You need to enter a name to receive a fortune.")
        return

    print("\nChoose a fortune category:")
    print("1. Humorous")
    print("2. Inspirational")
    print("3. Life Advice")
    choice = input("Enter the number of your choice: ")

    # Map the user input to a category
    category_map = {
        "1": "humorous",
        "2": "inspirational",
        "3": "advice"
    }
    category = category_map.get(choice)

    # Generate and display the fortune
    if category:
        fortune_message = generate_fortune(name, category)
        print("\nYour Fortune Cookie says:")
        print(fortune_message)
    else:
        print("Invalid choice. Please run the program again and select a valid category.")

if __name__ == "__main__":
    main()
