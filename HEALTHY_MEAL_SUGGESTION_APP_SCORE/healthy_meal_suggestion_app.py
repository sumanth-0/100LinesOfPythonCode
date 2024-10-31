
import tkinter as tk
from tkinter import ttk

class MealSuggestionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthy Meal Suggestion App")
        self.ingredients_entry = tk.Entry(root, width=30)
        self.ingredients_entry.grid(row=0, column=1, padx=10, pady=10)
        self.suggest_button = tk.Button(root, text="Suggest Meal", command=self.suggest_meal)
        self.suggest_button.grid(row=1, column=1, padx=10, pady=10)
        self.result_label = tk.Label(root, text="", font=("Arial", 10))
        self.result_label.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Available Ingredients:").grid(row=0, column=0, padx=10, pady=10)

    def suggest_meal(self):
        ingredients = self.ingredients_entry.get().split(',')
        meal = self.generate_meal(ingredients)
        self.result_label.config(text=f"Suggested Meal: {meal}")

    def generate_meal(self, ingredients):
        # Mock meal suggestion based on ingredients
        if "chicken" in ingredients and "rice" in ingredients:
            return "Grilled chicken with steamed vegetables and brown rice"
        elif "tofu" in ingredients and "veggies" in ingredients:
            return "Stir-fried tofu with mixed vegetables"
        return "Mixed salad with a protein of choice"

if __name__ == "__main__":
    root = tk.Tk()
    app = MealSuggestionApp(root)
    root.mainloop()
