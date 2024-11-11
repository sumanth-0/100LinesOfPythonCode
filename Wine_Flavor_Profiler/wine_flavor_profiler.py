
def get_wine_suggestions(taste_profile):
    # Example wine suggestions based on taste profile
    wine_suggestions = {
        "fruity": [
            "Moscato d'Asti - Sweet, fruity, and light.",
            "Chardonnay - Crisp and vibrant with notes of green apple."
        ],
        "earthy": [
            "Pinot Noir - Light-bodied with earthy undertones.",
            "Cabernet Sauvignon - Bold with a complex earthy flavor."
        ],
        "floral": [
            "Riesling - Delicate with floral aromas and hints of peach.",
            "Gewürztraminer - Fragrant with floral and spice notes."
        ],
        "spicy": [
            "Syrah - Bold with spicy notes and dark berry flavors.",
            "Zinfandel - Rich with a peppery finish."
        ]
    }

    # Return the wine suggestions based on the user's taste profile
    if taste_profile in wine_suggestions:
        return wine_suggestions[taste_profile]
    else:
        return ["Sorry, we don't have wine suggestions for this flavor profile."]

def get_user_input():
    # Input the user's flavor profile
    print("Select your preferred wine taste profile:")
    print("1. Fruity\n2. Earthy\n3. Floral\n4. Spicy")
    taste_choice = int(input("Enter choice (1-4): "))
    
    if taste_choice == 1:
        taste_profile = "fruity"
    elif taste_choice == 2:
        taste_profile = "earthy"
    elif taste_choice == 3:
        taste_profile = "floral"
    elif taste_choice == 4:
        taste_profile = "spicy"
    else:
        print("Invalid choice! Defaulting to 'fruity'.")
        taste_profile = "fruity"
    
    return taste_profile

def main():
    taste_profile = get_user_input()
    wine_suggestions = get_wine_suggestions(taste_profile)
    
    print("\nWine Suggestions based on your profile:")
    for wine in wine_suggestions:
        print(f"- {wine}")

# Run the program
if __name__ == "__main__":
    main()
