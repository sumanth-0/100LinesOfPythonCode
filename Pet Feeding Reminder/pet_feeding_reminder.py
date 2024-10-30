import datetime
import time
import threading

class PetFeeder:
    def __init__(self):
        self.feed_log = []  # Log for tracking feeding times and instructions

    def add_feeding_reminder(self, pet_name, feeding_time, instructions):
        """Add a feeding reminder with specified time and instructions."""
        today_date = datetime.datetime.now().date()
        # Combine today's date with the feeding time
        full_feeding_time = datetime.datetime.strptime(f"{today_date} {feeding_time}", '%Y-%m-%d %H:%M')
        
        reminder = {
            'pet_name': pet_name,
            'feeding_time': full_feeding_time,
            'instructions': instructions,
            'logged_time': datetime.datetime.now(),
            'alarm_triggered': False  # Track if alarm has been triggered
        }
        self.feed_log.append(reminder)
        print(f"Reminder set for {pet_name} at {full_feeding_time} with instructions: '{instructions}'")

    def show_feed_log(self):
        """Display the feeding log."""
        if not self.feed_log:
            print("No feeding logs available.")
            return
        print("\nFeeding Log:")
        for log in self.feed_log:
            print(f"Pet: {log['pet_name']}, Time: {log['feeding_time']}, Instructions: {log['instructions']}, Logged at: {log['logged_time']}")

    def alarm_check(self):
        """Periodically checks if any feeding time is due and triggers an alarm."""
        while True:
            now = datetime.datetime.now()
            for log in self.feed_log:
                # Check if it's time to feed and the alarm hasn't been triggered
                if log['feeding_time'] <= now and not log['alarm_triggered']:
                    print(f"\nALERT: Time to feed {log['pet_name']}! Instructions: {log['instructions']}")
                    log['alarm_triggered'] = True  # Mark this alarm as triggered to avoid duplicate alerts
            time.sleep(60)  # Check every minute

def main():
    pet_feeder = PetFeeder()
    
    # Start the alarm check in a separate thread
    alarm_thread = threading.Thread(target=pet_feeder.alarm_check, daemon=True)
    alarm_thread.start()

    while True:
        print("\n--- Pet Feeding Reminder System ---")
        pet_name = input("Enter your pet's name (or 'exit' to quit): ")
        if pet_name.lower() == 'exit':
            break

        feeding_time = input("Enter the feeding time (e.g., '18:00'): ")
        try:
            # Validate the feeding time format
            datetime.datetime.strptime(feeding_time, '%H:%M')
        except ValueError:
            print("Invalid time format. Please use 'HH:MM'.")
            continue

        instructions = input("Enter any special feeding instructions (or press Enter to skip): ")
        pet_feeder.add_feeding_reminder(pet_name, feeding_time, instructions)

        # Option to add another feeding time for the same pet
        another_time = input("Would you like to add another feeding time for this pet? (yes/no): ")
        while another_time.lower() == 'yes':
            feeding_time = input("Enter the feeding time (e.g., '18:00'): ")
            try:
                feeding_time = feeding_time.strip()  # Ensure there are no leading/trailing spaces
                datetime.datetime.strptime(feeding_time, '%H:%M')  # Re-validate the time format
            except ValueError:
                print("Invalid time format. Please use 'HH:MM'.")
                continue

            instructions = input("Enter any special feeding instructions (or press Enter to skip): ")
            pet_feeder.add_feeding_reminder(pet_name, feeding_time, instructions)
            another_time = input("Would you like to add another feeding time for this pet? (yes/no): ")

        view_log = input("Would you like to view the feeding log? (yes/no): ")
        if view_log.lower() == 'yes':
            pet_feeder.show_feed_log()

if __name__ == "__main__":
    main()
