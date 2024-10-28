import requests

class Pet:
    """Class representing a pet available for adoption."""
    def __init__(self, name, species, age, location):
        self.name = name
        self.species = species
        self.age = age
        self.location = location

    def __str__(self):
        """Return a string representation of the pet."""
        return f"{self.name} - {self.species}, {self.age} years old, located in {self.location}"

class PetAdoptionFinder:
    """Class to find pets available for adoption based on user preference."""
    def __init__(self):
        self.pets = []

    def fetch_pets(self, location):
        """Fetch pets available for adoption from an online source."""
        # Example API call - replace with a real API
        api_url = f"https://api.example.com/pets?location={location}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            for pet in data['pets']:
                self.pets.append(Pet(pet['name'], pet['species'], pet['age'], pet['location']))
        else:
            print("Error fetching data.")

    def show_pets(self):
        """Display all pets available for adoption."""
        if not self.pets:
            print("No pets found for adoption.")
            return
        for pet in self.pets:
            print(pet)

def main():
    """Main function to interact with the user."""
    finder = PetAdoptionFinder()
    
    location = input("Enter your location to find pets available for adoption: ")
    finder.fetch_pets(location)
    finder.show_pets()

if __name__ == "__main__":
    main()
