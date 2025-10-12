# Weather Dashboard CLI ☀️

A simple and elegant command-line weather dashboard that displays real-time weather information for any city with beautiful emoji icons and summaries.

## Features ✨

- 🌍 **City-based weather lookup** - Enter any city name to get weather information
- 🌡️ **Temperature display** - Shows current temperature with heat indicators (Hot/Warm/Mild/Cold)
- 💧 **Humidity tracking** - Current humidity percentage
- 💨 **Wind speed** - Real-time wind speed in km/h
- 🌦️ **Emoji weather icons** - Visual representation of weather conditions (sun, clouds, rain, snow, etc.)
- ⏰ **Timestamp** - Shows when the data was last updated
- 📊 **Feels like temperature** - What the temperature actually feels like

## Installation 📥

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/weather_dashboard_cli
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage 🚀

### Interactive Mode
Run the script without arguments to enter interactive mode:
```bash
python weather_dashboard_cli.py
```
You'll be prompted to enter a city name.

### Command-line Argument
Pass the city name directly as an argument:
```bash
python weather_dashboard_cli.py London
```

For cities with multiple words:
```bash
python weather_dashboard_cli.py New York
python weather_dashboard_cli.py Los Angeles
```

## Example Output 📝

```
🌦️  Welcome to Weather Dashboard CLI!

🔍 Fetching weather for London...

==================================================
  🌍 Weather Dashboard for London
==================================================

☁️  Condition: Partly cloudy
🌡️  Temperature: 🙂 15°C (Mild)
🤔 Feels Like: 13°C
💧 Humidity: 72%
💨 Wind Speed: 15 km/h
⏰ Updated: 2025-10-11 21:15:30
==================================================
```

## Weather Conditions & Emojis 🌈

The dashboard uses appropriate emojis based on weather conditions:

- ☀️ **Clear** - Sunny and clear skies
- ☁️ **Clouds** - Cloudy weather
- 🌧️ **Rain** - Rainy conditions
- 🌦️ **Drizzle** - Light rain
- ⛈️ **Thunderstorm** - Stormy weather
- ❄️ **Snow** - Snowy conditions
- 🌫️ **Mist/Fog/Haze** - Reduced visibility
- 💨 **Smoke/Dust/Sand** - Poor air quality

## Temperature Indicators 🌡️

- 🔥 **> 30°C** - Hot
- 😊 **20-30°C** - Warm
- 🙂 **10-20°C** - Mild
- 🥶 **< 10°C** - Cold

## API Information 🔑

This project uses the [wttr.in](https://wttr.in) API, which provides free weather data without requiring an API key. This makes it easy to use out of the box!

### Alternative: OpenWeatherMap

If you prefer to use OpenWeatherMap API:
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Modify the `fetch_weather()` function to use OpenWeatherMap endpoint
3. Pass your API key to the function

## Requirements 📝

- Python 3.6+
- `requests` library

## Code Statistics 📊

- **Total Lines**: < 100 lines (as per project requirement)
- **Language**: Python 3
- **Dependencies**: Minimal (only requests library)

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License 📜

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

## Author ✍️

Created as part of the Weather Dashboard CLI challenge (Issue #691)

---

**Enjoy checking the weather!** 🌤️
