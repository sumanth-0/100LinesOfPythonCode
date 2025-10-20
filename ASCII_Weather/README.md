# ASCII Weather

A terminal-based weather application that fetches current weather data and displays it with beautiful ASCII art.

## Features

- **Real-time Weather Data**: Fetches current weather conditions from OpenWeatherMap API
- **ASCII Art Display**: Shows weather conditions with artistic ASCII representations
- **Temperature Evolution**: Displays temperature trends using animated matrix visualization
- **5-Day Forecast**: Provides weather forecasts for the upcoming days
- **Demo Mode**: Can run without API key to demonstrate functionality
- **Multiple Weather Conditions**: Supports Clear, Clouds, Rain, Snow, Thunderstorm, Drizzle, and Mist

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/ascii_weather
```

2. Install required dependencies:
```bash
pip install requests
```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Navigate to API keys section
   - Generate a new API key

## Usage

### With API Key (Recommended)

```bash
python ascii_weather.py
```

When prompted:
1. Enter your desired city name
2. Enter your OpenWeatherMap API key

Example:
```
Enter city name: London
Enter your OpenWeatherMap API key: your_api_key_here
```

### Demo Mode

You can also run the application in demo mode without an API key:

```bash
python ascii_weather.py
```

When prompted for the API key, simply press Enter to use demo mode with sample data.

## Output Features

### Current Weather Display
- City name and country
- ASCII art representation of weather condition
- Current temperature and "feels like" temperature
- Humidity percentage
- Wind speed
- Atmospheric pressure
- Sunrise and sunset times

### Temperature Evolution
- Visual bar chart showing temperature trends
- Next 24 hours temperature forecast
- Easy-to-read matrix format

### 5-Day Forecast
- Daily weather summaries
- Minimum, average, and maximum temperatures
- Most common weather condition per day

## Example ASCII Art

### Sunny Weather
```
    \   /    
     .-.     
  ― (   ) ―  
     `-'     
    /   \    
```

### Rainy Weather
```
      .-.     
     (   ).   
    (___(__)  
   ‚'‚'‚'‚'   
   ‚'‚'‚'‚'   
```

### Cloudy Weather
```
      .--.    
   .-(    ).  
  (___.__)__) 
```

## API Information

This application uses the OpenWeatherMap API:
- **Current Weather Endpoint**: `http://api.openweathermap.org/data/2.5/weather`
- **Forecast Endpoint**: `http://api.openweathermap.org/data/2.5/forecast`
- **Free Tier**: 1,000 API calls per day
- **Documentation**: https://openweathermap.org/api

## Error Handling

The application includes comprehensive error handling:
- Invalid city names
- Network connection issues
- Invalid API keys
- API rate limiting

## Contributing

This project is part of the 100 Lines of Python Code collection. Contributions are welcome!

## Issue Reference

This application was created for issue #859 in the 100LinesOfPythonCode repository.

## License

This project is part of the 100LinesOfPythonCode repository. Please refer to the main repository for licensing information.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- ASCII art inspired by various weather terminal applications
- Created as part of Hacktoberfest contributions
