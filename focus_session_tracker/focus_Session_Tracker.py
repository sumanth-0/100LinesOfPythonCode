import time

def log_session(times, breaks):
    print("Today's Focus Sessions:")
    for idx, (focus, brk) in enumerate(zip(times, breaks), 1):
        print(f"Session {idx}: {focus} min, Break: {brk} min")
    if not times:
        print("No sessions logged today.")

def tracker():
    focus_times, break_times = [], []
    session = 1
    while True:
        try:
            focus = int(input(f"Focus Session {session} minutes (default 25): ") or 25)
            print(f"Starting focus: {focus} min")
            for i in range(focus * 60):
                if i % 60 == 0: print(f"{focus-i//60} min left...", end="\r")
                time.sleep(1)
            print("Focus session ended! Time for a break.")
            brk = int(input("Break minutes (default 5): ") or 5)
            print(f"Break: {brk} min")
            for i in range(brk * 60):
                if i % 60 == 0: print(f"{brk-i//60} min left...", end="\r")
                time.sleep(1)
            print("Break complete!")
            focus_times.append(focus)
            break_times.append(brk)
            more = input("Log another session? (y/n): ").strip().lower()
            if more != 'y':
                break
            session += 1
        except Exception: break
    log_session(focus_times, break_times)

def main():
    print("Focus Session Tracker")
    tracker()

if __name__ == "__main__":
    main()
