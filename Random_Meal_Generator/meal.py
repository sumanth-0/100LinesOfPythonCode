import random
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Lists of options for each course
appetizers = [
    "Spring Rolls", "Garlic Bread", "Bruschetta", "Nachos", "Salad",
    "Mozzarella Sticks", "Stuffed Mushrooms", "Deviled Eggs", "Shrimp Cocktail"
]
main_courses = [
    "Spaghetti Bolognese", "Grilled Chicken", "Vegetable Stir Fry", "Tacos",
    "Burger", "Sushi", "Steak", "Pad Thai", "Pizza", "Burrito Bowl"
]
desserts = [
    "Ice Cream", "Brownie", "Fruit Salad", "Cheesecake", "Panna Cotta",
    "Chocolate Cake", "Tiramisu", "Creme Brulee", "Macarons", "Pudding"
]

# Function to pick a random item from each list
def pick_meal():
    appetizer = random.choice(appetizers)
    main_course = random.choice(main_courses)
    dessert = random.choice(desserts)
    return appetizer, main_course, dessert

# Display the randomly selected meal with some color and styling
appetizer, main_course, dessert = pick_meal()

print(Fore.GREEN + Style.BRIGHT + "Today's Meal Suggestion".center(40, "="))
print(Fore.CYAN + "Appetizer:" + Fore.YELLOW + f" {appetizer}")
print(Fore.CYAN + "Main Course:" + Fore.YELLOW + f" {main_course}")
print(Fore.CYAN + "Dessert:" + Fore.YELLOW + f" {dessert}")
print(Fore.GREEN + Style.BRIGHT + "=" * 40)
print(Fore.MAGENTA + Style.BRIGHT + "Enjoy your meal!".center(40))
