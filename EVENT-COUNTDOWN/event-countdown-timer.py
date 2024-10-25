import time
from datetime import datetime

class EventCountdownTimer:
    def __init__(self, event_date):
        self.event_date = event_date

    def countdown(self):
        while True:
            now = datetime.now()
            remaining_time = self.event_date - now

            if remaining_time.total_seconds() <= 0:
                print("Event has started!")
                break

            days, seconds = remaining_time.days, remaining_time.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            print(f"\rTime until event: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")
            time.sleep(1)

def main():
    event_input = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
    event_date = datetime.strptime(event_input, "%Y-%m-%d %H:%M:%S")
    timer = EventCountdownTimer(event_date)
    timer.countdown()

if __name__ == "__main__":
    main()
