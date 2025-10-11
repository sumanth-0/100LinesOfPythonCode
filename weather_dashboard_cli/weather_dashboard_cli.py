#!/usr/bin/env python3
"""Weather Dashboard CLI - Fetch and display weather information for any city."""

import requests
import sys
from datetime import datetime

# Weather emoji mapping
WEATHER_EMOJIS = {
    'Clear': '☀️',
    'Clouds': '☁️',
    'Rain': '🌧️',
    'Drizzle': '🌦️',
    'Thunderstorm': '⛈️',
    'Snow': '❄️',
    'Mist': '🌫️',
    'Fog': '🌫️',
    'Haze': '🌫️',
    'Smoke': '💨',
    'Dust': '💨',
    'Sand': '💨'
}

def get_weather_emoji(condition):
    """Return emoji for weather condition."""
    return WEATHER_EMOJIS.get(condition, '🌍')

def format_temperature(temp):
    """Format temperature with color indicator."""
    if temp > 30:
        return f"🔥 {temp}°C (Hot)"
    elif temp > 20:
        return f"😊 {temp}°C (Warm)"
    elif temp > 10:
        return f"🙂 {temp}°C (Mild)"
    else:
        return f"🥶 {temp}°C (Cold)"

def fetch_weather(city, api_key='demo'):
    """Fetch weather data from OpenWeatherMap API."""
    # Using OpenWeatherMap API (users should get their own API key)
    # For demo purposes, we'll use wttr.in as a fallback which doesn't require API key
    
    # Try wttr.in first (no API key needed)
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        current = data['current_condition'][0]
        weather_desc = current['weatherDesc'][0]['value']
        temp_c = float(current['temp_C'])
        feels_like = float(current['FeelsLikeC'])
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        
        # Determine weather condition for emoji
        condition = 'Clear' if 'clear' in weather_desc.lower() else \
                   'Clouds' if 'cloud' in weather_desc.lower() else \
                   'Rain' if 'rain' in weather_desc.lower() else \
                   'Snow' if 'snow' in weather_desc.lower() else \
                   'Thunderstorm' if 'thunder' in weather_desc.lower() else \
                   'Mist' if any(x in weather_desc.lower() for x in ['mist', 'fog']) else weather_desc
        
        return {
            'city': city,
            'condition': condition,
            'description': weather_desc,
            'temperature': temp_c,
            'feels_like': feels_like,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    except Exception as e:
        print(f"❌ Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    """Display weather information with emojis."""
    if not weather_data:
        return
    
    emoji = get_weather_emoji(weather_data['condition'])
    
    print("\n" + "="*50)
    print(f"  🌍 Weather Dashboard for {weather_data['city'].title()}")
    print("="*50)
    print(f"\n{emoji}  Condition: {weather_data['description']}")
    print(f"🌡️  Temperature: {format_temperature(weather_data['temperature'])}")
    print(f"🤔 Feels Like: {weather_data['feels_like']}°C")
    print(f"💧 Humidity: {weather_data['humidity']}%")
    print(f"💨 Wind Speed: {weather_data['wind_speed']} km/h")
    print(f"⏰ Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50 + "\n")

def main():
    """Main function to run the weather dashboard."""
    print("\n🌦️  Welcome to Weather Dashboard CLI!\n")
    
    if len(sys.argv) > 1:
        city = ' '.join(sys.argv[1:])
    else:
        city = input("Enter city name: ").strip()
    
    if not city:
        print("❌ City name cannot be empty!")
        sys.exit(1)
    
    print(f"\n🔍 Fetching weather for {city}...\n")
    weather_data = fetch_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
