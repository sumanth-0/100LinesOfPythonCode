import time, random, pygame, os
from datetime import datetime

class AlarmClock:
    def __init__(self):
        # Initialize the pygame audio mixer for playing sounds
        pygame.mixer.init()        
        # Get the absolute path to the 'sounds' directory next to our script
        # os.path.dirname gets the directory containing the script
        # os.path.join combines paths safely for any operating system
        sounds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds')
        # Dictionary mapping sound names to their full file paths, You can add or modify sound files here
        self.alarm_tones = {
            'beep': os.path.join(sounds_dir, 'beep.mp3'),
            'birds': os.path.join(sounds_dir, 'birds.mp3'),
            'TinSing': os.path.join(sounds_dir, 'TinSing.mp3')
        }
        # List to store all active alarms
        self.alarms = []
        # Check and display the status of each sound file ✅ means file exists, ❌ means file is missing
        print("\nSound files status:")
        for tone, path in self.alarm_tones.items():
            print(f"{'✅' if os.path.exists(path) else '❌'} {tone}: {path}")

    def add_alarm(self, time_str, tone=None):
        """ Add a new alarm with an optional specific sound
            Parameters: time_str: String in "HH:MM" format (24-hour), tone: Optional name of the sound to play (default: random) """
        try:
            # Convert string time (e.g., "09:30") to a time object
            alarm_time = datetime.strptime(time_str, "%H:%M").time()
            # Add new alarm to our list with specified or default random tone
            self.alarms.append({'time': alarm_time, 'tone': tone})
            # Confirm alarm was set successfully
            print(f"Alarm set for {time_str}" + (f" with {tone} sound" if tone else " with random sound"))
        except ValueError:
            print("Invalid time format. Use HH:MM")
    def play_alarm(self, tone=None):
        """ Play the alarm sound
        Parameters:
            tone: Optional specific sound to play (default: random) """
        try:
            # Choose specified tone or random if none specified, The ternary operator 'a if condition else b' is used here
            sound_file = self.alarm_tones[tone] if tone in self.alarm_tones else random.choice(list(self.alarm_tones.values()))
            # Check if the selected sound file exists
            if os.path.exists(sound_file):
                print(f"🔔 ALARM! Playing: {sound_file}")
                # Load and play the sound file
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                # Keep the sound playing for 30 seconds
                time.sleep(30)
                # Stop the sound after 30 seconds
                pygame.mixer.music.stop()
            else:
                # If sound file is missing, show warning and make system beep (\a)
                print(f"⚠️ Sound file not found: {sound_file}\n\a")
        except Exception as e:
            # If any error occurs during playback, show error and make system beep
            print(f"Error playing sound: {e}\n\a")
    def check_alarms(self):
        """Check all alarms and trigger any that match current time"""
        # Get the current time
        current_time = datetime.now().time()
        # Check each alarm in our list, Using [:] creates a copy of the list so we can safely remove items
        for alarm in self.alarms[:]:
            # If alarm hour and minute match current time
            if current_time.hour == alarm['time'].hour and current_time.minute == alarm['time'].minute:
                self.play_alarm(alarm['tone'])
                # Remove the alarm after it's triggered
                self.alarms.remove(alarm)
    def run(self):
        """Start the alarm clock and keep it running until interrupted"""
        print("\nAlarm Clock Running... (Press Ctrl+C to exit)")
        # Show all currently set alarms in HH:MM format
        print(f"Current alarms: " + ", ".join([f"{a['time'].strftime('%H:%M')} ({a['tone'] or 'random'})" for a in self.alarms]))
        try:
            # Infinite loop to keep checking alarms
            while True:
                self.check_alarms()
                # Wait 30 seconds before next check (saves CPU usage)
                time.sleep(30)
        except KeyboardInterrupt:
            # When user presses Ctrl+C, clean up and exit
            print("\nAlarm Clock stopped.")
            pygame.mixer.quit()

def main():
    # Create an instance of our alarm clock
    clock = AlarmClock()
    # Calculate time for test alarm (1 minute from now), %60 ensures minutes wrap around correctly at hour boundaries
    next_alarm = f"{datetime.now().hour:02d}:{(datetime.now().minute + 1) % 60:02d}"
    # Set the test alarm with 'birds' sound
    clock.add_alarm(next_alarm, "birds")
    # Start the alarm clock
    clock.run()
# Only run the program if this file is run directly (not imported)
if __name__ == "__main__":
    main()