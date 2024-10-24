import tkinter as tk
import requests
import time

# Function to get the current cryptocurrency price
def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

# Function to update the prices in the GUI window
def update_prices():
    # Update Bitcoin price
    btc_price = get_crypto_price('bitcoin')
    btc_change = btc_price - old_prices['bitcoin']
    btc_percentage_change = (btc_change / old_prices['bitcoin']) * 100
    bitcoin_price_label.config(text=f"${btc_price:.2f}")
    bitcoin_change_label.config(text=f"Change: ${btc_change:.2f} ({btc_percentage_change:.2f}%)")
    bitcoin_change_label.config(fg="green" if btc_change >= 0 else "red")
    old_prices['bitcoin'] = btc_price

    # Update Ethereum price
    eth_price = get_crypto_price('ethereum')
    eth_change = eth_price - old_prices['ethereum']
    eth_percentage_change = (eth_change / old_prices['ethereum']) * 100
    ethereum_price_label.config(text=f"${eth_price:.2f}")
    ethereum_change_label.config(text=f"Change: ${eth_change:.2f} ({eth_percentage_change:.2f}%)")
    ethereum_change_label.config(fg="green" if eth_change >= 0 else "red")
    old_prices['ethereum'] = eth_price

    # Schedule the function to run again after the interval (in milliseconds)
    root.after(interval * 1000, update_prices)

# Setup the GUI window
root = tk.Tk()
root.title("Crypto Price Tracker")
root.configure(bg="black")

# Interval (time between updates in seconds)
interval = 10

# Initial prices setup
old_prices = {
    'bitcoin': get_crypto_price('bitcoin'),
    'ethereum': get_crypto_price('ethereum')
}

# Add a title label
title_label = tk.Label(root, text="Live Cryptocurrency Prices", font=("Arial", 24, "bold"), fg="green", bg="black")
title_label.pack(pady=20)

# Set up Bitcoin section
btc_frame = tk.Frame(root, bg="black")
btc_frame.pack(pady=10)

# Bitcoin labels
bitcoin_label = tk.Label(btc_frame, text="Bitcoin (BTC)", font=("Arial", 20), fg="white", bg="black")
bitcoin_label.pack()
bitcoin_price_label = tk.Label(btc_frame, text=f"${old_prices['bitcoin']:.2f}", font=("Arial", 20), fg="green", bg="black")
bitcoin_price_label.pack(pady=5)
bitcoin_change_label = tk.Label(btc_frame, text="Change: $0.00 (0.00%)", font=("Arial", 16), fg="green", bg="black")
bitcoin_change_label.pack()

# Set up Ethereum section
eth_frame = tk.Frame(root, bg="black")
eth_frame.pack(pady=10)

# Ethereum labels
ethereum_label = tk.Label(eth_frame, text="Ethereum (ETH)", font=("Arial", 20), fg="white", bg="black")
ethereum_label.pack()
ethereum_price_label = tk.Label(eth_frame, text=f"${old_prices['ethereum']:.2f}", font=("Arial", 20), fg="green", bg="black")
ethereum_price_label.pack(pady=5)
ethereum_change_label = tk.Label(eth_frame, text="Change: $0.00 (0.00%)", font=("Arial", 16), fg="green", bg="black")
ethereum_change_label.pack()

# Start the price update loop
root.after(interval * 1000, update_prices)

# Run the GUI loop
root.mainloop()
