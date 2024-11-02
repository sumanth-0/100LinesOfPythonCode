
import datetime
import random
import tkinter as tk

seasonal_recipes = {
    "spring": [
        "Asparagus and Lemon Pasta",
        "Fresh Herb and Goat Cheese Salad",
        "Strawberry Spinach Smoothie",
    ],
    "summer": [
        "Grilled Peach and Burrata Salad",
        "Chilled Cucumber Soup",
        "Mango Avocado Salsa with Chips",
    ],
    "fall": [
        "Pumpkin Risotto",
        "Butternut Squash Soup",
        "Apple Cinnamon Oatmeal",
    ],
    "winter": [
        "Root Vegetable Stew",
        "Warm Lentil Salad with Roasted Beets",
        "Spiced Hot Chocolate",
    ]
}

class RecipeFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Seasonal Recipe Finder")
        
        tk.Label(root, text="Get a recipe idea for this season!", font=("Arial", 12)).pack(pady=10)
        
        self.recipe_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=300)
        self.recipe_label.pack(pady=10)
        
        self.generate_button = tk.Button(root, text="Find Recipe", command=self.show_seasonal_recipe)
        self.generate_button.pack(pady=10)
    
    def current_season(self):
        month = datetime.datetime.now().month
        if 3 <= month <= 5:
            return "spring"
        elif 6 <= month <= 8:
            return "summer"
        elif 9 <= month <= 11:
            return "fall"
        else:
            return "winter"
    
    def show_seasonal_recipe(self):
        season = self.current_season()
        recipe = random.choice(seasonal_recipes[season])
        self.recipe_label.config(text=f"Season: {season.capitalize()}\nRecipe: {recipe}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeFinder(root)
    root.mainloop()
