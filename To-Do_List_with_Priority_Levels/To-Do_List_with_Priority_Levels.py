class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"[{self.priority}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        if priority not in ['High', 'Medium', 'Low']:
            print("Invalid priority! Use 'High', 'Medium', or 'Low'.")
            return
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f"Removed task: {task}")
                return
        print("Task not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do list.")
            return
        print("To-Do List:")
        for task in sorted(self.tasks, key=lambda x: x.priority):
            print(task)


if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1- Add Task")
        print("2- Remove Task")
        print("3- Show Tasks")
        print("4- Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (High, Medium, Low): ")
            todo_list.add_task(description, priority)
        elif choice == '2':
            description = input("Enter task description to remove: ")
            todo_list.remove_task(description)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Please try again to select right choice.")
