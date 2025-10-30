# Shopping Bill with Discount
# Student Name: Satyajeet Ravan
# Registration No.: 241080057

def shopping_bill():
    items = {}
    n = int(input("Enter number of items: "))

    for i in range(n):
        name = input(f"Enter name of item {i+1}: ").strip().upper()
        price = float(input(f"Enter price of {name}: "))
        items[name] = price

    total = sum(items.values())
    expensive_item = max(items, key=items.get)

    if total > 500:
        discount = total * 0.10
        total_after_discount = total - discount
    else:
        discount = 0
        total_after_discount = total

    print("\n----- BILL -----")
    for item, price in items.items():
        print(f"{item}: ₹{price:.2f}")
    print(f"Total before discount: ₹{total:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Total after discount: ₹{total_after_discount:.2f}")
    print(f"Most expensive item: {expensive_item} (₹{items[expensive_item]:.2f})")

shopping_bill()
