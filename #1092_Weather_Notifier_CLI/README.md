# 🌤️ Weather Notifier CLI

A simple command-line tool that fetches the **current weather** for any
city and displays: - Temperature (°C) - Humidity (%) - Weather condition
(e.g., Clear, Cloudy, Rainy)

------------------------------------------------------------------------

## ⚙️ Features

-   No API key required.
-   Uses the free **Open-Meteo API**.
-   Works directly in your terminal.

------------------------------------------------------------------------

## 🚀 Usage

1.  Install dependencies:

    ``` bash
    pip install requests
    ```

2.  Run the script:

    ``` bash
    python weather_notifier.py
    ```

3.  Enter a city name when prompted.

------------------------------------------------------------------------

## 🧠 Example

    🌤️  Weather Notifier CLI
    Enter city name: Mumbai

    📍 City: Mumbai
    🌡️  Temperature: 30.2°C
    💧 Humidity: 72%
    🌦️  Condition: Partly cloudy

------------------------------------------------------------------------

## 🧰 Tech

-   **Python 3**
-   **Requests library**
-   **Open-Meteo API** (no authentication needed)

------------------------------------------------------------------------

## 💡 Notes

This project is great for learning about: - Using REST APIs - JSON
parsing in Python - Building simple CLI utilities