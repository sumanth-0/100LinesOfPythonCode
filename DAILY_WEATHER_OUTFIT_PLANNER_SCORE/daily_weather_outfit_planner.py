
import tkinter as tk
import requests

class WeatherOutfitPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Weather & Outfit Planner")
        self.city_entry = tk.Entry(root, width=20)
        self.city_entry.grid(row=0, column=1, padx=10, pady=10)
        self.submit_button = tk.Button(root, text="Get Forecast", command=self.get_forecast)
        self.submit_button.grid(row=1, column=1, padx=10, pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(root, text="City:").grid(row=0, column=0, padx=10, pady=10)

    def get_forecast(self):
        city = self.city_entry.get()
        weather = self.fetch_weather(city)
        outfit = self.suggest_outfit(weather)
        self.result_label.config(text=f"Weather: {weather}\nOutfit: {outfit}")

    def fetch_weather(self, city):
        # Mock weather retrieval
        return "Sunny"

    def suggest_outfit(self, weather):
        if weather == "Sunny":
            return "T-shirt and sunglasses"
        elif weather == "Rainy":
            return "Raincoat and boots"
        else:
            return "Layered clothing"

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherOutfitPlanner(root)
    root.mainloop()
