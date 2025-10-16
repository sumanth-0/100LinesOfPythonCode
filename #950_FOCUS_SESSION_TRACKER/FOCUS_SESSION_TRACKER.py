import sys
import time
from datetime import timedelta

def run_timer(minutes, label):
    total_seconds = int(minutes * 60)
    
    try:
        for s in reversed(range(total_seconds)):
            mins, secs = divmod(s, 60)
            timer_display = f'{label}: {mins:02d}:{secs:02d}'
            
            sys.stdout.write(f'\r{timer_display} ')
            sys.stdout.flush()
            
            time.sleep(1)
            
        sys.stdout.write(f'\r{" " * 30}\r')
        print(f"{label} session complete.")
        return True
        
    except KeyboardInterrupt:
        print("\n\nTimer cancelled by user.")
        return False

def main():
    total_productive_seconds = 0
    print("--- Focus & Break Timer ---")
    
    while True:
        action = input("\nAction? (f)ocus, (b)reak, (q)uit: ").lower().strip()
        
        if action == 'q':
            break
            
        elif action in ['f', 'b']:
            label = "Focus" if action == 'f' else "Break"
            
            try:
                duration_str = input(f"Enter duration for {label} (minutes): ")
                duration_minutes = float(duration_str)
                
                if duration_minutes <= 0:
                    print("Error: Please enter a positive number for minutes.")
                    continue
                    
            except ValueError:
                print("Error: Invalid input. Please enter a numerical value.")
                continue

            completed = run_timer(duration_minutes, label)
            
            if completed and action == 'f':
                total_productive_seconds += duration_minutes * 60
                
        else:
            print("Invalid action. Please choose 'f', 'b', or 'q'.")

    print("\n--------------------------")
    if total_productive_seconds > 0:
        formatted_time = str(timedelta(seconds=int(total_productive_seconds)))
        print(f"Total Productive Time: {formatted_time}")
    else:
        print("No productive time was tracked.")
    print("Goodbye.")
    
if __name__ == "__main__":
    main()