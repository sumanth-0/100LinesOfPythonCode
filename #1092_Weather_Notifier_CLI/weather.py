import requests

def get_weather(city: str) -> dict:
    """Fetch current weather data for a given city using the Open-Meteo API."""
    try:
        # Step 1: Get coordinates of the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url).json()

        if "results" not in geo_response:
            return {"error": "City not found."}

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        # Step 2: Fetch weather data using coordinates
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}"
            f"&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code"
        )
        weather_response = requests.get(weather_url).json()
        current = weather_response.get("current", {})

        return {
            "city": city.title(),
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "condition": decode_weather(current.get("weather_code")),
        }
    except Exception as e:
        return {"error": f"Error fetching data: {e}"}


def decode_weather(code: int) -> str:
    """Convert weather code to human-readable condition."""
    conditions = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Depositing rime fog", 51: "Light drizzle", 61: "Light rain",
        71: "Light snow", 80: "Rain showers", 95: "Thunderstorm"
    }
    return conditions.get(code, "Unknown")


def main():
    print("🌤️  Weather Notifier CLI")
    city = input("Enter city name: ").strip()
    weather = get_weather(city)

    if "error" in weather:
        print("❌", weather["error"])
    else:
        print(f"\n📍 City: {weather['city']}")
        print(f"🌡️  Temperature: {weather['temperature']}°C")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"🌦️  Condition: {weather['condition']}")


if __name__ == "__main__":
    main()
