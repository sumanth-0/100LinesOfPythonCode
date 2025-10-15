# focus_session_tracker.py
# Tracks focus sessions and breaks, shows total productive time

class FocusSessionTracker:
    def __init__(self):
        self.sessions = []
        self.breaks = []

    def add_session(self, minutes):
        """Add a focused session in minutes"""
        self.sessions.append(minutes)

    def add_break(self, minutes):
        """Add a break in minutes"""
        self.breaks.append(minutes)

    def total_focus_time(self):
        """Calculate total productive time"""
        return sum(self.sessions)

# Example usage
if __name__ == "__main__":
    tracker = FocusSessionTracker()
    tracker.add_session(25)
    tracker.add_break(5)
    tracker.add_session(30)
    print("Total Focus Time:", tracker.total_focus_time(), "minutes")
