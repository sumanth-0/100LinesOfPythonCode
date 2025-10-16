# focus_session_tracker.py
# Tracks focus sessions and breaks, shows total productive time

from pyfiglet import figlet_format
from datetime import timedelta

class FocusSessionTracker:
    def __init__(self):
        self.sessions = []
        self.breaks = []

    def add_session(self, minutes):
        """Add a focused session in minutes"""
        self.sessions.append(minutes)
        print(figlet_format("FOCUS SESSION", font="slant"))
        print(f"Added focus session: {minutes} minutes")

    def add_break(self, minutes):
        """Add a break in minutes"""
        self.breaks.append(minutes)
        print(figlet_format("BREAK TIME", font="slant"))
        print(f"Added break: {minutes} minutes")

    def total_focus_time(self):
        """Calculate total productive time"""
        return sum(self.sessions)

    def total_break_time(self):
        """Calculate total break time"""
        return sum(self.breaks)

# Example usage
if __name__ == "__main__":
    tracker = FocusSessionTracker()
    tracker.add_session(25)
    tracker.add_break(5)
    tracker.add_session(30)
    print("\nSummary:")
    print("Total Focus Time:", tracker.total_focus_time(), "minutes")
    print("Total Break Time:", tracker.total_break_time(), "minutes")
