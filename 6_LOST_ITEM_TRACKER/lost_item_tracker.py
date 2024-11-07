import time

class LostItem:
    def __init__(self, name, description, last_location):
        self.name = name
        self.description = description
        self.last_location = last_location
        self.date_logged = time.time()

    def days_since_lost(self):
        return int((time.time() - self.date_logged) / (60 * 60 * 24))

    def display_item_info(self):
        print(f"\nItem: {self.name}")
        print(f"Description: {self.description}")
        print(f"Last Known Location: {self.last_location}")
        print(f"Days Since Lost: {self.days_since_lost()}")

def check_common_spots():
    spots = ["Car", "Desk", "Bag", "Jacket Pockets"]
    print("\nRemember to check these common spots:")
    for spot in spots:
        print(f" - {spot}")

def main():
    items = []
    print("Welcome to the Lost Item Tracker!")
    
    while True:
        name = input("\nEnter the lost item name: ").strip()
        description = input("Enter a description: ").strip()
        last_location = input("Enter the last known location: ").strip()
        lost_item = LostItem(name, description, last_location)
        items.append(lost_item)
        
        lost_item.display_item_info()
        check_common_spots()
        
        another = input("\nWould you like to log another item? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("\nThank you for using the Lost Item Tracker!")

if __name__ == "__main__":
    main()
