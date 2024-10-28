class ScavengerHunt:
    def __init__(self):
        self.locations = {}
        self.progress = []

    def add_location(self, clue, location):
        """Add a clue and corresponding location."""
        self.locations[clue] = location

    def show_clues(self):
        """Display available clues."""
        print("Available Clues:")
        for clue in self.locations.keys():
            print(f"- {clue}")

    def check_location(self, clue, answer):
        """Check if the user's answer is correct."""
        if clue in self.locations and self.locations[clue].lower() == answer.lower():
            print("Correct! You've found the location!")
            self.progress.append(clue)
        else:
            print("Try again!")

    def show_progress(self):
        """Display the user's progress."""
        print("Your progress:")
        for clue in self.progress:
            print(f"- {clue}")

def main():
    """Main function to run the scavenger hunt."""
    hunt = ScavengerHunt()
    hunt.add_location("Near the big oak tree", "Park")
    hunt.add_location("Where the sun sets", "Beach")
    hunt.add_location("The tallest building", "Downtown")

    while True:
        hunt.show_clues()
        clue = input("Enter a clue you want to check: ")
        answer = input("Where do you think it leads? ")
        hunt.check_location(clue, answer)
        hunt.show_progress()

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
