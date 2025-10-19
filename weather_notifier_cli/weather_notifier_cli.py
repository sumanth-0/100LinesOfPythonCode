#!/usr/bin/env python3
"""
Weather Notifier CLI

A command-line weather notification tool that fetches current weather data,
provides forecasts, and sends notifications based on specified conditions.

Features:
- Current weather information
- 5-day weather forecast
- Weather alerts and notifications
- Support for multiple locations
- Temperature unit conversion (Celsius/Fahrenheit)
- Customizable notification thresholds

Usage:
    python weather_notifier_cli.py <city> [options]
"""

import requests
import argparse
import json
import sys
from datetime import datetime
from typing import Dict, Optional, List
import os

# Constants
API_BASE_URL = "https://api.openweathermap.org/data/2.5"
DEFAULT_API_KEY = "demo"  # Users should replace with their own API key

class WeatherNotifier:
    """Main class for weather notification functionality."""
    
    def __init__(self, api_key: str = DEFAULT_API_KEY):
        """Initialize the WeatherNotifier with an API key."""
        self.api_key = api_key
        self.session = requests.Session()
    
    def get_current_weather(self, city: str, units: str = "metric") -> Optional[Dict]:
        """Fetch current weather data for a given city."""
        try:
            url = f"{API_BASE_URL}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def get_forecast(self, city: str, units: str = "metric") -> Optional[Dict]:
        """Fetch 5-day weather forecast for a given city."""
        try:
            url = f"{API_BASE_URL}/forecast"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return None
    
    def format_current_weather(self, data: Dict, units: str) -> str:
        """Format current weather data for display."""
        if not data:
            return "No weather data available."
        
        temp_unit = "°C" if units == "metric" else "°F"
        speed_unit = "m/s" if units == "metric" else "mph"
        
        output = []
        output.append("="*50)
        output.append(f"Current Weather for {data['name']}, {data['sys']['country']}")
        output.append("="*50)
        output.append(f"Temperature: {data['main']['temp']}{temp_unit}")
        output.append(f"Feels Like: {data['main']['feels_like']}{temp_unit}")
        output.append(f"Condition: {data['weather'][0]['description'].title()}")
        output.append(f"Humidity: {data['main']['humidity']}%")
        output.append(f"Wind Speed: {data['wind']['speed']} {speed_unit}")
        output.append(f"Pressure: {data['main']['pressure']} hPa")
        output.append(f"Visibility: {data.get('visibility', 'N/A')} meters")
        output.append("="*50)
        
        return "\n".join(output)
    
    def format_forecast(self, data: Dict, units: str, days: int = 5) -> str:
        """Format forecast data for display."""
        if not data or 'list' not in data:
            return "No forecast data available."
        
        temp_unit = "°C" if units == "metric" else "°F"
        
        output = []
        output.append("="*50)
        output.append(f"5-Day Forecast for {data['city']['name']}")
        output.append("="*50)
        
        # Group forecasts by day
        current_date = None
        for item in data['list'][:days*8]:  # 8 entries per day (3-hour intervals)
            dt = datetime.fromtimestamp(item['dt'])
            date_str = dt.strftime("%Y-%m-%d")
            
            if date_str != current_date:
                current_date = date_str
                output.append(f"\n{dt.strftime('%A, %B %d, %Y')}")
                output.append("-"*50)
            
            time_str = dt.strftime("%H:%M")
            temp = item['main']['temp']
            desc = item['weather'][0]['description'].title()
            output.append(f"  {time_str}: {temp}{temp_unit}, {desc}")
        
        output.append("="*50)
        return "\n".join(output)
    
    def check_weather_alerts(self, data: Dict, thresholds: Dict) -> List[str]:
        """Check weather conditions against thresholds and generate alerts."""
        alerts = []
        
        if not data:
            return alerts
        
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        if 'max_temp' in thresholds and temp > thresholds['max_temp']:
            alerts.append(f"⚠️  High temperature alert: {temp}°C")
        
        if 'min_temp' in thresholds and temp < thresholds['min_temp']:
            alerts.append(f"⚠️  Low temperature alert: {temp}°C")
        
        if 'max_humidity' in thresholds and humidity > thresholds['max_humidity']:
            alerts.append(f"⚠️  High humidity alert: {humidity}%")
        
        if 'max_wind' in thresholds and wind_speed > thresholds['max_wind']:
            alerts.append(f"⚠️  High wind speed alert: {wind_speed} m/s")
        
        # Check for specific weather conditions
        condition = data['weather'][0]['main'].lower()
        if condition in ['rain', 'thunderstorm', 'snow']:
            alerts.append(f"⚠️  Weather alert: {condition.title()} detected")
        
        return alerts

def main():
    """Main function to run the Weather Notifier CLI."""
    parser = argparse.ArgumentParser(
        description="Weather Notifier CLI - Get weather updates and alerts"
    )
    parser.add_argument("city", help="City name to get weather for")
    parser.add_argument(
        "--api-key",
        default=os.environ.get("OPENWEATHER_API_KEY", DEFAULT_API_KEY),
        help="OpenWeatherMap API key (or set OPENWEATHER_API_KEY env variable)"
    )
    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Temperature units (metric for Celsius, imperial for Fahrenheit)"
    )
    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Show 5-day weather forecast"
    )
    parser.add_argument(
        "--alerts",
        action="store_true",
        help="Check for weather alerts based on thresholds"
    )
    parser.add_argument(
        "--max-temp",
        type=float,
        help="Maximum temperature threshold for alerts"
    )
    parser.add_argument(
        "--min-temp",
        type=float,
        help="Minimum temperature threshold for alerts"
    )
    parser.add_argument(
        "--max-humidity",
        type=float,
        help="Maximum humidity threshold for alerts (%)"
    )
    parser.add_argument(
        "--max-wind",
        type=float,
        help="Maximum wind speed threshold for alerts"
    )
    
    args = parser.parse_args()
    
    # Initialize the weather notifier
    notifier = WeatherNotifier(api_key=args.api_key)
    
    # Get current weather
    current_weather = notifier.get_current_weather(args.city, args.units)
    
    if not current_weather:
        print("Failed to retrieve weather data. Please check your API key and city name.")
        sys.exit(1)
    
    # Display current weather
    print(notifier.format_current_weather(current_weather, args.units))
    
    # Check for alerts if requested
    if args.alerts:
        thresholds = {}
        if args.max_temp is not None:
            thresholds['max_temp'] = args.max_temp
        if args.min_temp is not None:
            thresholds['min_temp'] = args.min_temp
        if args.max_humidity is not None:
            thresholds['max_humidity'] = args.max_humidity
        if args.max_wind is not None:
            thresholds['max_wind'] = args.max_wind
        
        alerts = notifier.check_weather_alerts(current_weather, thresholds)
        
        if alerts:
            print("\n" + "="*50)
            print("WEATHER ALERTS")
            print("="*50)
            for alert in alerts:
                print(alert)
            print("="*50)
        else:
            print("\n✓ No weather alerts at this time.")
    
    # Show forecast if requested
    if args.forecast:
        forecast_data = notifier.get_forecast(args.city, args.units)
        if forecast_data:
            print("\n" + notifier.format_forecast(forecast_data, args.units))
        else:
            print("Failed to retrieve forecast data.")

if __name__ == "__main__":
    main()
