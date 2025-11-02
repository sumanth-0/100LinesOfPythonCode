#!/usr/bin/env python3
"""
weather_cli.py
Simple Weather CLI using Open-Meteo and OpenStreetMap APIs.

Usage:
  python weather_cli.py "New Delhi"
  python weather_cli.py "San Francisco"
"""

import requests
import sys

def get_coordinates(city):
    """Get latitude and longitude for a city using Nominatim API."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    resp = requests.get(url, params=params, headers={"User-Agent": "WeatherCLI/1.0"})
    resp.raise_for_status()
    data = resp.json()
    if not data:
        raise ValueError(f"City '{city}' not found.")
    return float(data[0]["lat"]), float(data[0]["lon"])

def get_weather(lat, lon):
    """Fetch current weather from Open-Meteo API."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()["current_weather"]

def show_weather(city):
    """Display weather info for a city."""
    try:
        lat, lon = get_coordinates(city)
        weather = get_weather(lat, lon)
        print(f"🌍  Weather for {city}")
        print(f"📍  Lat: {lat:.2f}, Lon: {lon:.2f}")
        print(f"🌡️  Temperature: {weather['temperature']}°C")
        print(f"💨  Windspeed: {weather['windspeed']} km/h")
        print(f"🕒  Time: {weather['time']}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py <city name>")
        sys.exit(1)
    city_name = " ".join(sys.argv[1:])
    show_weather(city_name)
