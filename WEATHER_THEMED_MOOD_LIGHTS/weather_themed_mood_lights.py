import requests

def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def mood_color(weather_main):
    mood_colors = {
        "Clear": "Yellow",
        "Clouds": "Gray",
        "Rain": "Blue",
        "Thunderstorm": "Purple",
        "Snow": "White",
        "Drizzle": "Light Blue",
        "Mist": "Light Gray",
    }
    return mood_colors.get(weather_main, "Neutral")

def display_mood_light(city):
    weather_data = get_weather(city)
    weather_main = weather_data["weather"][0]["main"]
    color = mood_color(weather_main)
    print(f"The weather is {weather_main}. Setting lights to {color}.")

def main():
    city = input("Enter your city: ")
    display_mood_light(city)

if __name__ == "__main__":
    main()
