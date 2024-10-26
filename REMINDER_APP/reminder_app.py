import time
import threading

class ReminderApp:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, message, delay):
        def notify():
            time.sleep(delay)
            print(f"Reminder: {message}")
        threading.Thread(target=notify).start()

    def add_reminder(self):
        message = input("Enter reminder message: ")
        delay = int(input("Enter time in seconds before reminder: "))
        self.reminders.append(message)
        self.set_reminder(message, delay)

def main():
    app = ReminderApp()
    
    while True:
        app.add_reminder()
        cont = input("Do you want to add another reminder? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
