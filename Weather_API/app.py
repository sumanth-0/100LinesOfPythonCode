import requests
from dotenv import load_dotenv
import os
import json
import time
import sys
from rich.console import Console
from rich.table import Table

# Load environment variables from .env file
load_dotenv()

# Create console for formatted output
console = Console()

# Loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for frame in animation:
            sys.stdout.write(f"\r Loading... {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r Loading complete!         \n")

# Get weather forecast for a city
def get_forecast(city_name):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        console.print("[bold red]API key not found. Set it in the .env file.[/bold red]")
        return

    loading_animation()

    # API request
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        console.print(f"[bold red]City {city_name} not found or an error occurred: {data.get('message')}[/bold red]")
    else:
        console.print(f"\n[bold blue]Weather forecast for {city_name.capitalize()} for today:[/bold blue]\n")
        
        # Display today's forecast in a table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Time", style="dim")
        table.add_column("Temperature (°C)")
        table.add_column("Description")
        table.add_column("Wind Speed (m/s)")
        
        today = data['list'][0]['dt_txt'].split()[0]
        for forecast in data['list']:
            if forecast['dt_txt'].startswith(today):
                temp = forecast['main']['temp']
                desc = forecast['weather'][0]['description']
                wind = forecast['wind']['speed']
                table.add_row(forecast['dt_txt'], f"{temp} °C", desc.capitalize(), f"{wind} m/s")
        
        console.print(table)
        save_to_file(city_name, data)

# Save weather data to JSON file
def save_to_file(city_name, data):
    filename = f'{city_name.lower()}_weather_data.json'
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        console.print(f"\n[bold green]Weather data for {city_name} saved to {filename}.[/bold green]\n")
    except Exception as e:
        console.print(f"[bold red]Error saving data: {e}[/bold red]")

if __name__ == "__main__":
    city = console.input("[bold yellow]Enter city name: [/bold yellow]")
    get_forecast(city)
