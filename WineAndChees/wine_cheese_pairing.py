

import random

def wine_cheese_pairing():
    """Suggests wine and cheese pairings."""

    # Wine and cheese pairings with descriptions
    pairings = {
        "Camembert": ["Chardonnay", "Pinot Noir"],
        "Brie": ["Champagne", "Sauvignon Blanc"],
        "Gouda": ["Riesling", "Pinot Gris"],
        "Cheddar": ["Cabernet Sauvignon", "Zinfandel"],
        "Blue Cheese": ["Port", "Sauternes"]
    }

    # Randomly select a cheese
    cheese = random.choice(list(pairings.keys()))

    # Get suggested wine pairings
    suggested_wines = pairings[cheese]

    print(f"**Cheese:** {cheese}")
    print("Suggested Wine Pairings:")
    for wine in suggested_wines:
        print(f"- {wine}")

    # Add more detailed descriptions and recommendations as needed
    # ... (e.g., flavor profiles, body, acidity)

if __name__ == "__main__":
    wine_cheese_pairing()
