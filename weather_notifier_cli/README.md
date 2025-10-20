# Weather Notifier CLI

A comprehensive command-line weather notification tool that provides current weather information, forecasts, and customizable weather alerts.

## Features

- **Current Weather**: Get real-time weather data for any city
- **5-Day Forecast**: View detailed weather forecasts with 3-hour intervals
- **Weather Alerts**: Set custom thresholds for temperature, humidity, and wind speed
- **Unit Conversion**: Support for both Celsius (metric) and Fahrenheit (imperial)
- **Weather Notifications**: Automatic alerts for rain, snow, thunderstorms, and more
- **Multiple Locations**: Check weather for any city worldwide

## Requirements

- Python 3.6+
- `requests` library
- OpenWeatherMap API key (free tier available)

## Installation

1. Clone this repository or download the script:

```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/weather_notifier_cli
```

2. Install required dependencies:

```bash
pip install requests
```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api):
   - Sign up for a free account
   - Navigate to API Keys section
   - Generate a new API key

## Usage

### Basic Usage

```bash
python weather_notifier_cli.py "London"
```

### With API Key

```bash
python weather_notifier_cli.py "New York" --api-key YOUR_API_KEY
```

Or set the API key as an environment variable:

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
python weather_notifier_cli.py "Tokyo"
```

### Get 5-Day Forecast

```bash
python weather_notifier_cli.py "Paris" --forecast
```

### Use Imperial Units (Fahrenheit)

```bash
python weather_notifier_cli.py "Los Angeles" --units imperial
```

### Enable Weather Alerts

```bash
python weather_notifier_cli.py "Mumbai" --alerts --max-temp 35 --min-temp 15 --max-humidity 80
```

### Combined Options

```bash
python weather_notifier_cli.py "Sydney" --api-key YOUR_API_KEY --forecast --alerts --max-temp 30 --units metric
```

## Command-Line Arguments

- `city`: (Required) Name of the city to get weather for
- `--api-key`: OpenWeatherMap API key (can also use `OPENWEATHER_API_KEY` env variable)
- `--units`: Temperature units - `metric` (Celsius) or `imperial` (Fahrenheit). Default: `metric`
- `--forecast`: Show 5-day weather forecast
- `--alerts`: Enable weather alerts based on thresholds
- `--max-temp`: Maximum temperature threshold for alerts
- `--min-temp`: Minimum temperature threshold for alerts
- `--max-humidity`: Maximum humidity threshold (%) for alerts
- `--max-wind`: Maximum wind speed threshold for alerts

## Output Examples

### Current Weather

```
==================================================
Current Weather for London, GB
==================================================
Temperature: 18.5°C
Feels Like: 17.2°C
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 5.2 m/s
Pressure: 1013 hPa
Visibility: 10000 meters
==================================================
```

### Weather Alerts

```
==================================================
WEATHER ALERTS
==================================================
⚠️  High temperature alert: 36.5°C
⚠️  Weather alert: Rain detected
==================================================
```

## How It Works

1. **API Integration**: The script uses the OpenWeatherMap API to fetch weather data
2. **Data Processing**: Weather data is parsed and formatted for easy reading
3. **Alert System**: Compares current conditions against user-defined thresholds
4. **Notifications**: Displays alerts when conditions exceed thresholds or specific weather events occur

## Error Handling

The script handles various error scenarios:
- Invalid API keys
- Network connectivity issues
- Invalid city names
- API rate limiting
- Timeout errors

## API Rate Limits

Free OpenWeatherMap API tier includes:
- 60 calls per minute
- 1,000,000 calls per month

## Contributing

This is part of the 100 Lines of Python Code project. Contributions are welcome!

## Related Issue

This implementation addresses issue [#1035](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1035)

## License

This project is part of the 100LinesOfPythonCode repository. Please refer to the main repository for license information.

## Credits

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) project

## Troubleshooting

### "Failed to retrieve weather data"
- Check your API key is valid
- Verify the city name is spelled correctly
- Ensure you have internet connectivity
- Check if you've exceeded API rate limits

### "Invalid API key"
- Obtain a new API key from OpenWeatherMap
- Ensure the key is activated (may take a few hours after generation)
- Check for any typos in the API key

## Future Enhancements

- Email/SMS notifications
- Historical weather data
- Weather maps visualization
- Multiple location tracking
- Scheduled weather checks
- Custom notification sounds
