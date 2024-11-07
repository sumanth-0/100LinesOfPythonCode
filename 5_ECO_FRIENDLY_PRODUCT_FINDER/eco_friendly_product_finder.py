eco_products = {
    "Plastic Toothbrush": {"Alternative": "Bamboo Toothbrush", "Category": "Personal Care", "Link": "https://example.com/bamboo_toothbrush"},
    "Plastic Bag": {"Alternative": "Reusable Cloth Bag", "Category": "Grocery", "Link": "https://example.com/reusable_bag"},
    "Paper Towel": {"Alternative": "Reusable Cloth Towel", "Category": "Home", "Link": "https://example.com/cloth_towel"},
    "Plastic Straw": {"Alternative": "Metal Straw", "Category": "Dining", "Link": "https://example.com/metal_straw"},
}

def display_alternatives():
    print("\nEco-Friendly Product Finder\nDiscover sustainable swaps for everyday items.\n")
    for item, details in eco_products.items():
        print(f"Item: {item}")
        print(f"  Sustainable Alternative: {details['Alternative']}")
        print(f"  Category: {details['Category']}")
        print(f"  Find More Here: {details['Link']}\n")

def main():
    print("Welcome to the Eco-Friendly Product Finder!")
    while True:
        display_alternatives()
        choice = input("Would you like to see another list? (yes/no): ").strip().lower()
        if choice != "yes":
            break
    print("\nThank you for choosing eco-friendly options!")

if __name__ == "__main__":
    main()
