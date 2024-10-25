import requests

def find_recipes(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['meals']:
            print(f"\nRecipes found with ingredient '{ingredient}':")
            for i, meal in enumerate(data['meals'], start=1):
                print(f"{i}. {meal['strMeal']} - Link: https://www.themealdb.com/meal/{meal['idMeal']}")
        else:
            print(f"No recipes found with ingredient '{ingredient}'. Try something else.")
    else:
        print("Error fetching recipes:", response.status_code)

# User input for ingredient
user_ingredient = input("Enter a single ingredient: ")
find_recipes(user_ingredient)
