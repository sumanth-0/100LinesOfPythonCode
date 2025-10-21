import requests
import datetime

def get_weather(city, api_key):
    """Fetch weather data from OpenWeatherMap"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def display_weather(data):
    """Display weather details in a nice format"""
    name = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels = data['main']['feels_like']
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description'].capitalize()
    wind = data['wind']['speed']
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

    print(f"\n🌤️  Weather in {name}, {country}")
    print("──────────────────────────────")
    print(f"🌡️  Temperature: {temp}°C (Feels like {feels}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️  Wind Speed: {wind} m/s")
    print(f"🌈 Condition: {desc}")
    print(f"🌅 Sunrise: {sunrise}")
    print(f"🌇 Sunset: {sunset}")
    print("──────────────────────────────\n")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    api_key = "8a72f2324bcb659eb471ab4e2043ed03"  

    weather_data = get_weather(city, api_key)
    if weather_data:
        display_weather(weather_data)
