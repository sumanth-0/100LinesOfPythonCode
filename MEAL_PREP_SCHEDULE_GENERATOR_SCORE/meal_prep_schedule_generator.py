
def create_meal_schedule(recipes):
    schedule = {}
    for day, recipe in recipes.items():
        prep_time = recipe['prep_time']
        cook_time = recipe['cook_time']
        total_time = prep_time + cook_time
        schedule[day] = {
            'Recipe': recipe['name'],
            'Total Time (min)': total_time,
            'Prep Time (min)': prep_time,
            'Cook Time (min)': cook_time
        }
    return schedule

def main():
    print("Welcome to the Meal Prep Schedule Generator!")
    recipes = {}
    
    num_recipes = int(input("How many recipes do you want to input? "))
    for _ in range(num_recipes):
        name = input("Enter recipe name: ")
        prep_time = int(input("Enter prep time in minutes: "))
        cook_time = int(input("Enter cook time in minutes: "))
        day = input("Enter day for the recipe: ")
        recipes[day] = {'name': name, 'prep_time': prep_time, 'cook_time': cook_time}

    schedule = create_meal_schedule(recipes)
    
    print("\nYour Meal Prep Schedule:")
    for day, details in schedule.items():
        print(f"{day}: {details['Recipe']} (Prep: {details['Prep Time (min)']} min, Cook: {details['Cook Time (min)']} min, Total: {details['Total Time (min)']} min)")

if __name__ == "__main__":
    main()
