class Stock:
    """Class representing a stock with its details."""
    def __init__(self, symbol, purchase_price, quantity):
        self.symbol = symbol
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.current_price = purchase_price  # Assume initial current price is the purchase price

    def update_current_price(self, new_price):
        """Update the current price of the stock."""
        self.current_price = new_price

    def calculate_gain_loss(self):
        """Calculate the gain or loss for the stock."""
        return (self.current_price - self.purchase_price) * self.quantity


def main():
    """Run the stock portfolio tracker."""
    portfolio = []
    total_gain_loss = 0

    print("Welcome to the Stock Portfolio Tracker!\n")
    
    while True:
        symbol = input("Enter stock symbol (or type 'exit' to finish): ")
        if symbol.lower() == 'exit':
            break
        
        purchase_price = float(input(f"Enter purchase price for {symbol}: "))
        quantity = int(input(f"Enter quantity for {symbol}: "))
        
        stock = Stock(symbol, purchase_price, quantity)
        portfolio.append(stock)

    print("\nUpdating current prices...")
    for stock in portfolio:
        current_price = float(input(f"Enter current price for {stock.symbol}: "))
        stock.update_current_price(current_price)
        gain_loss = stock.calculate_gain_loss()
        total_gain_loss += gain_loss
        print(f"{stock.symbol}: Gain/Loss = ${gain_loss:.2f}")

    print(f"\nTotal Gain/Loss in Portfolio: ${total_gain_loss:.2f}")


if __name__ == "__main__":
    main()
