import os
os.system("pip install -q psutil")
import psutil
import time

def display_usage():
    print(f"{'Time':^12} {'CPU %':^12} {'Memory %':^12}")
    print("-" * 40)
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage over 1 second
            memory_percent = psutil.virtual_memory().percent  # Memory usage
            current_time = time.strftime("%H:%M:%S")
            print(f"{current_time:^12} {cpu_percent:^12} {memory_percent:^12}")
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    print("Starting CPU and RAM usage monitor. Press Ctrl+C to stop.\n\n")
    display_usage()
