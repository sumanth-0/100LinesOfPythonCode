"""
CO2 Emission Calculator
Estimate CO2 emissions for a given travel distance and mode (car, bus, flight)
"""

import json, os

DATA_FILE = os.path.join(os.getcwd(), "co2_emissions.json")

# Average CO2 emission rates (kg CO2 per km)
EMISSION_RATES = {
    "car": 0.192,     # per km per passenger
    "bus": 0.105,     # per km per passenger
    "flight": 0.255   # short-haul average per km per passenger
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def calculate_emission(mode, distance):
    rate = EMISSION_RATES.get(mode.lower())
    if not rate:
        print("Invalid mode. Choose car, bus, or flight.")
        return None
    return distance * rate

def log_trip():
    mode = input("Enter travel mode (car/bus/flight): ").strip().lower()
    try:
        distance = float(input("Enter distance traveled (km): "))
        if distance < 0:
            print("Distance cannot be negative.")
            return
    except ValueError:
        print("Invalid distance input.")
        return
    co2 = calculate_emission(mode, distance)
    if co2 is None:
        return
    trip = {"mode": mode, "distance_km": distance, "co2_kg": round(co2, 2)}
    data = load_data()
    data.append(trip)
    save_data(data)
    print(f"✅ Trip logged! Estimated CO2: {trip['co2_kg']} kg")

def show_history():
    data = load_data()
    if not data:
        print("No trips logged yet.")
        return
    print("\n📊 Logged Trips and CO2 Emissions:")
    for i, trip in enumerate(data, 1):
        print(f"{i}. Mode: {trip['mode'].capitalize()}, Distance: {trip['distance_km']} km, CO2: {trip['co2_kg']} kg")
    total = sum(t["co2_kg"] for t in data)
    print(f"\nTotal CO2 emitted: {round(total,2)} kg")

def main():
    print("\n🌍 CO2 Emission Calculator 🌍")
    while True:
        print("\nMenu:")
        print("1️⃣  Log a Trip")
        print("2️⃣  Show Logged Trips & Total CO2")
        print("3️⃣  Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            log_trip()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye! 🌱 Keep travel eco-friendly!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
