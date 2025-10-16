def show_menu():
    """Display the available options."""
    print("\n=== TO-DO LIST MENU ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def view_tasks(tasks):
    """Show all current tasks with their completion status."""
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done!" if task["done"] else "✘ Pending"
            print(f"{i}. {task['task']}  [{status}]")


def add_task(tasks):
    """Add a new task to the list."""
    name = input("Enter new task: ").strip()
    if name:
        tasks.append({"task": name, "done": False})
        print(f"Task '{name}' added.")
    else:
        print("Task cannot be empty!")


def mark_completed(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("No tasks to mark.")
        return
    num = input("Enter task number to mark as done: ").strip()
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        tasks[int(num) - 1]["done"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    """Delete a task from the list."""
    if not tasks:
        print("No tasks to delete.")
        return
    num = input("Enter task number to delete: ").strip()
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        removed = tasks.pop(int(num) - 1)
        print(f"Task '{removed['task']}' deleted.")
    else:
        print("Invalid task number.")


def main():
    """Main loop for the To-Do List."""
    tasks = []
    while True:
        show_menu()
        choice = input("Enter choice (1–5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
