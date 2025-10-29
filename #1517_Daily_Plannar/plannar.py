import json, os
from datetime import datetime

DATA_FILE = "tasks.json"
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task():
    text = input("Enter a new task: ").strip()
    if not text:
        print("Task cannot be empty!")
        return
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "text": text,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {text}")

def list_tasks(show_done=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for t in tasks:
        if show_done is None or t["done"] == show_done:
            status = "✓" if t["done"] else "✗"
            print(f"{t['id']:>2}. [{status}] {t['text']} ({t['created']})")

def mark_done():
    list_tasks(show_done=False)
    try:
        tid = int(input("Enter a task ID to mark done: "))
        tasks = load_tasks()
        for t in tasks:
            if t["id"] == tid:
                t["done"] = True
                save_tasks(tasks)
                print(f"Marked task #{tid} as done.")
                return
        print("Invalid task ID.")
    except ValueError:
        print("Enter a valid number!")

def delete_task():
    list_tasks()
    try:
        tid = int(input("Enter a task ID to delete: "))
        tasks = load_tasks()
        tasks = [t for t in tasks if t["id"] != tid]
        save_tasks(tasks)
        print(f"Deleted task #{tid}.")
    except ValueError:
        print("Enter a valid number!")

def main():
    while True:
        print("\n--- DAILY TASK MANAGER ---")
        print("1. Add Task")
        print("2. List Pending Tasks")
        print("3. List Completed Tasks")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1": add_task()
        elif choice == "2": list_tasks(show_done=False)
        elif choice == "3": list_tasks(show_done=True)
        elif choice == "4": mark_done()
        elif choice == "5": delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
