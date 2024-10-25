def calculate_ingredients(original_recipe, servings, desired_servings):
    scale_factor = desired_servings / servings
    scaled_recipe = {ingredient: amount * scale_factor for ingredient, amount in original_recipe.items()}
    return scaled_recipe

def main():
    # Original recipe for 4 servings
    original_recipe = {
        "Sugar (cups)": 1,
        "Flour (cups)": 2,
        "Butter (cups)": 0.5,
        "Eggs": 2
    }

    print("Original Recipe (4 servings):")
    for ingredient, amount in original_recipe.items():
        print(f"{ingredient}: {amount}")

    desired_servings = int(input("\nEnter the number of servings you want to make: "))
    scaled_recipe = calculate_ingredients(original_recipe, 4, desired_servings)

    print("\nScaled Recipe:")
    for ingredient, amount in scaled_recipe.items():
        print(f"{ingredient}: {amount:.2f}")

if __name__ == "__main__":
    main()
