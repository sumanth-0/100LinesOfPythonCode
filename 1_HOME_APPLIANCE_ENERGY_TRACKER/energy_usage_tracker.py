class Appliance:
    def __init__(self, name, power, hours_per_day):
        self.name = name
        self.power = power  # in watts
        self.hours_per_day = hours_per_day

    def daily_energy(self):
        return (self.power * self.hours_per_day) / 1000  # kWh

    def weekly_energy(self):
        return self.daily_energy() * 7

    def monthly_energy(self):
        return self.daily_energy() * 30

def main():
    appliances = []
    
    print("Home Appliance Energy Usage Tracker")
    while True:
        name = input("Enter appliance name (or 'done' to stop): ")
        if name.lower() == 'done':
            break
        try:
            power = float(input("Enter power in watts: "))
            hours_per_day = float(input("Enter hours used per day: "))
            appliance = Appliance(name, power, hours_per_day)
            appliances.append(appliance)
        except ValueError:
            print("Invalid input. Please enter numbers for power and hours.")
        
    print("\nEnergy Usage Report (kWh):")
    for appliance in appliances:
        print(f"{appliance.name}: Daily: {appliance.daily_energy():.2f}, Weekly: {appliance.weekly_energy():.2f}, Monthly: {appliance.monthly_energy():.2f}")

if __name__ == "__main__":
    main()
