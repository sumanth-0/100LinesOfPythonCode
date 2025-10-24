import random

# Lists for generating taglines
adjectives = [
    "Revolutionary", "Ultimate", "Bold", "Epic", "Sleek", "Dynamic", "Vibrant",
    "Unleashed", "Premier", "Elite", "Radiant", "Swift", "Empowered", "Luxe",
    "Intrepid", "Zenith", "Pinnacle", "Audacious", "Celestial", "Fierce",
    "Harmonic", "Infinite", "Jubilant", "Kinetic", "Luminous", "Majestic"
]

nouns = [
    "Innovation", "Experience", "Journey", "Edge", "Fusion", "Spark", "Pulse",
    "Horizon", "Vanguard", "Essence", "Catalyst", "Synergy", "Apex", "Bliss",
    "Momentum", "Radiance", "Summit", "Thrive", "Unleash", "Verve", "Wonder",
    "Zen", "Quest", "Realm", "Surge", "Tide", "Utopia", "Vortex"
]

templates = [
    "{adj} {noun}: Redefine {product}",
    "Unlock the {adj} {noun} with {product}",
    "Experience {adj} {noun} in Every {product}",
    "{product}: The {adj} {noun} Awaits",
    "Ignite Your {adj} {noun} – {product} Edition",
    "Discover {adj} {noun} Through {product}",
    "{adj} {noun} Redefined by {product}"
]

def generate_taglines(product, num_taglines=5):
    """Generate catchy taglines using adj + noun templates."""
    taglines = []
    for _ in range(num_taglines):
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        template = random.choice(templates)
        tagline = template.format(adj=adj, noun=noun, product=product)
        taglines.append(tagline)
    return taglines

def main():
    print("Catchy Tagline Generator")
    product = input("Enter product name (e.g., 'Wireless Earbuds'): ").strip()
    if not product:
        product = "Your Product"
    
    try:
        num = int(input("Number of taglines (default 5): ").strip() or "5")
    except ValueError:
        num = 5
    
    taglines = generate_taglines(product, num)
    print(f"\nGenerated taglines for '{product}':\n")
    for i, tagline in enumerate(taglines, 1):
        print(f"{i}. {tagline}")
        print()

if __name__ == "__main__":
    main()
