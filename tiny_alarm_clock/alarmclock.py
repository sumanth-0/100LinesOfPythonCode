import datetime
import time
import winsound  # For playing simple beeps on Windows

def play_tune():
    """Plays a short happy tune when the alarm rings 🎶"""
    notes = [
        (659, 200), (659, 200), (0, 150), (659, 200),  # E E pause E
        (523, 200), (659, 200), (784, 400), (392, 400)  # C E G C
    ]
    for freq, dur in notes:
        if freq == 0:
            time.sleep(dur / 1000.0)
        else:
            winsound.Beep(freq, dur)

def alarm_clock(set_hour, set_minute):
    print(f"✅ Alarm set for {set_hour:02d}:{set_minute:02d}. Waiting...")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == set_hour and current_minute == set_minute:
            print("\n🔔🔔 Wake Up! 🔔🔔")
            play_tune()
            break

        time.sleep(10)

if __name__ == "__main__":
    print("=== 🎵 Simple Python Alarm Clock ===")
    try:
        hour = int(input("⏰ Enter hour (0–23): "))
        minute = int(input("⏰ Enter minute (0–59): "))
        alarm_clock(hour, minute)
    except ValueError:
        print("⚠️ Please enter valid numeric values for hour and minute.")
