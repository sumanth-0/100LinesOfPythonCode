# 🌦️ Weather Info App
A simple Python script that fetches real-time weather information for any city using the OpenWeatherMap API.

## 📋 Features
- Fetches live weather data including:
   - 🌡️ Temperature (in °C)
  - 💧 Humidity (%)
  - 🌥️ Weather conditions 
- Automatically handles:
 - Invalid city names
 - Network or API errors
 - Missing or incorrect data
- Uses the free and reliable OpenWeatherMap API

## ⚙️ Requirements
- Install requests library
> pip install requests
- Get your free API key from  **[OpenWeatherMap API](https://openweathermap.org/api)**

## 🚀 How to Run
- Replace the placeholder in the script:
> API_key = "your_api_key_here"
- Save the file.      
- Run it in your terminal:
> python weather.py
- Enter any city name when prompted:
  
## 🧾 Example Output
Enter a city name: Tokyo

--- Weather in Tokyo ---      
Temperature: 27.3°C       
Humidity: 68%            
Conditions: Broken Clouds
