import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Create complete URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Get response from the API
    response = requests.get(complete_url)
    return response.json()

def display_weather(api_key, city):
    data = get_weather(api_key, city)
    if data['cod'] == 200:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']

        result = (f"Weather in {city_name}:\n"
                  f"Temperature: {temperature}°C\n"
                  f"Humidity: {humidity}%\n"
                  f"Conditions: {weather_desc.capitalize()}")
        messagebox.showinfo("Weather Information", result)
    else:
        messagebox.showerror("Error", "City not found or error occurred.")

def on_submit():
    api_key = api_key_entry.get()
    city = city_entry.get()
    if api_key and city:
        display_weather(api_key, city)
    else:
        messagebox.showwarning("Warning", "Please enter both API key and city name.")

# Create the main window
root = tk.Tk()
root.title("Weather Dashboard")

# Create and place labels and entries
tk.Label(root, text="Enter your OpenWeatherMap API Key:").pack(pady=10)
api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack(pady=5)

tk.Label(root, text="Enter city name:").pack(pady=10)
city_entry = tk.Entry(root, width=50)
city_entry.pack(pady=5)

# Create and place submit button
submit_button = tk.Button(root, text="Get Weather", command=on_submit)
submit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
