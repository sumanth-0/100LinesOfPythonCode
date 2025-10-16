# 🌤️ ASCII Weather

A beautiful command-line weather application that displays current weather and forecasts with colorful ASCII art!

---
## ✨ Features
-   **🎨 Beautiful ASCII Art Weather Icons** - Visual representation of weather conditions (sunny, cloudy, rainy, snowy).
-   **🌡️ Current Weather Details** - Temperature, condition, humidity, and wind speed.
-   **📅 5-Day Forecast** - Extended weather predictions with max/min temperatures.
-   **🎨 Colorful Output** - Enhanced terminal experience with `colorama`.
-   **🔤 ASCII Art Title** - Stylish header using `pyfiglet`.

---
## 📋 Prerequisites
-   Python 3.6 or higher
-   Internet connection (to fetch weather data)

---
## 🚀 Installation

1.  **Clone or download this repository.**
2.  **Install required packages:**
    ```bash
    pip install requests pyfiglet colorama
    ```

---
## 🔑 Getting Your API Key

1.  Visit **[WeatherAPI.com](https://www.weatherapi.com/)**.
2.  Sign up for a free account.
3.  Navigate to your dashboard and copy your API key.

---
## ⚙️ Configuration
You must manually add your API key to the script.

1.  Open `Weather.py` in a text editor.
2.  Find this line:
    ```python
    API_KEY = "YOUR_API_KEY_GOES_HERE"
    ```
3.  Replace `YOUR_API_KEY_GOES_HERE` with your actual API key:
    ```python
    API_KEY = "your_actual_api_key_here"
    ```
4.  Save the file.

---
## 🎮 Usage
Run the script from your terminal:
```bash
python Weather.py