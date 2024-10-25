def calculate_discounted_price(price, discount_rate):
    discount_amount = price * (discount_rate / 100)
    final_price = price - discount_amount
    return final_price

def main():
    print("Welcome to the Discount Calculator!")
    price = float(input("Enter the item's price: $"))
    discount_rate = float(input("Enter the discount rate (%): "))

    final_price = calculate_discounted_price(price, discount_rate)
    print(f"The final price after a discount of {discount_rate}% is: ${final_price:.2f}")

if __name__ == "__main__":
    main()
