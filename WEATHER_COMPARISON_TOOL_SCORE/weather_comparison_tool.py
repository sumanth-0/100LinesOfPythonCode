
import tkinter as tk

class WeatherComparisonTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Comparison Tool")
        
        tk.Label(root, text="City 1:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="City 2:").grid(row=1, column=0, padx=10, pady=10)

        self.city1_entry = tk.Entry(root)
        self.city1_entry.grid(row=0, column=1, padx=10)
        self.city2_entry = tk.Entry(root)
        self.city2_entry.grid(row=1, column=1, padx=10)

        compare_button = tk.Button(root, text="Compare", command=self.compare_weather)
        compare_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def compare_weather(self):
        # Placeholder functionality for demonstration
        city1_weather = "Sunny, 25°C"
        city2_weather = "Cloudy, 22°C"
        self.result_label.config(text=f"City 1 Weather: {city1_weather}\nCity 2 Weather: {city2_weather}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherComparisonTool(root)
    root.mainloop()
