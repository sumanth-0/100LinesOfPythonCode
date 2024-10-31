
class TravelBucketList:
    def __init__(self):
        self.destinations = {}

    def add_destination(self, destination, notes=""):
        self.destinations[destination] = {'visited': False, 'notes': notes, 'rating': None}

    def mark_visited(self, destination, rating=None):
        if destination in self.destinations:
            self.destinations[destination]['visited'] = True
            if rating is not None:
                self.destinations[destination]['rating'] = rating

    def display_list(self):
        for destination, details in self.destinations.items():
            status = "Visited" if details['visited'] else "Not Visited"
            print(f"{destination}: {status}, Notes: {details['notes']}, Rating: {details['rating']}")

if __name__ == "__main__":
    bucket_list = TravelBucketList()
    
    while True:
        action = input("Choose action: add, visit, view, or quit: ").strip().lower()
        
        if action == "add":
            dest = input("Enter destination name: ")
            notes = input("Enter any notes: ")
            bucket_list.add_destination(dest, notes)
        
        elif action == "visit":
            dest = input("Enter destination name to mark as visited: ")
            rating = input("Enter rating (1-5) or leave blank: ")
            bucket_list.mark_visited(dest, rating if rating else None)
        
        elif action == "view":
            bucket_list.display_list()
        
        elif action == "quit":
            break
        
        else:
            print("Invalid action. Please try again.")
