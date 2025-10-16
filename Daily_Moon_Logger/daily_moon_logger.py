"""
Daily Mood Logger
A simple Python script to log your daily mood and save it to a CSV file.
Supports adding mood entries, viewing mood history, and basic statistics.
"""

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter


class MoodLogger:
    """Manages daily mood logging with CSV storage."""

    def __init__(self, filename="mood_log.csv"):
        self.filename = filename
        self.moods = [
            "happy", "sad", "neutral", "lost",
            "excited", "anxious", "calm", "angry",
            "bored", "confident", "curious", "frustrated",
            "hopeful", "lonely", "peaceful", "overwhelmed",
            "relaxed", "surprised", "tired", "grateful",
            "guilty", "nostalgic", "jealous", "motivated",
            "nervous", "proud", "sadistic", "stressed",
            "optimistic", "pensive", "playful", "resentful"
        ]
        self._initialize_csv()

    def _initialize_csv(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Time", "Mood", "Note"])

    def log_mood(self, mood, note=""):
        mood = mood.lower()
        if mood not in self.moods:
            print(f"Invalid mood! Please choose from: {', '.join(self.moods)}")
            return False

        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, current_time, mood, note])

        print(f"Mood logged: {mood} on {current_date} at {current_time}")
        return True

    def view_history(self, days=7):
        if not os.path.exists(self.filename):
            print("No mood history found.")
            return

        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            entries = list(reader)

        if not entries:
            print("No mood entries yet.")
            return


        print(f"\n{'='*60}")
        print(f"Mood History (Last {len(entries[-days:])} entries)")
        print(f"{'='*60}")

        for entry in entries[-days:]:
            date, time, mood, note = entry
            note_text = f" - {note}" if note else ""
            print(f"{date} {time}: {mood.upper()}{note_text}")

        last_entries = entries[-days:]
        moods_last_days = [entry[2] for entry in last_entries]
        mood_counts = Counter(moods_last_days)
        mood_counts = {mood: count for mood, count in mood_counts.items() if count > 0}

        plt.figure(figsize=(10, 5))
        plt.bar(mood_counts.keys(), mood_counts.values(), color='skyblue')
        plt.title(f"Mood Distribution (Last {len(last_entries)} entries)")
        plt.xlabel("Mood")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def get_statistics(self):
        if not os.path.exists(self.filename):
            print("No mood data available.")
            return

        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            entries = list(reader)

        if not entries:
            print("No mood entries yet.")
            return

        mood_counts = {mood: 0 for mood in self.moods}
        for entry in entries:
            mood = entry[2]
            if mood in mood_counts:
                mood_counts[mood] += 1

        total = len(entries)
        print(f"\n{'='*40}")
        print("Mood Statistics")
        print(f"{'='*40}")
        print(f"Total entries: {total}")
        for mood, count in mood_counts.items():
            percentage = (count / total) * 100 if total else 0
            print(f"{mood.capitalize()}: {count} ({percentage:.1f}%)")


def main():
    logger = MoodLogger()
    print("\n" + "="*40)
    print("  Daily Mood Logger")
    print("="*40)

    while True:
        print("\nOptions:")
        print("1. Log today's mood")
        print("2. View mood history")
        print("3. View statistics")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            print(f"\nAvailable moods: {', '.join(logger.moods)}")
            mood = input("Enter your mood: ").strip()
            note = input("Add a note (optional): ").strip()
            logger.log_mood(mood, note)

        elif choice == "2":
            try:
                days = input("How many entries to show? (default 7): ").strip()
                days = int(days) if days else 7
                logger.view_history(days)
            except ValueError:
                logger.view_history()

        elif choice == "3":
            logger.get_statistics()

        elif choice == "4":
            print("\nGoodbye! Keep tracking your mood!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
