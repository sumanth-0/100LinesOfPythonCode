import time
import threading

class CookingTimer:
    def __init__(self):
        self.timers = []

    def start_timer(self, duration, timer_name):
        """Starts a timer for a given duration in seconds."""
        print(f"Starting timer '{timer_name}' for {duration} seconds.")
        time.sleep(duration)
        print(f"Timer '{timer_name}' finished! 🎉")
    
    def add_timer(self, duration, timer_name):
        """Adds a new timer to the list and starts it in a new thread."""
        timer_thread = threading.Thread(target=self.start_timer, args=(duration, timer_name))
        timer_thread.start()
        self.timers.append(timer_thread)

def main():
    cooking_timer = CookingTimer()
    
    while True:
        try:
            duration = int(input("Enter timer duration in seconds (or type -1 to exit): "))
            if duration == -1:
                print("Exiting the Cooking Timer.")
                break
            timer_name = input("Enter a name for this timer: ")
            cooking_timer.add_timer(duration, timer_name)
        except ValueError:
            print("Please enter a valid number for the duration.")

if __name__ == "__main__":
    main()
