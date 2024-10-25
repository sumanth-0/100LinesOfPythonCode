import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Create complete URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Get response from the API
    response = requests.get(complete_url)
    return response.json()

def display_weather(data):
    if data['cod'] == 200:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_desc.capitalize()}")
    else:
        print(f"City not found or error occurred.")

def main():
    print("Welcome to the Weather Dashboard!")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_data = get_weather(city)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
