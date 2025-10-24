#!/usr/bin/env python3
"""
ASCII Weather - Terminal Weather Application
Fetches current weather data and displays it with ASCII art
"""

import requests
import json
import sys
from datetime import datetime
import time

# ASCII Art for different weather conditions
WEATHER_ART = {
    "Clear": """
    \   /    
     .-.     
  ― (   ) ―  
     `-'     
    /   \    
""",
    "Clouds": """
      .--.    
   .-(    ).  
  (___.__)__) 
              
""",
    "Rain": """
      .-.     
     (   ).   
    (___(__)  
   ‚'‚'‚'‚'   
   ‚'‚'‚'‚'   
""",
    "Snow": """
      .-.     
     (   ).   
    (___(__)  
   * * * *    
  * * * *     
""",
    "Thunderstorm": """
      .-.     
     (   ).   
    (___(__)  
   ⚡'⚡'⚡'   
   ‚'‚'‚'‚'   
""",
    "Drizzle": """
      .-.     
     (   ).   
    (___(__)  
   ‚ ‚ ‚ ‚    
              
""",
    "Mist": """
             
 _ - _ - _ -  
  _ - _ - _   
 _ - _ - _ -  
"""
}

def get_weather_art(condition):
    """Return ASCII art for weather condition"""
    for key in WEATHER_ART:
        if key.lower() in condition.lower():
            return WEATHER_ART[key]
    return WEATHER_ART["Clear"]  # Default

def display_temperature_matrix(temps, label="Temperature Evolution"):
    """Display temperature evolution as a matrix animation"""
    print(f"\n{label}:")
    print("=" * 50)
    max_temp = max(temps)
    min_temp = min(temps)
    temp_range = max_temp - min_temp if max_temp != min_temp else 1
    
    # Create a visual bar for each temperature
    for i, temp in enumerate(temps):
        bar_length = int(((temp - min_temp) / temp_range) * 30)
        bar = "█" * bar_length
        time_label = f"Hour {i:2d}" if i < 24 else f"Day {i//24 + 1}"
        print(f"{time_label}: {bar} {temp:.1f}°C")
    print("=" * 50)

def fetch_weather_data(city, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def fetch_forecast_data(city, api_key):
    """Fetch 5-day forecast from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def display_current_weather(data):
    """Display current weather with ASCII art"""
    if not data:
        return
    
    print("\n" + "=" * 60)
    print(f"Current Weather in {data['name']}, {data['sys']['country']}")
    print("=" * 60)
    
    # Get weather condition
    condition = data['weather'][0]['main']
    description = data['weather'][0]['description'].title()
    
    # Display ASCII art
    print(get_weather_art(condition))
    
    # Display weather details
    print(f"Condition: {description}")
    print(f"Temperature: {data['main']['temp']:.1f}°C")
    print(f"Feels Like: {data['main']['feels_like']:.1f}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Pressure: {data['main']['pressure']} hPa")
    
    # Sunrise and sunset
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
    print(f"Sunrise: {sunrise} | Sunset: {sunset}")
    print("=" * 60)

def display_forecast(forecast_data):
    """Display weather forecast for next days"""
    if not forecast_data:
        return
    
    print("\n5-Day Weather Forecast:")
    print("=" * 60)
    
    # Group forecasts by day
    daily_forecasts = {}
    temps = []
    
    for item in forecast_data['list']:
        date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        temp = item['main']['temp']
        temps.append(temp)
        
        if date not in daily_forecasts:
            daily_forecasts[date] = {
                'temps': [],
                'conditions': [],
                'descriptions': []
            }
        
        daily_forecasts[date]['temps'].append(temp)
        daily_forecasts[date]['conditions'].append(item['weather'][0]['main'])
        daily_forecasts[date]['descriptions'].append(item['weather'][0]['description'])
    
    # Display daily summaries
    for date, info in list(daily_forecasts.items())[:5]:
        avg_temp = sum(info['temps']) / len(info['temps'])
        max_temp = max(info['temps'])
        min_temp = min(info['temps'])
        most_common_condition = max(set(info['conditions']), key=info['conditions'].count)
        
        print(f"\n{date}:")
        print(f"  Condition: {most_common_condition}")
        print(f"  Temp: Min {min_temp:.1f}°C | Avg {avg_temp:.1f}°C | Max {max_temp:.1f}°C")
    
    print("\n" + "=" * 60)
    
    # Display temperature evolution matrix for next 24 hours
    next_24_temps = temps[:8]  # 8 x 3-hour periods = 24 hours
    if next_24_temps:
        display_temperature_matrix(next_24_temps, "Next 24 Hours Temperature")

def main():
    """Main function to run the weather application"""
    print("\n" + "*" * 60)
    print("*" + " " * 18 + "ASCII WEATHER APP" + " " * 19 + "*")
    print("*" * 60)
    
    # Get city from user
    city = input("\nEnter city name: ").strip()
    if not city:
        print("Error: City name cannot be empty!")
        sys.exit(1)
    
    # API Key - users should replace this with their own key
    api_key = input("Enter your OpenWeatherMap API key (or press Enter to use demo mode): ").strip()
    
    if not api_key:
        print("\nRunning in demo mode with sample data...")
        print("To use real data, get a free API key from: https://openweathermap.org/api")
        # Demo data
        print("\nShowing sample weather for London:")
        sample_temps = [15.5, 16.2, 17.1, 18.3, 19.5, 20.1, 19.8, 18.9]
        display_temperature_matrix(sample_temps, "Sample Temperature Evolution")
        return
    
    # Fetch and display current weather
    print(f"\nFetching weather data for {city}...")
    weather_data = fetch_weather_data(city, api_key)
    
    if weather_data:
        display_current_weather(weather_data)
        
        # Fetch and display forecast
        print(f"\nFetching forecast data for {city}...")
        forecast_data = fetch_forecast_data(city, api_key)
        
        if forecast_data:
            display_forecast(forecast_data)
        
        print("\nWeather data successfully retrieved!")
    else:
        print("\nFailed to retrieve weather data. Please check:")
        print("1. City name is correct")
        print("2. API key is valid")
        print("3. Internet connection is working")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
