# Minimalistic To-Do List

A simple command-line interface (CLI) to-do list application written in Python. This tool allows you to manage your tasks efficiently with basic operations like adding, removing, listing, and marking tasks as done.

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list
- **Remove Tasks**: Delete tasks by their ID
- **List Tasks**: View all your tasks with their completion status
- **Mark as Done**: Mark tasks as completed
- **Persistent Storage**: Tasks are automatically saved to and loaded from a JSON file
- **Interactive CLI**: User-friendly command-line interface

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `minimalistic_to_do_list` directory
3. Run the script:

```bash
python minimalistic_to_do_list.py
```

## Usage

When you run the application, you'll be greeted with a welcome message and a list of available commands. The application runs in an interactive loop where you can enter commands.

### Available Commands

- `add <description>` - Add a new task with the given description
- `remove <id>` - Remove a task by its ID number
- `list` - Display all tasks with their IDs and completion status
- `done <id>` - Mark a task as completed
- `help` - Display the help message with available commands
- `exit` - Exit the application

### Examples

```bash
# Add a new task
Enter command: add Buy groceries
Task added: Buy groceries

# List all tasks
Enter command: list

Your To-Do List:
--------------------------------------------------
[ ] 1. Buy groceries
[ ] 2. Complete Python project
[ ] 3. Call the dentist
--------------------------------------------------

# Mark a task as done
Enter command: done 1
Task 1 marked as done.

# List tasks again to see the update
Enter command: list

Your To-Do List:
--------------------------------------------------
[✓] 1. Buy groceries
[ ] 2. Complete Python project
[ ] 3. Call the dentist
--------------------------------------------------

# Remove a task
Enter command: remove 2
Task 2 removed.

# Exit the application
Enter command: exit
Goodbye!
```

## Data Storage

Tasks are stored in a file named `todo_list.json` in the same directory as the script. This file is automatically created when you add your first task and is updated with each operation.

The JSON structure stores each task with:
- `id`: Unique identifier for the task
- `description`: The task description
- `done`: Boolean indicating whether the task is completed

## Code Structure

The application is organized into the following functions:

- `load_tasks()`: Loads tasks from the JSON file
- `save_tasks(tasks)`: Saves tasks to the JSON file
- `add_task(description)`: Adds a new task
- `remove_task(task_id)`: Removes a task by ID
- `list_tasks()`: Displays all tasks
- `mark_done(task_id)`: Marks a task as completed
- `display_help()`: Shows available commands
- `main()`: Main application loop

## Contributing

This is part of the 100LinesOfPythonCode project. The entire application is implemented in exactly 100 lines of Python code.

## License

This project is open source and available under the MIT License.
