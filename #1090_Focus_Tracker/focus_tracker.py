
import time
import datetime
import os

work_total = 0
break_total = 0
session_start = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_time(minutes, seconds):
    digits = {
        '0': ["███", "█ █", "█ █", "█ █", "███"],
        '1': [" █ ", "██ ", " █ ", " █ ", "███"],
        '2': ["███", "  █", "███", "█  ", "███"],
        '3': ["███", "  █", "███", "  █", "███"],
        '4': ["█ █", "█ █", "███", "  █", "  █"],
        '5': ["███", "█  ", "███", "  █", "███"],
        '6': ["███", "█  ", "███", "█ █", "███"],
        '7': ["███", "  █", "  █", "  █", "  █"],
        '8': ["███", "█ █", "███", "█ █", "███"],
        '9': ["███", "█ █", "███", "  █", "███"],
        ':': [" ", "█", " ", "█", " "]
    }
    
    time_str = f"{minutes:02d}:{seconds:02d}"
    for row in range(5):
        line = ""
        for char in time_str:
            line += digits[char][row] + " "
        print(line)

def live_timer(session_type):
    global work_total, break_total, session_start
    session_start = time.time()
    
    try:
        while True:
            elapsed = int(time.time() - session_start)
            minutes = elapsed // 60
            seconds = elapsed % 60
            
            clear_screen()
            print(f"=== {session_type.upper()} SESSION ===")
            ascii_time(minutes, seconds)
            print(f"\nPress Ctrl+C to {'take a break' if session_type == 'work' else 'resume work'}")
            print(f"\nTotal work today: {work_total//60}m {work_total%60}s")
            print(f"Total break today: {break_total//60}m {break_total%60}s")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        elapsed = int(time.time() - session_start)
        if session_type == 'work':
            work_total += elapsed
        else:
            break_total += elapsed
        return elapsed

def main():
    global work_total, break_total
    print("Productivity Time Tracker")
    print("Press Ctrl+C during session to switch modes")
    print("=" * 40)
    
    mode = 'work'
    
    while True:
        if mode == 'work':
            print(f"\n1. Start work session")
            print(f"2. View stats")
            print(f"3. Exit")
            choice = input("Option (1-3): ")
            
            if choice == '1':
                duration = live_timer('work')
                print(f"\nWork session: {duration//60}m {duration%60}s")
                mode = 'break'
            elif choice == '2':
                print(f"\nTotal work: {work_total//60}m {work_total%60}s")
                print(f"Total break: {break_total//60}m {break_total%60}s")
            elif choice == '3':
                break
        
        else:  # break mode
            print(f"\n1. Start break")
            print(f"2. Resume work")
            print(f"3. Exit")
            choice = input("Option (1-3): ")
            
            if choice == '1':
                duration = live_timer('break')
                print(f"\nBreak time: {duration//60}m {duration%60}s")
                mode = 'work'
            elif choice == '2':
                mode = 'work'
            elif choice == '3':
                break
    
    print("Session complete!")
    print(f"Final stats - Work: {work_total//60}m, Break: {break_total//60}m")

if __name__ == "__main__":
    main()







