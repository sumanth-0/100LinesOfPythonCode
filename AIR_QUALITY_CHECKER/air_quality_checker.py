import requests

def get_air_quality(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/air-pollution?appid={api_key}&q={city}"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        aqi = data['list'][0]['main']['aqi']
        pollutants = data['list'][0]['components']

        air_quality = {
            "AQI": aqi,
            "Pollutants": pollutants
        }
        return air_quality
    else:
        return None

def main():
    city = input("Enter the city name: ")
    air_quality = get_air_quality(city)
    
    if air_quality:
        print(f"Air Quality Index for {city}: {air_quality['AQI']}")
        print("Pollutant Levels:")
        for pollutant, level in air_quality["Pollutants"].items():
            print(f"{pollutant.capitalize()}: {level} µg/m³")
    else:
        print("Error retrieving data. Please check the city name and try again.")

if __name__ == "__main__":
    main()
