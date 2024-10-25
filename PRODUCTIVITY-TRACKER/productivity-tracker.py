import time

def track_time():
    activities = {}
    while True:
        activity = input("Enter the task name (or type 'exit' to finish): ")
        if activity.lower() == 'exit':
            break
        
        start_time = time.time()
        input(f"Started tracking '{activity}'. Press Enter to stop.")
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        activities[activity] = activities.get(activity, 0) + elapsed_time

    return activities

def display_summary(activities):
    print("\nProductivity Summary:")
    for activity, total_time in activities.items():
        print(f"{activity}: {total_time / 60:.2f} minutes")

def main():
    print("Welcome to the Productivity Tracker!")
    activities = track_time()
    display_summary(activities)

if __name__ == "__main__":
    main()
