"""
Break Reminder — A simple cross-platform Python script
that reminds you to take a break every hour based on system uptime.

✅ Works on Windows, macOS, and Linux
✅ Uses only the Python standard library
✅ Under 100 lines and well-commented
"""

import time
import platform
import ctypes
import os
import sys
import datetime
import subprocess

def get_uptime_seconds():
    """Return the system uptime in seconds for the current OS."""
    system = platform.system()

    try:
        if system == "Windows":
            # Windows: milliseconds since last boot
            return ctypes.windll.kernel32.GetTickCount64() / 1000

        elif system == "Linux":
            # Linux: read uptime from /proc/uptime
            with open("/proc/uptime", "r") as f:
                return float(f.readline().split()[0])

        elif system == "Darwin":
            # macOS: use sysctl to get boot time
            boot_time = subprocess.check_output(["sysctl", "-n", "kern.boottime"]).decode()
            sec = int(boot_time.split("sec =")[1].split(",")[0])
            boot = datetime.datetime.fromtimestamp(sec)
            return (datetime.datetime.now() - boot).total_seconds()

        else:
            raise NotImplementedError("Unsupported OS")

    except Exception as e:
        print("Error detecting uptime:", e)
        return 0


def notify(message):
    """Display a cross-platform notification with the given message."""
    system = platform.system()

    if system == "Windows":
        ctypes.windll.user32.MessageBoxW(0, message, "Break Reminder", 0x40)
    elif system == "Darwin":
        os.system(f'''osascript -e 'display notification "{message}" with title "Break Reminder"' ''')
    else:  # Linux
        os.system(f'notify-send "Break Reminder" "{message}"')


def main():
    """Main loop — checks uptime and reminds user every hour."""
    print("☕ Break Reminder started! You'll be notified every hour.\n")

    last_reminder = 0  # Tracks how many hours have passed

    while True:
        uptime = get_uptime_seconds()
        hours_on = int(uptime // 3600)
        mins_on = int((uptime % 3600) // 60)

        # Show live uptime in the terminal
        sys.stdout.write(f"\rSystem on for {hours_on}h {mins_on}m")
        sys.stdout.flush()

        # Send a reminder every hour
        if uptime // 3600 > last_reminder:
            notify("You’ve been working for an hour! Time to take a short break ☕")
            last_reminder += 1

        time.sleep(30)  # Check every 30 seconds


if __name__ == "__main__":
    main()
