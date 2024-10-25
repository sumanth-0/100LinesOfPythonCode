import time
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing!")
            winsound.Beep(1000, 2000)  # Ring for 2 seconds
            return

def main():
    alarm_time = input("Enter the alarm time (HH:MM, 24-hour format): ")
    snooze_time = 5  # snooze duration in minutes

    while True:
        set_alarm(alarm_time)

        snooze = input("Press 's' to snooze for 5 minutes, or any other key to stop: ")
        if snooze.lower() == 's':
            print(f"Snoozing for {snooze_time} minutes...")
            time.sleep(snooze_time * 60)  # snooze duration
        else:
            print("Alarm stopped.")
            break

if __name__ == "__main__":
    main()
