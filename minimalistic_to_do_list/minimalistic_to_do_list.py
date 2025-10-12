import json
import os
import sys

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def remove_task(task_id):
    """Remove a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    # Reassign IDs to maintain continuity
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
    save_tasks(tasks)
    print(f"Task {task_id} removed.")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task["done"] else " "
        print(f"[{status}] {task['id']}. {task['description']}")
    print("-" * 50)

def mark_done(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

def display_help():
    """Display help information."""
    print("\nMinimalistic To-Do List - Commands:")
    print("  add <description>    - Add a new task")
    print("  remove <id>          - Remove a task by ID")
    print("  list                 - List all tasks")
    print("  done <id>            - Mark a task as done")
    print("  help                 - Display this help message")
    print("  exit                 - Exit the application\n")

def main():
    """Main function to run the CLI."""
    print("Welcome to Minimalistic To-Do List!")
    display_help()
    
    while True:
        try:
            command = input("\nEnter command: ").strip().split()
            if not command:
                continue
            
            action = command[0].lower()
            
            if action == "add":
                if len(command) < 2:
                    print("Usage: add <description>")
                else:
                    add_task(" ".join(command[1:]))
            elif action == "remove":
                if len(command) != 2 or not command[1].isdigit():
                    print("Usage: remove <id>")
                else:
                    remove_task(int(command[1]))
            elif action == "list":
                list_tasks()
            elif action == "done":
                if len(command) != 2 or not command[1].isdigit():
                    print("Usage: done <id>")
                else:
                    mark_done(int(command[1]))
            elif action == "help":
                display_help()
            elif action == "exit":
                print("Goodbye!")
                sys.exit(0)
            else:
                print(f"Unknown command: {action}. Type 'help' for available commands.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
