#!/usr/bin/env python3
"""
Vegan Recipe Randomizer - Generates random vegan recipes for plant-based meal inspiration.
For the days when you want plants, but make it fancy!
"""
import random
from typing import Dict, List

# Pre-set collection of delicious vegan recipes
VEGAN_RECIPES = [
    {"name": "Creamy Coconut Curry", "ingredients": ["coconut milk", "chickpeas", "spinach", "curry paste", "rice"], "time": "30 min", "difficulty": "Easy"},
    {"name": "Buddha Bowl Supreme", "ingredients": ["quinoa", "roasted chickpeas", "avocado", "tahini", "kale"], "time": "25 min", "difficulty": "Easy"},
    {"name": "Spicy Black Bean Tacos", "ingredients": ["black beans", "corn tortillas", "avocado", "salsa", "cilantro"], "time": "20 min", "difficulty": "Easy"},
    {"name": "Mushroom Stroganoff", "ingredients": ["mushrooms", "cashew cream", "pasta", "garlic", "thyme"], "time": "35 min", "difficulty": "Medium"},
    {"name": "Thai Peanut Noodles", "ingredients": ["rice noodles", "peanut butter", "vegetables", "soy sauce", "lime"], "time": "20 min", "difficulty": "Easy"},
    {"name": "Lentil Shepherd's Pie", "ingredients": ["lentils", "mashed potatoes", "carrots", "peas", "vegetable broth"], "time": "50 min", "difficulty": "Medium"},
    {"name": "Vegan Pad Thai", "ingredients": ["rice noodles", "tofu", "peanuts", "bean sprouts", "tamarind sauce"], "time": "25 min", "difficulty": "Medium"},
    {"name": "Mediterranean Hummus Bowl", "ingredients": ["hummus", "quinoa", "cucumber", "tomatoes", "olives"], "time": "15 min", "difficulty": "Easy"},
    {"name": "Sweet Potato Buddha Bowl", "ingredients": ["sweet potato", "chickpeas", "quinoa", "tahini", "spinach"], "time": "30 min", "difficulty": "Easy"},
    {"name": "Vegan Chili", "ingredients": ["kidney beans", "tomatoes", "bell peppers", "corn", "chili powder"], "time": "40 min", "difficulty": "Easy"}
]

def display_recipe(recipe: Dict) -> None:
    """Display a recipe in a formatted manner."""
    print(f"\n{'='*50}\n🌱 {recipe['name']} 🌱\n{'='*50}")
    print(f"⏱️  Time: {recipe['time']} | 📊 Difficulty: {recipe['difficulty']}")
    print(f"\n🥗 Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"   • {ingredient}")
    print("="*50 + "\n")

def get_random_recipe() -> Dict:
    """Return a random vegan recipe from the collection."""
    return random.choice(VEGAN_RECIPES)

def get_recipes_by_difficulty(difficulty: str) -> List[Dict]:
    """Filter recipes by difficulty level."""
    return [r for r in VEGAN_RECIPES if r['difficulty'].lower() == difficulty.lower()]

def get_quick_recipes(max_time: int = 25) -> List[Dict]:
    """Get recipes that can be made within specified time."""
    return [r for r in VEGAN_RECIPES if int(r['time'].split()[0]) <= max_time]

def main():
    """Main function to run the Vegan Recipe Randomizer."""
    print("\n🌿 Welcome to the Vegan Recipe Randomizer! 🌿")
    print("For the days when you want plants, but make it fancy!\n")
    
    while True:
        print("\nOptions:")
        print("1. Random recipe")
        print("2. Random easy recipe")
        print("3. Random medium recipe")
        print("4. Quick recipe (<25 min)")
        print("5. Show all recipes")
        print("6. Exit")
        
        choice = input("\nChoice (1-6): ").strip()
        
        if choice == '1':
            display_recipe(get_random_recipe())
        elif choice == '2':
            easy = get_recipes_by_difficulty('Easy')
            if easy: display_recipe(random.choice(easy))
        elif choice == '3':
            medium = get_recipes_by_difficulty('Medium')
            if medium: display_recipe(random.choice(medium))
        elif choice == '4':
            quick = get_quick_recipes()
            if quick: display_recipe(random.choice(quick))
            else: print("\n❌ No quick recipes found.")
        elif choice == '5':
            print(f"\n📋 Total Recipes: {len(VEGAN_RECIPES)}")
            for i, r in enumerate(VEGAN_RECIPES, 1):
                print(f"{i}. {r['name']} ({r['time']}, {r['difficulty']})")
        elif choice == '6':
            print("\n🌱 Happy cooking! Stay plant-powered! 🌱\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
