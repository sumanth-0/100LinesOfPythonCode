# Crypto Price Tracker

A simple Python application built using Tkinter to track the live prices of Bitcoin (BTC) and Ethereum (ETH). The application fetches the current cryptocurrency prices from the CoinGecko API and updates them in real-time.

## Features

- Displays live cryptocurrency prices in USD.
- Shows the price change and percentage change for Bitcoin and Ethereum.
- Updates prices every 10 seconds.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Requests library

## Installation

1. Clone the repository or download the source code.
2. Make sure that Python 3 and pip are installed on your machine.
3. Install the Requests library if it is not already installed. You can do this using:

   ```bash
   pip install requests
   ```

4. Navigate to the folder where the code is saved using the terminal or command prompt.

## Usage

1. Run the application using Python:

   ```bash
   python app.py
   ```

2. The application window will appear displaying the live prices of Bitcoin and Ethereum.

## Code Overview

- **get_crypto_price(crypto_id)**: Function to fetch the current price of the cryptocurrency from the CoinGecko API.
- **update_prices()**: Function that updates the displayed prices and their corresponding changes in the GUI.
- The GUI is created using Tkinter, with a title, frames for each cryptocurrency, and labels for displaying the prices and changes.

## Example Screenshot

![Crypto Price Tracker Screenshot](./image.png)

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any enhancements or bug fixes.


## Acknowledgments

- [CoinGecko](https://www.coingecko.com) for providing the cryptocurrency data API.
```