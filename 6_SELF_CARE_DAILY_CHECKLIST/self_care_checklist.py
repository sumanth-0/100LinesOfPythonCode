from datetime import datetime, timedelta

# Define self-care tasks and reminders
SELF_CARE_TASKS = [
    {"task": "Drink Water", "completed": False},
    {"task": "Take a Break", "completed": False},
    {"task": "Practice Mindfulness", "completed": False},
    {"task": "Get Fresh Air", "completed": False}
]

def show_tasks():
    print("Daily Self-Care Checklist:")
    for idx, item in enumerate(SELF_CARE_TASKS, 1):
        status = "✓" if item["completed"] else "✗"
        print(f"{idx}. {item['task']} - {status}")

def mark_task_completed(task_number):
    if 1 <= task_number <= len(SELF_CARE_TASKS):
        SELF_CARE_TASKS[task_number - 1]["completed"] = True
        print(f"{SELF_CARE_TASKS[task_number - 1]['task']} marked as completed!")
    else:
        print("Invalid task number.")

def show_motivation():
    print("\nMotivational Message: Keep up the great work! Small steps each day build positive habits.")

def reset_tasks():
    for task in SELF_CARE_TASKS:
        task["completed"] = False

def main():
    reset_tasks()
    next_motivation_time = datetime.now() + timedelta(hours=1)

    while True:
        show_tasks()
        choice = input("\nSelect a task to complete (1-4) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            break
        elif choice.isdigit():
            mark_task_completed(int(choice))
            if datetime.now() >= next_motivation_time:
                show_motivation()
                next_motivation_time = datetime.now() + timedelta(hours=1)
        else:
            print("Invalid input, please select a valid task number.")

if __name__ == "__main__":
    main()
