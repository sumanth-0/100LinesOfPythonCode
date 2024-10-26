import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch landmarks from Foursquare API
def fetch_landmarks_from_foursquare(city):
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Authorization": "YOUR_FOURSQUARE_API_KEY"  # Replace with your actual API KEY, api key is hidden
    }
    params = {
        "near": city,
        "query": "landmark",
        "limit": 5  # Limits to top 5 results
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        places = response.json().get("results", [])
        return [place["name"] for place in places] if places else ["No landmarks found."]
    else:
        print("Error:", response.status_code)
        return ["Error fetching data."]

# Function to handle button click
def get_landmarks():
    city = city_entry.get().title()  # Get city input from user
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    landmarks = fetch_landmarks_from_foursquare(city)
    result_text.set(f"Top places to visit in {city}:\n" + "\n".join(landmarks))

# Initialize main window
root = tk.Tk()
root.title("Travel Recommendation Tool")
root.geometry("400x300")

# User input and buttons
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

search_button = tk.Button(root, text="Get Recommendations", command=get_landmarks)
search_button.pack(pady=10)

# Display results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", wraplength=380)
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
