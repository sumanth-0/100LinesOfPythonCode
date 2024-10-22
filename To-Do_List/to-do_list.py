# Simple To-Do List in Python

class Task:
    def __init__(self, description):  # Initialize task with description
        self.description = description
        self.completed = False  # Track if the task is complete

    def __str__(self):  # String representation of the task
        status = "✓" if self.completed else "✗"  # Mark complete or incomplete
        return f"{self.description} [{status}]"

class ToDoList:
    def __init__(self):  # Initialize an empty to-do list
        self.tasks = []

    def add_task(self, description):  # Add a new task to the list
        self.tasks.append(Task(description))
        print(f"Added: {description}")

    def view_tasks(self):  # Display all tasks
        if not self.tasks:
            print("No tasks available!")  # If the list is empty
        else:
            for i, task in enumerate(self.tasks, 1):  # Enumerate tasks for numbering
                print(f"{i}. {task}")

    def complete_task(self, task_num):  # Mark a task as complete
        try:
            self.tasks[task_num - 1].completed = True  # Mark task complete by index
            print(f"Task {task_num} marked complete.")
        except IndexError:  # Handle invalid task number
            print("Invalid task number!")

    def delete_task(self, task_num):  # Delete a task from the list
        try:
            removed_task = self.tasks.pop(task_num - 1)  # Remove task by index
            print(f"Deleted: {removed_task.description}")
        except IndexError:  #Handle tasks which are invalid
            print("Invalid task number!")

def display_menu():  # Display menu options
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task Complete\n4. Delete Task\n5. Exit")

def main():  # Main function to run the app
    todo = ToDoList()  # Create a ToDoList object
    while True:
        display_menu()  # Show menu
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            todo.add_task(input("Enter task description: "))  # Add task
        elif choice == "2":
            todo.view_tasks()  # View tasks
        elif choice == "3":
            todo.complete_task(int(input("Task number to complete: ")))  # Complete task
        elif choice == "4":
            todo.delete_task(int(input("Task number to delete: ")))  # Delete task
        elif choice == "5":
            print("Goodbye!")  # Exit program
            break
        else:
            print("Invalid choice, try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the program
