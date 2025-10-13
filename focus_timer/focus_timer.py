#!/usr/bin/env python3
"""Focus Timer - A Pomodoro/focus timer CLI that counts down and notifies at end."""

import time
import sys
import argparse
from datetime import timedelta

try:
    import plyer
    NOTIFICATIONS_AVAILABLE = True
except ImportError:
    NOTIFICATIONS_AVAILABLE = False
    print("Warning: plyer not installed. Install with 'pip install plyer' for notifications.")


def clear_line():
    """Clear the current terminal line."""
    sys.stdout.write('\r' + ' ' * 80 + '\r')
    sys.stdout.flush()


def format_time(seconds):
    """Format seconds into MM:SS format."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"


def notify(title, message):
    """Send system notification if available."""
    if NOTIFICATIONS_AVAILABLE:
        try:
            plyer.notification.notify(title=title, message=message, timeout=10)
        except Exception as e:
            print(f"\nNotification failed: {e}")
    else:
        print(f"\n🔔 {title}: {message}")


def countdown_timer(duration_minutes, label="Focus Session"):
    """Run a countdown timer for the specified duration."""
    total_seconds = duration_minutes * 60
    
    print(f"\n{'='*50}")
    print(f"  {label} - {duration_minutes} minutes")
    print(f"{'='*50}\n")
    
    try:
        for remaining in range(total_seconds, 0, -1):
            time_str = format_time(remaining)
            progress = int((total_seconds - remaining) / total_seconds * 40)
            bar = '█' * progress + '░' * (40 - progress)
            
            sys.stdout.write(f'\r⏱️  {time_str} [{bar}]')
            sys.stdout.flush()
            time.sleep(1)
        
        clear_line()
        print(f"\n✅ {label} completed!\n")
        notify("Timer Complete!", f"{label} ({duration_minutes} min) finished!")
        
    except KeyboardInterrupt:
        clear_line()
        print(f"\n⏸️  Timer paused. Time remaining: {format_time(remaining)}\n")
        sys.exit(0)


def main():
    """Main function to parse arguments and run the timer."""
    parser = argparse.ArgumentParser(
        description="Focus Timer - A Pomodoro/focus timer CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  %(prog)s                    # Default 25-minute Pomodoro\n"
               "  %(prog)s --duration 50      # 50-minute focus session\n"
               "  %(prog)s -d 5 -l Break      # 5-minute break\n"
    )
    
    parser.add_argument('-d', '--duration', type=int, default=25,
                        help='Duration in minutes (default: 25)')
    parser.add_argument('-l', '--label', type=str, default='Focus Session',
                        help='Label for the timer session (default: Focus Session)')
    
    args = parser.parse_args()
    
    if args.duration <= 0:
        print("Error: Duration must be positive.")
        sys.exit(1)
    
    countdown_timer(args.duration, args.label)


if __name__ == '__main__':
    main()
