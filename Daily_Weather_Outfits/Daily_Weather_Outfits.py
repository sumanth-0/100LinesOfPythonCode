# Daily_Weather_Outfits.py

import requests

# Function to get weather data using OpenWeatherMap API
def get_weather(city):
    api_key = "your_api_key_here"  # Insert your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to suggest outfits based on temperature
def suggest_outfit(weather_data):
    temp = weather_data['main']['temp']
    weather = weather_data['weather'][0]['main']
    outfit = ""

    if temp < 10:
        outfit = "Wear a warm coat, scarf, and boots!"
    elif 10 <= temp < 20:
        outfit = "A jacket or sweater should be perfect for today."
    elif 20 <= temp < 30:
        outfit = "A light shirt and jeans will keep you comfortable."
    else:
        outfit = "Stay cool with a t-shirt and shorts!"

    # Add weather-based suggestions
    if weather == "Rain":
        outfit += " Don't forget an umbrella or raincoat!"
    elif weather == "Snow":
        outfit += " A snow jacket and gloves will be necessary!"
    
    return outfit

# Main function to get the weather and suggest an outfit
def daily_outfit_suggestion(city):
    weather_data = get_weather(city)
    if weather_data.get("cod") != 200:
        print("City not found or there is an issue with the weather data.")
        return
    print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    outfit = suggest_outfit(weather_data)
    print(f"Suggested Outfit: {outfit}")

# Run the program
if __name__ == "__main__":
    city = input("Enter your city: ")
    daily_outfit_suggestion(city)
