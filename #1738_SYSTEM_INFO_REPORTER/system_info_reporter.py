import psutil
import time
import os

def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        while True: 
            cpu, ram, disk = get_system_usage()
            clear_screen()
            print("==== System Usage Monitor ====")
            print(f"CPU Usage  : {cpu}%")
            print(f"RAM Usage  : {ram}%")
            print(f"Disk Usage : {disk}%")
            print("\nPress Ctrl+C to exit.")
            time.sleep(1)
    except KeyboardInterrupt:
        clear_screen()
        print("Exiting System Monitor...")

if __name__ == "__main__":
    main()