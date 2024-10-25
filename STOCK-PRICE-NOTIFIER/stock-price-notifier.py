import requests
import time

def get_stock_price(symbol):
    # Using a free API (like Alpha Vantage, or you could use Yahoo Finance)
    api_key = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    try:
        latest_timestamp = list(data['Time Series (5min)'].keys())[0]
        latest_price = float(data['Time Series (5min)'][latest_timestamp]['1. open'])
        return latest_price
    except KeyError:
        print("Error fetching stock price. Please check the stock symbol or API key.")
        return None

def notify_user(message):
    print(message)  # Replace this with actual notification code (e.g., email, desktop notification)

def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ")
    threshold = float(input("Enter the price threshold: "))
    direction = input("Notify on 'above' or 'below' the threshold? ").strip().lower()
    
    if direction not in ['above', 'below']:
        print("Invalid input for direction. Please enter 'above' or 'below'.")
        return

    print("Monitoring stock price...")
    while True:
        current_price = get_stock_price(stock_symbol)
        if current_price is not None:
            print(f"Current price of {stock_symbol}: ${current_price:.2f}")
            if (direction == 'above' and current_price > threshold) or (direction == 'below' and current_price < threshold):
                notify_user(f"Stock price alert! {stock_symbol} is now ${current_price:.2f}.")
                break
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
