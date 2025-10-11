"""
Water Usage Tracker
- Log daily water usage (liters)
- View daily log as ASCII bar chart or matplotlib chart
"""

import os, json
from datetime import date

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

DATA_FILE = os.path.join(os.getcwd(), "water_usage.json")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_water():
    today = str(date.today())
    try:
        usage = float(input(f"Enter water usage for {today} (liters): "))
        if usage < 0:
            print("Cannot be negative!")
            return
    except ValueError:
        print("Invalid input!")
        return
    data = load_data()
    data[today] = usage
    save_data(data)
    print(f"✅ Logged {usage} liters for {today}")

def show_ascii_chart(data):
    print("\n🌊 Daily Water Usage (ASCII)")
    for day, usage in sorted(data.items()):
        bar = "█" * int(usage)
        print(f"{day}: {bar} ({usage} L)")

def show_matplotlib_chart(data):
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not installed. ASCII chart will be shown instead.")
        show_ascii_chart(data)
        return
    days = sorted(data.keys())
    usage = [data[d] for d in days]
    plt.figure(figsize=(8,4))
    plt.bar(days, usage, color='skyblue')
    plt.title("Daily Water Usage (Liters)")
    plt.xlabel("Date")
    plt.ylabel("Liters")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("\n🌊 Welcome to Water Usage Tracker 🌊")
    while True:
        print("\nMenu:")
        print("1️⃣  Log Water Usage")
        print("2️⃣  Show ASCII Chart")
        print("3️⃣  Show Matplotlib Chart")
        print("4️⃣  Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            log_water()
        elif choice == "2":
            show_ascii_chart(load_data())
        elif choice == "3":
            show_matplotlib_chart(load_data())
        elif choice == "4":
            print("Goodbye! 💧 Keep track of your water usage.")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
