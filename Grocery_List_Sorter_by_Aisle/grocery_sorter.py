def sort_grocery_list(grocery_items):
    """Sort grocery items by their corresponding aisles."""
    aisle_categories = {
        'Produce': [],
        'Dairy': [],
        'Meat': [],
        'Bakery': [],
        'Canned Goods': [],
        'Frozen Foods': [],
        'Snacks': [],
        'Beverages': [],
    }

    for item in grocery_items:
        category = item['category']
        if category in aisle_categories:
            aisle_categories[category].append(item['name'])

    return aisle_categories

def main():
    grocery_list = []
    print("Enter grocery items. Type 'done' when finished.")

    while True:
        item_name = input("Enter item name (or 'done'): ")
        if item_name.lower() == 'done':
            break
        category = input("Enter category (Produce, Dairy, Meat, Bakery, Canned Goods, Frozen Foods, Snacks, Beverages): ")
        
        grocery_list.append({'name': item_name, 'category': category})

    sorted_list = sort_grocery_list(grocery_list)

    print("\nSorted Grocery List:")
    for aisle, items in sorted_list.items():
        if items:  # Only print aisles with items
            print(f"{aisle}: {', '.join(items)}")

if __name__ == "__main__":
    main()
