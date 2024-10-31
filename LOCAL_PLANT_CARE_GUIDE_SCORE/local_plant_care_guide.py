
import tkinter as tk
from tkinter import ttk

class PlantCareGuide:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Plant Care Guide")
        self.plants = {
            "Aloe Vera": {"Light": "Bright, indirect light", "Water": "Once every 3 weeks"},
            "Snake Plant": {"Light": "Low to bright indirect light", "Water": "Once every 2 weeks"},
            "Spider Plant": {"Light": "Indirect light", "Water": "Once a week"},
        }
        self.setup_gui()

    def setup_gui(self):
        # Plant selection dropdown
        self.plant_var = tk.StringVar()
        self.plant_var.set("Select Plant")
        plant_menu = ttk.Combobox(self.root, textvariable=self.plant_var, values=list(self.plants.keys()))
        plant_menu.grid(row=0, column=1, padx=10, pady=10)

        # Show care info button
        show_info_button = ttk.Button(self.root, text="Show Care Info", command=self.show_care_info)
        show_info_button.grid(row=1, column=1, padx=10, pady=10)

        # Care info display
        self.care_info_label = ttk.Label(self.root, text="")
        self.care_info_label.grid(row=2, column=1, padx=10, pady=10)

        # Label
        ttk.Label(self.root, text="Plant:").grid(row=0, column=0, padx=10, pady=10)

    def show_care_info(self):
        plant = self.plant_var.get()
        if plant in self.plants:
            light = self.plants[plant]["Light"]
            water = self.plants[plant]["Water"]
            self.care_info_label.config(text=f"Light: {light}\nWater: {water}")
        else:
            self.care_info_label.config(text="Please select a valid plant.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlantCareGuide(root)
    root.mainloop()
