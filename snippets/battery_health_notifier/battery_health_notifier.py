#!/usr/bin/env python3
"""
Battery Health Notifier
Monitors battery health and sends notifications based on battery status
Requires: psutil, plyer (for notifications)
"""

import psutil
import time
import sys

try:
    from plyer import notification
    NOTIFICATIONS_AVAILABLE = True
except ImportError:
    NOTIFICATIONS_AVAILABLE = False
    print("Warning: plyer not installed. Install with: pip install plyer")


def get_battery_info():
    """Get current battery information"""
    if not hasattr(psutil, "sensors_battery"):
        return None
    
    battery = psutil.sensors_battery()
    if battery is None:
        return None
    
    return {
        'percent': battery.percent,
        'plugged': battery.power_plugged,
        'time_left': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None
    }


def format_time(seconds):
    """Format seconds to human readable time"""
    if seconds is None or seconds < 0:
        return "Unknown"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{int(hours)}h {int(minutes)}m"


def send_notification(title, message):
    """Send desktop notification"""
    if NOTIFICATIONS_AVAILABLE:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='Battery Health Notifier',
                timeout=10
            )
        except Exception as e:
            print(f"Notification error: {e}")
    print(f"[{title}] {message}")


def monitor_battery(check_interval=60, low_threshold=20, high_threshold=80):
    """Monitor battery and send notifications"""
    print("Battery Health Notifier Started")
    print(f"Low threshold: {low_threshold}%, High threshold: {high_threshold}%")
    print(f"Checking every {check_interval} seconds...\n")
    
    last_status = {'low_notified': False, 'high_notified': False, 'full_notified': False}
    
    while True:
        try:
            battery_info = get_battery_info()
            
            if battery_info is None:
                print("No battery detected. Exiting...")
                sys.exit(1)
            
            percent = battery_info['percent']
            plugged = battery_info['plugged']
            time_left = battery_info['time_left']
            
            status = "Charging" if plugged else "Discharging"
            time_str = format_time(time_left) if time_left else "N/A"
            print(f"Battery: {percent}% | {status} | Time remaining: {time_str}")
            
            # Low battery warning
            if not plugged and percent <= low_threshold and not last_status['low_notified']:
                send_notification("Low Battery Warning", f"Battery at {percent}%. Please charge soon.")
                last_status['low_notified'] = True
            elif percent > low_threshold:
                last_status['low_notified'] = False
            
            # High charge notification
            if plugged and percent >= high_threshold and not last_status['high_notified']:
                send_notification("Battery Charged", f"Battery at {percent}%. Consider unplugging.")
                last_status['high_notified'] = True
            elif percent < high_threshold:
                last_status['high_notified'] = False
            
            time.sleep(check_interval)
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(check_interval)


if __name__ == "__main__":
    monitor_battery()
