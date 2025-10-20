import time

def timer(minutes, label):
    secs = minutes * 60
    print(f"{label} for {minutes} minutes.")
    while secs:
        mins, sec = divmod(secs, 60)
        print(f"{label} - {mins:02d}:{sec:02d}", end='\r')
        time.sleep(1)
        secs -= 1
    print(f"\n{label} finished! Take a break.")

def pomodoro(sessions=4, focus=25, short_break=5, long_break=15):
    for i in range(1, sessions + 1):
        timer(focus, f"Session {i}")
        if i < sessions:
            timer(short_break, "Short Break")
        else:
            timer(long_break, "Long Break")
    print("All focus sessions complete.")

def main():
    print("Focus Timer (Pomodoro)")
    try:
        sessions = int(input("How many sessions?: ") or 4)
        focus = int(input("Focus minutes (default 25): ") or 25)
        short_break = int(input("Short break minutes (default 5): ") or 5)
        long_break = int(input("Long break minutes (default 15): ") or 15)
    except Exception:
        print("Invalid input, using defaults.")
        sessions, focus, short_break, long_break = 4, 25, 5, 15
    pomodoro(sessions, focus, short_break, long_break)

if __name__ == "__main__":
    main()
