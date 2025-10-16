# Sleep Log Tracker - Record sleep start and end times, calculate duration.
import json
import os
from datetime import datetime, timedelta

class SleepTracker:
    def __init__(self, file="sleep_log.json"):
        self.file = file
        self.logs = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file):
            try:
                with open(self.file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_data(self):
        with open(self.file, 'w') as f:
            json.dump(self.logs, f, indent=2)
    
    def start_sleep(self, time=None):
        if time is None:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"start": time, "end": None, "duration": None, "quality": None}
        self.logs.append(entry)
        self.save_data()
        return f"💤 Sleep started at {time}"
    
    def end_sleep(self, time=None):
        if time is None:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for entry in reversed(self.logs):
            if entry["end"] is None:
                entry["end"] = time
                start = datetime.strptime(entry["start"], "%Y-%m-%d %H:%M:%S")
                end = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                if end < start:
                    end += timedelta(days=1)
                duration = (end - start).total_seconds() / 3600
                entry["duration"] = round(duration, 2)
                self.save_data()
                return f"⏰ Sleep ended at {time}. Duration: {entry['duration']} hours"
        return "❌ No active sleep session found"
    
    def rate_sleep(self, quality):
        if not (1 <= quality <= 10):
            return "❌ Quality must be 1-10"
        for entry in reversed(self.logs):
            if entry["end"] and entry["quality"] is None:
                entry["quality"] = quality
                self.save_data()
                return f"⭐ Sleep rated: {quality}/10"
        return "❌ No completed session to rate"
    
    def view_logs(self, count=5):
        if not self.logs:
            return "📝 No sleep logs found"
        recent = self.logs[-count:]
        output = f"📊 Recent Sleep Logs:\n{'='*30}\n"
        for entry in recent:
            start_time = entry["start"].split()[1]
            if entry["end"]:
                end_time = entry["end"].split()[1]
                output += f"💤 {start_time} - {end_time} ({entry['duration']}h)"
                if entry["quality"]:
                    output += f" ⭐{entry['quality']}/10"
                output += "\n"
            else:
                output += f"💤 {start_time} - Currently sleeping...\n"
        return output
    
    def statistics(self):
        completed = [log for log in self.logs if log["duration"]]
        if not completed:
            return "📊 No completed sessions"
        durations = [log["duration"] for log in completed]
        qualities = [log["quality"] for log in completed if log["quality"]]
        
        output = f"📈 Sleep Statistics:\n{'='*20}\n"
        output += f"📊 Sessions: {len(completed)}\n"
        output += f"⏱️  Avg duration: {sum(durations)/len(durations):.1f}h\n"
        output += f"🌙 Longest: {max(durations):.1f}h\n"
        output += f"☀️  Shortest: {min(durations):.1f}h\n"
        if qualities:
            output += f"⭐ Avg quality: {sum(qualities)/len(qualities):.1f}/10\n"
        return output

def main():
    tracker = SleepTracker()
    print("🌙 Sleep Log Tracker 🌙")
    
    while True:
        print("\n1. 💤 Start Sleep  2. ⏰ End Sleep  3. ⭐ Rate Sleep")
        print("4. 📊 View Logs    5. 📈 Statistics  6. 🚪 Exit")
        
        choice = input("Choose (1-6): ").strip()
        
        try:
            if choice == '1':
                print(tracker.start_sleep())
            elif choice == '2':
                print(tracker.end_sleep())
            elif choice == '3':
                quality = int(input("Rate sleep (1-10): "))
                print(tracker.rate_sleep(quality))
            elif choice == '4':
                count = input("How many entries? (default 5): ").strip()
                count = int(count) if count.isdigit() else 5
                print(tracker.view_logs(count))
            elif choice == '5':
                print(tracker.statistics())
            elif choice == '6':
                print("🌙 Sweet dreams!")
                break
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n🌙 Sweet dreams!")
            break

if __name__ == "__main__":
    main()
