import time

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"{label} for {minutes} minutes...")
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"{label} ended.")

def pomodoro_timer(work_minutes=25, short_break=5, long_break=15, cycles=4):
    for i in range(1, cycles + 1):
        countdown(work_minutes, "Work")
        if i < cycles:
            countdown(short_break, "Short break")
        else:
            countdown(long_break, "Long break")

if __name__ == "__main__":
    pomodoro_timer()
