
import time
import sched

class PetFeedingReminder:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.feedings = []

    def add_feeding(self, pet_name, feeding_time):
        self.feedings.append((pet_name, feeding_time))
        self.scheduler.enterabs(feeding_time, 1, self.send_reminder, argument=(pet_name,))
        print(f"Reminder set for {pet_name} at {time.ctime(feeding_time)}")

    def send_reminder(self, pet_name):
        print(f"\nTime to feed {pet_name}!")

    def start(self):
        print("Feeding reminder system started.")
        self.scheduler.run()

def main():
    reminder = PetFeedingReminder()
    
    while True:
        pet_name = input("\nEnter the pet's name (or 'quit' to exit): ")
        if pet_name.lower() == 'quit':
            break
        feeding_time = int(input("Enter feeding time in seconds from now: ")) + time.time()
        reminder.add_feeding(pet_name, feeding_time)

    reminder.start()

if __name__ == "__main__":
    main()
