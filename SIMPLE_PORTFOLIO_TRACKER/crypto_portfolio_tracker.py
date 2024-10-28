import requests

class CryptoPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_crypto(self, symbol, amount):
        """Add cryptocurrency to the portfolio."""
        self.portfolio[symbol] = amount

    def remove_crypto(self, symbol):
        """Remove cryptocurrency from the portfolio."""
        if symbol in self.portfolio:
            del self.portfolio[symbol]

    def get_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        total_value = 0
        for symbol, amount in self.portfolio.items():
            price = self.get_crypto_price(symbol)
            total_value += price * amount
        return total_value

    def get_crypto_price(self, symbol):
        """Get the current price of the cryptocurrency."""
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        return data[symbol]['usd'] if symbol in data else 0

    def display_portfolio(self):
        """Display the user's cryptocurrency portfolio."""
        print("Your Cryptocurrency Portfolio:")
        for symbol, amount in self.portfolio.items():
            price = self.get_crypto_price(symbol)
            value = price * amount
            print(f"{symbol.upper()}: Amount: {amount}, Current Price: ${price:.2f}, Total Value: ${value:.2f}")

def main():
    portfolio = CryptoPortfolio()
    
    # User input for adding cryptocurrencies
    while True:
        action = input("Do you want to add, remove, or view your portfolio? (add/remove/view/exit): ").lower()
        if action == 'add':
            symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin): ").lower()
            amount = float(input(f"Enter the amount of {symbol} you own: "))
            portfolio.add_crypto(symbol, amount)
        elif action == 'remove':
            symbol = input("Enter the cryptocurrency symbol to remove: ").lower()
            portfolio.remove_crypto(symbol)
        elif action == 'view':
            portfolio.display_portfolio()
            total_value = portfolio.get_portfolio_value()
            print(f"Total Portfolio Value: ${total_value:.2f}")
        elif action == 'exit':
            print("Exiting the portfolio tracker.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
