# 🪙 Crypto Price Notifier

A simple, command-line tool to display live prices of selected cryptocurrencies directly in your terminal. This script uses the CoinGecko API for real-time data.

## ✨ Features

-   **Live Price Tracking**: Fetches and displays the latest prices.
-   **Customizable Coin List**: Easily edit a Python list to track your favorite coins.
-   **Multiple Currencies**: Supports displaying prices in various fiat currencies (USD, EUR, INR, etc.).
-   **Auto-Refresh**: Automatically updates the prices at a configurable interval.
-   **Clean Interface**: A minimal and readable display that clears the screen on each update.

## ⚙️ Setup and Installation

1.  **Prerequisites**:
    -   Python 3.x
    -   `pip` (Python package installer)

2.  **Navigate to the project directory**:
    ```bash
    cd #1093_CRYPTO_PRICE_NOTIFIER
    ```

3.  **Install required packages**:
    This project requires the `requests` library.
    ```bash
    pip install requests
    ```

## 🚀 Usage

To run the script, execute the following command in your terminal:

```bash
python main.py
```

The script will start fetching data and display the prices. It will refresh automatically. To stop the script, press `Ctrl + C`.

## 🔧 Configuration

You can easily customize the script by editing the configuration section at the top of the `main.py` file.

-   **`COINS_TO_TRACK`**: A Python list of coin IDs from CoinGecko.
    -   *Example*: `["bitcoin", "ethereum", "dogecoin"]`
-   **`VS_CURRENCY`**: The fiat currency for price display.
    -   *Example*: `"usd"`, `"eur"`, `"inr"`
-   **`REFRESH_RATE`**: Time in seconds between each price update.
    -   *Example*: `60` (for one minute)

## 📸 Demo Output

```text
--- Live Crypto Prices ---
Last updated: 2025-10-18 17:30:57

Bitcoin         $65,123.45
Ethereum        $4,321.90
Solana          $150.77

Refreshing in 30 seconds...
```