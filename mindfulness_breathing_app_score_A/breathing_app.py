import time

class BreathingApp:
    def __init__(self):
        self.breathing_cycle = 5  # seconds for inhale and exhale

    def inhale(self):
        print("Inhale...")
        time.sleep(self.breathing_cycle)
        print("Hold...")
        time.sleep(2)

    def exhale(self):
        print("Exhale...")
        time.sleep(self.breathing_cycle)
        print("Hold...")
        time.sleep(2)

    def start_breathing_session(self, cycles=5):
        for _ in range(cycles):
            self.inhale()
            self.exhale()
        print("Breathing session complete. Well done!")

def main():
    """Main function to start the mindfulness breathing app."""
    cycles = int(input("Enter the number of breathing cycles you want (default 5): ") or 5)
    app = BreathingApp()
    app.start_breathing_session(cycles)

if __name__ == "__main__":
    main()
