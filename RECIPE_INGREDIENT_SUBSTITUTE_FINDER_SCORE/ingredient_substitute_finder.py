
import tkinter as tk

class IngredientSubstituteFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Ingredient Substitute Finder")
        self.ingredient_entry = tk.Entry(root, width=20)
        self.ingredient_entry.grid(row=0, column=1, padx=10, pady=10)
        self.submit_button = tk.Button(root, text="Find Substitute", command=self.find_substitute)
        self.submit_button.grid(row=1, column=1, padx=10, pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Ingredient:").grid(row=0, column=0, padx=10, pady=10)

    def find_substitute(self):
        ingredient = self.ingredient_entry.get()
        substitutes = self.get_substitute(ingredient)
        self.result_label.config(text=f"Substitute for {ingredient}: {substitutes}")

    def get_substitute(self, ingredient):
        # Simplified substitute suggestions
        substitutes = {
            "milk": "Almond milk, soy milk, coconut milk",
            "butter": "Coconut oil, olive oil, applesauce",
            "egg": "Flaxseed meal, chia seeds, applesauce",
        }
        return substitutes.get(ingredient.lower(), "No substitute found")

if __name__ == "__main__":
    root = tk.Tk()
    app = IngredientSubstituteFinder(root)
    root.mainloop()
