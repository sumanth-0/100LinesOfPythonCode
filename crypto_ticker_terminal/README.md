# Crypto Ticker Terminal

A simple Python CLI tool to fetch and display real-time cryptocurrency prices with colorful terminal output.

## Features

- 🚀 Real-time cryptocurrency price data from CoinGecko API
- 🎨 Color-coded terminal output using ANSI colors
- 📊 Display price, 24h change, market cap, and trading volume
- 💰 Support for popular cryptocurrencies (BTC, ETH, ADA, SOL, XRP, DOGE, DOT, MATIC)
- 🌍 Multi-currency support (USD, EUR, etc.)
- ⚡ Fast and lightweight (under 100 lines of code)

## Requirements

```bash
pip install requests
```

## Usage

Basic usage with default currency (USD):
```bash
python crypto_ticker_terminal.py <cryptocurrency>
```

With custom currency:
```bash
python crypto_ticker_terminal.py <cryptocurrency> <currency>
```

## Examples

Fetch Bitcoin price in USD:
```bash
python crypto_ticker_terminal.py btc
```

Fetch Ethereum price in EUR:
```bash
python crypto_ticker_terminal.py eth eur
```

Fetch Solana price:
```bash
python crypto_ticker_terminal.py sol
```

## Supported Cryptocurrencies

- Bitcoin (btc, bitcoin)
- Ethereum (eth, ethereum)
- Cardano (ada, cardano)
- Solana (sol, solana)
- Ripple (xrp, ripple)
- Dogecoin (doge, dogecoin)
- Polkadot (dot, polkadot)
- Polygon (matic, polygon)

You can also use the full CoinGecko ID for any cryptocurrency.

## Output Information

The tool displays:
- **Current Price**: Real-time price in selected currency
- **24h Change**: Percentage change in the last 24 hours (color-coded: green for positive, red for negative)
- **Market Cap**: Total market capitalization
- **24h Volume**: Trading volume in the last 24 hours

## API

This tool uses the free [CoinGecko API](https://www.coingecko.com/en/api) which doesn't require an API key.

## Contributing

Feel free to open issues or submit pull requests to improve this tool!

## License

MIT License - Feel free to use this project for learning and development.

## Author

Created for issue #653 - Part of the 100LinesOfPythonCode project.
