import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Lists of options for each course with calorie count (in tuples: (food, calories))
appetizers = [
    ("Spring Rolls", 200), ("Garlic Bread", 150), ("Bruschetta", 180), 
    ("Nachos", 300), ("Salad", 100), ("Mozzarella Sticks", 220),
    ("Stuffed Mushrooms", 160), ("Deviled Eggs", 120), ("Shrimp Cocktail", 150)
]
main_courses = [
    ("Spaghetti Bolognese", 600), ("Grilled Chicken", 400), ("Vegetable Stir Fry", 350), 
    ("Tacos", 450), ("Burger", 700), ("Sushi", 300), 
    ("Steak", 550), ("Pad Thai", 600), ("Pizza", 750), ("Burrito Bowl", 650)
]
desserts = [
    ("Ice Cream", 250), ("Brownie", 300), ("Fruit Salad", 100), 
    ("Cheesecake", 450), ("Panna Cotta", 350), ("Chocolate Cake", 400),
    ("Tiramisu", 450), ("Creme Brulee", 300), ("Macarons", 150), ("Pudding", 200)
]

# Get the minimum calorie value based on the lowest possible meal combination
min_calories = min(a[1] for a in appetizers) + min(m[1] for m in main_courses) + min(d[1] for d in desserts)

# Function to pick a meal within the calorie limit
def pick_meal(calorie_limit):
    while True:
        appetizer = random.choice(appetizers)
        main_course = random.choice(main_courses)
        dessert = random.choice(desserts)

        total_calories = appetizer[1] + main_course[1] + dessert[1]
        if total_calories <= calorie_limit:
            return appetizer, main_course, dessert, total_calories

# Main interaction with user
def meal_suggestion():
    # Get calorie limit from user
    while True:
        try:
            calorie_limit = int(input(f"Enter your desired daily calorie intake (minimum {min_calories} calories): "))
            if calorie_limit < min_calories:
                print(Fore.RED + f"Calorie intake too low! The minimum calorie intake is {min_calories} calories.")
            else:
                break
        except ValueError:
            print("Please enter a valid number!")

    # Pick a meal based on the calorie limit
    appetizer, main_course, dessert, total_calories = pick_meal(calorie_limit)

    # Display the meal details
    print(Fore.GREEN + Style.BRIGHT + "Today's Meal Suggestion".center(40, "="))
    print(Fore.CYAN + f"Appetizer: {appetizer[0]} - {appetizer[1]} calories")
    print(Fore.CYAN + f"Main Course: {main_course[0]} - {main_course[1]} calories")
    print(Fore.CYAN + f"Dessert: {dessert[0]} - {dessert[1]} calories")
    print(Fore.YELLOW + f"Total Calories: {total_calories}")
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.MAGENTA + Style.BRIGHT + "Enjoy your meal!".center(40))

# Run the meal suggestion tool
meal_suggestion()
