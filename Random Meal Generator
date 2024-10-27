import random

def select_meal():
    appetizers = [
        "Samosa",
        "Dhokla",
        "Aloo Tikki",
        "Spring Rolls",
        "Pakora"
    ]

    main_courses = [
        "Paneer Butter Masala",
        "Dal Makhani",
        "Mix Veg",
        "Aloo Gobi",
        "Butter Chicken"
    ]

    desserts = [
        "Kheer",
        "Ladoo",
        "Rasmalai",
        "Cheesecake",
        "Gulab Jamun"
    ]

    selected_appetizer = random.choice(appetizers)
    selected_main_course = random.choice(main_courses)
    selected_dessert = random.choice(desserts)

    meal_plan = {
        "Appetizer": selected_appetizer,
        "Main Course": selected_main_course,
        "Dessert": selected_dessert
    }

    return meal_plan

if __name__ == "__main__":
    meal = select_meal()
    print("Today's Meal Selection:")
    for course, dish in meal.items():
        print(f"{course}: {dish}")
