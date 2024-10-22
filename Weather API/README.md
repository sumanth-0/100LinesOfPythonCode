# Weather Forecast Application

## Overview
The **Weather Forecast Application** is a Python program that uses the OpenWeatherMap API to predict today's weather for a specified city. It provides a detailed forecast, including temperature, weather description, and wind speed, with an engaging user interface featuring loading animations and colorful tables, thanks to the `rich` library.

## Features
- Fetches the weather forecast for today using the OpenWeatherMap API.
- Displays the forecast in an easy-to-read table format, including:
  - Time of forecast
  - Temperature in Celsius
  - Weather description
  - Wind speed
- Saves weather data to a JSON file for each city searched.

## Installation and Setup
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```
2. **Navigate to the project directory**:
   ```bash
   cd weather_forecast_app
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install rich
   ```
4. **Set up the environment**:
   - Create a `.env` file and add your OpenWeatherMap API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

## Usage
Run the script to get today's weather forecast for your city:
```bash
python app.py
```
Enter the name of the city when prompted, and the forecast will be displayed in a well-formatted table with animations.

## Important Information
- **API Key**: Make sure you have a valid OpenWeatherMap API key to use the app.
- **JSON File**: The forecast data for each city is saved into a JSON file (e.g., `london_weather_data.json`) for later reference.



## License

This project is licensed under the MIT License.

## Contribution

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Contact

For any queries or issues, please reach out at ttasbi@myseneca.ca.