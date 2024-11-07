
from typing import List

# Sample recipes database
RECIPES = {
    "Vegan Salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "olive oil"],
        "category": "vegan"
    },
    "Low-Carb Omelette": {
        "ingredients": ["egg", "cheese", "spinach"],
        "category": "low-carb"
    },
    "Protein Smoothie": {
        "ingredients": ["banana", "spinach", "protein powder", "almond milk"],
        "category": "high-protein"
    },
    "Grilled Chicken": {
        "ingredients": ["chicken breast", "olive oil", "lemon"],
        "category": "high-protein"
    }
}

def suggest_recipes(available_ingredients: List[str], category: str = None) -> List[str]:
    suggestions = []
    for recipe, details in RECIPES.items():
        # Check if recipe matches the specified category (if provided)
        if category and details["category"] != category:
            continue
        # Suggest recipe if all its ingredients are available
        if all(item in available_ingredients for item in details["ingredients"]):
            suggestions.append(recipe)
    return suggestions

def main():
    print("Healthy Recipe Suggestion\n")
    ingredients = input("Enter ingredients you have (comma-separated): ").strip().split(", ")
    category = input("Enter dietary preference (e.g., vegan, low-carb, high-protein) or leave blank: ").strip().lower()
    
    recipe_suggestions = suggest_recipes(ingredients, category)
    if recipe_suggestions:
        print("\nRecipes you can make:")
        for recipe in recipe_suggestions:
            print(f"- {recipe}")
    else:
        print("No recipes found with the current ingredients and preferences.")

if __name__ == "__main__":
    main()
