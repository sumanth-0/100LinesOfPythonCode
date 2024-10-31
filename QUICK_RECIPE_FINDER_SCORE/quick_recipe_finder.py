
import tkinter as tk
from tkinter import messagebox

class RecipeFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Recipe Finder")
        
        tk.Label(root, text="Enter Ingredients (comma-separated):").pack(pady=10)
        self.ingredient_entry = tk.Entry(root, width=50)
        self.ingredient_entry.pack(pady=5)
        
        find_button = tk.Button(root, text="Find Recipes", command=self.find_recipe)
        find_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.result_label.pack(pady=10)

    def find_recipe(self):
        ingredients = self.ingredient_entry.get().split(',')
        # Placeholder logic for demonstration
        recipe = f"With {', '.join(ingredients)}, you can make: Simple Pasta, Veggie Stir-fry."
        self.result_label.config(text=recipe)
        self.ingredient_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeFinder(root)
    root.mainloop()
