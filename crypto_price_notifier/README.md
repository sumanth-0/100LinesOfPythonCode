# Crypto Price Notifier CLI

A command-line tool to monitor cryptocurrency prices and send notifications when price thresholds are reached. Uses the [CoinGecko API](https://www.coingecko.com/en/api) which is free and requires no API key.

## Features

- 📊 Real-time cryptocurrency price monitoring
- 🔔 Price threshold notifications
- 📈 24-hour price change tracking
- 💰 Market cap information
- 📝 Price history logging
- 🎨 Colored terminal output
- ⚡ Simple CLI interface

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/crypto_price_notifier
```

2. Install dependencies:
```bash
pip install requests
```

## Usage

### Basic Usage

Check the current price of Bitcoin (one-time check):
```bash
python crypto_price_notifier.py --crypto bitcoin --once
```

### Monitor with Alerts

Monitor Ethereum and alert when price goes above $3000:
```bash
python crypto_price_notifier.py --crypto ethereum --target 3000 --condition above
```

Monitor Bitcoin and alert when price drops below $40000:
```bash
python crypto_price_notifier.py --crypto bitcoin --target 40000 --condition below
```

### Continuous Monitoring

Monitor Dogecoin every 30 seconds:
```bash
python crypto_price_notifier.py --crypto dogecoin --interval 30
```

Monitor for a specific duration (e.g., 3600 seconds = 1 hour):
```bash
python crypto_price_notifier.py --crypto ethereum --interval 60 --duration 3600
```

## Command-Line Arguments

| Argument | Short | Type | Default | Description |
|----------|-------|------|---------|-------------|
| `--crypto` | `-c` | string | bitcoin | Cryptocurrency ID (e.g., bitcoin, ethereum, dogecoin) |
| `--target` | `-t` | float | None | Target price for notification |
| `--condition` | - | string | above | Condition for notification (above/below) |
| `--interval` | `-i` | int | 60 | Check interval in seconds |
| `--duration` | `-d` | int | None | Total monitoring duration in seconds |
| `--once` | - | flag | False | Check price once and exit |

## Supported Cryptocurrencies

You can monitor any cryptocurrency supported by CoinGecko. Some popular options:

- `bitcoin` (BTC)
- `ethereum` (ETH)
- `dogecoin` (DOGE)
- `cardano` (ADA)
- `solana` (SOL)
- `polkadot` (DOT)
- `ripple` (XRP)
- `litecoin` (LTC)
- `chainlink` (LINK)
- `polygon` (MATIC)

For the complete list, visit: https://api.coingecko.com/api/v3/coins/list

## Output Example

```
============================================================
Cryptocurrency: BITCOIN
Current Price: $43,567.89 USD
24h Change: ▲ 2.45%
Market Cap: $852,134,567,890
Last Updated: 2024-10-19 13:45:23
============================================================
```

## Price History

The tool automatically saves price data to `crypto_price_history.json` in the current directory. The history is limited to the last 100 entries.

## Features in Detail

### Real-time Monitoring
The tool fetches live price data from CoinGecko API and displays it in an easy-to-read format.

### Threshold Notifications
Set price targets and receive notifications when the cryptocurrency reaches your specified price level.

### 24-Hour Change
Track price changes over the last 24 hours with visual indicators (▲ for increase, ▼ for decrease).

### Market Cap
View the current market capitalization of the cryptocurrency.

### Continuous Monitoring
Monitor prices at custom intervals with automatic threshold checking.

## Error Handling

The tool includes robust error handling for:
- Network connection issues
- Invalid cryptocurrency IDs
- API rate limiting
- Invalid input parameters

## Tips

- Use shorter intervals (e.g., 30 seconds) for active trading
- Use longer intervals (e.g., 300 seconds) for passive monitoring to reduce API calls
- Press `Ctrl+C` to stop monitoring at any time
- Check the CoinGecko API documentation for cryptocurrency IDs: https://www.coingecko.com/en/api/documentation

## Contributing

This project is part of the 100 Lines of Python Code challenge. Contributions are welcome!

## Issue Reference

This implementation addresses issue #1036 from the 100LinesOfPythonCode repository.

## License

This project is open source and available under the MIT License.

## Disclaimer

⚠️ This tool is for educational and informational purposes only. It should not be used as the sole basis for making financial decisions. Cryptocurrency prices are highly volatile. Always do your own research before investing.

## Future Enhancements

Potential features for future versions:
- Email notifications
- SMS notifications
- Desktop notifications
- Multiple cryptocurrency monitoring
- Price charts
- Telegram bot integration
- Discord webhook integration

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Happy Crypto Monitoring! 🚀**
