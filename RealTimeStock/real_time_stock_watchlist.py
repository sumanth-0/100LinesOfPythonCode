# real_time_stock_watchlist.py
import requests
import time

# Function to get the current stock price
def get_stock_price(stock_symbol):
    url = f'https://api.stockapi.com/v3/quote/{stock_symbol}?apikey=YOUR_API_KEY'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]['price']  # Return the stock price
    else:
        print("Error fetching stock data")
        return None

# Function to track stocks and notify when a price threshold is reached
def track_stock(stock_symbol, target_price):
    print(f"Tracking {stock_symbol}. Notifications will trigger when the price reaches {target_price}.")
    
    while True:
        current_price = get_stock_price(stock_symbol)
        
        if current_price is not None:
            print(f"Current price of {stock_symbol}: ${current_price}")
            
            if current_price >= target_price:
                print(f"ALERT! {stock_symbol} has reached or exceeded your target price of ${target_price}.")
                break  # Stop tracking when target price is reached
        else:
            print("Could not retrieve stock data.")
        
        # Wait for 60 seconds before checking again
        time.sleep(60)

# Main function to get user input and start tracking
def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ").upper()
    target_price = float(input("Enter your target price for this stock: $"))
    
    track_stock(stock_symbol, target_price)

# Run the program
if __name__ == "__main__":
    main()
