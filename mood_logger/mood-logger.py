from datetime import datetime

print("=== Mood Logger ===")
choice = input("Do you want to (1) Log mood or (2) View all moods? ")

if choice == "1":
    mood = input("How are you feeling today? ")
    with open("mood_log.txt", "a") as f:
        f.write(f"{datetime.now().date()} - {mood}\n")
    print("📝 Mood saved!")
elif choice == "2":
    try:
        with open("mood_log.txt") as f:
            print("\nYour moods so far:\n" + f.read())
    except FileNotFoundError:
        print("No moods logged yet.")
else:
    print("Invalid option.")
