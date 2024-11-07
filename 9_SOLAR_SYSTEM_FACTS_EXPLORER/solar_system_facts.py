
class SolarSystemFactsExplorer:
    def __init__(self):
        self.solar_system_data = {
            "Mercury": {
                "facts": "Mercury is the smallest planet in the Solar System.",
                "distance_from_sun": "57.9 million km",
                "radius": "2,439.7 km",
                "day_length": "58.6 Earth days"
            },
            "Venus": {
                "facts": "Venus has the longest rotation period of any planet.",
                "distance_from_sun": "108.2 million km",
                "radius": "6,051.8 km",
                "day_length": "243 Earth days"
            },
            "Earth": {
                "facts": "Earth is the only planet known to support life.",
                "distance_from_sun": "149.6 million km",
                "radius": "6,371 km",
                "day_length": "24 hours"
            },
            # Add more planets with similar details
        }

    def display_fact(self, planet_name):
        planet = self.solar_system_data.get(planet_name)
        if planet:
            print(f"\n{planet_name} Facts:")
            for key, value in planet.items():
                print(f"{key}: {value}")
        else:
            print("Planet not found. Please enter a valid planet name.")

if __name__ == "__main__":
    explorer = SolarSystemFactsExplorer()
    print("Welcome to the Solar System Facts Explorer!")
    while True:
        planet = input("Enter the name of a planet (or 'exit' to quit): ").capitalize()
        if planet == "Exit":
            break
        explorer.display_fact(planet)
