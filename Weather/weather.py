import requests
API_key = "your_api_key_here"
base_url = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")
params = {
    'q': city,
    'appid': API_key,
    'units': 'metric'
}

try:
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()  
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        print(f"\n--- Weather in {data['name']} ---")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.title()}")  
    else:
        data = response.json()
        print(f"\nError: {data.get('message', 'Could not find city.')}")

except requests.exceptions.RequestException:
    print("\nError: Could not connect to the weather service.")
except KeyError:
    print("\nError: Could not parse weather data.")
