import time
import sys

def pomodoro_timer(minutes):
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        
        sys.stdout.write(f"\rTime Remaining: {timer_display}")
        sys.stdout.flush()
        
        time.sleep(1)
        total_seconds -= 1
        
    print(f"\nTime's up! Take a break. \a")

if __name__ == "__main__":
    print("--- Pomodoro Timer Started ---")
    
    work_minutes = 25
    pomodoro_timer(work_minutes)
    
    break_minutes = 5
    print(f"\n--- Starting {break_minutes}-minute break ---")
    pomodoro_timer(break_minutes)

    print("\nPomodoro session complete!")