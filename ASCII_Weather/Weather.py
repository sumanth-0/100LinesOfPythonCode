import requests, os
from pyfiglet import Figlet
from colorama import Fore, Style, init
from datetime import datetime
init(autoreset=True)
API_KEY = "YOUR_API_KEY_GOES_HERE"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
WEATHER_ICONS = {
    "sunny": Fore.YELLOW + "    \\   /    \n     .-.     \n  ― (   ) ―  \n     `-'     \n    /   \\    ",
    "cloudy": Fore.WHITE + "             \n    .--.    \n .-(    ).  \n(___.__)__) \n            ",
    "rainy": Fore.BLUE + "     .--.   \n  .-(    ). \n (___.__)__)\n  ‚'‚'‚'‚'  \n  ‚'‚'‚'‚'  ",
    "snowy": Fore.CYAN + "     .--.   \n  .-(    ). \n (___.__)__)\n  * * * *   \n * * * *    ",
    "default": Fore.RED + "             \n    .-.      \n   ( ? )     \n    `-'      \n             "
}
def get_weather_icon(condition_text):
    """Selects an icon based on the weather condition text."""
    condition = condition_text.lower()
    if "sun" in condition or "clear" in condition:
        return WEATHER_ICONS["sunny"]
    elif "cloud" in condition or "overcast" in condition:
        return WEATHER_ICONS["cloudy"]
    elif "rain" in condition or "drizzle" in condition:
        return WEATHER_ICONS["rainy"]
    elif "snow" in condition or "sleet" in condition:
        return WEATHER_ICONS["snowy"]
    else:
        return WEATHER_ICONS["default"]
def display_current_weather_esthetically(data):
    """
    Displays the current weather with the icon and text side-by-side.
    """
    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]
    
    icon = get_weather_icon(condition)
    icon_lines = icon.split('\n')
    text_lines = [
        f"{Fore.GREEN}\t  Location: {location}",
        f"{Style.BRIGHT}Temperature: {temp_c}°C{Style.NORMAL}",
        f"{Fore.LIGHTWHITE_EX}Condition: {condition}",
        f"{Fore.CYAN}Humidity: {humidity}%",
        f"{Fore.MAGENTA}Wind: {wind_kph} kph"
    ]
    print("\n" + "="*60)
    print(f"{Style.BRIGHT}{Fore.YELLOW}CURRENT WEATHER{Style.RESET_ALL}")
    print("="*60)
    for i in range(len(icon_lines)):
        if i < len(text_lines):
            print(f"{icon_lines[i]:<25} {text_lines[i]}")
        else:
            print(icon_lines[i])
    print("="*60)


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('ASCII Weather'))
    if API_KEY == "YOUR_API_KEY_GOES_HERE":
        print(Fore.RED + "Error: API key has not been configured in the script.")
    else:
        city = input(f"{Fore.MAGENTA}Enter the name of a city: ")
        if city:
            params = {"q": city, "key": API_KEY, "days": 6}
            try:
                response = requests.get(BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()
                display_current_weather_esthetically(data)
                print(Style.BRIGHT + Fore.CYAN + "5-DAY FORECAST" + "\n" + "="*60)
                for day in data["forecast"]["forecastday"][1:]:
                    date = datetime.strptime(day['date'], '%Y-%m-%d').strftime('%a, %b %d')
                    max_temp = day['day']['maxtemp_c']
                    min_temp = day['day']['mintemp_c']
                    day_condition = day['day']['condition']['text']
                    print(f"{Fore.YELLOW}{date:<15}: {Fore.RED}Max {max_temp}°C / {Fore.BLUE}Min {min_temp}°C - {Fore.LIGHTWHITE_EX}{day_condition}")
            except requests.exceptions.RequestException:
                print(Fore.RED + "Error: Could not retrieve weather data. Please check the city name.")
        else:
            print(Fore.RED + "Error: City name cannot be empty.")