#!/usr/bin/env python3
"""Quick Task Tracker - A simple CLI for fast task tracking."""
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False,
        'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Task added: {description}")

def complete_task(task_id):
    """Mark a task as complete."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print(f"✓ Task completed: {task['description']}")
            return
    print(f"✗ Task #{task_id} not found")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Add one with: python task_tracker.py add <description>")
        return
    
    print("\n=== Quick Task Tracker ===")
    pending = [t for t in tasks if not t['completed']]
    completed = [t for t in tasks if t['completed']]
    
    if pending:
        print("\nPending Tasks:")
        for task in pending:
            print(f"  [{task['id']}] {task['description']} (added: {task['created']})")
    
    if completed:
        print("\nCompleted Tasks:")
        for task in completed:
            print(f"  [✓] {task['description']} (completed: {task.get('completed_at', 'N/A')})")
    
    print(f"\nTotal: {len(tasks)} | Pending: {len(pending)} | Completed: {len(completed)}\n")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    for i, task in enumerate(tasks, 1):
        task['id'] = i
    save_tasks(tasks)
    print(f"✓ Task #{task_id} deleted")

def main():
    """Main function to handle CLI commands."""
    import sys
    if len(sys.argv) < 2:
        view_tasks()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py add <description>")
            return
        description = ' '.join(sys.argv[2:])
        add_task(description)
    elif command == 'complete':
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py complete <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
    elif command == 'view':
        view_tasks()
    else:
        print("Unknown command. Available: add, complete, delete, view")

if __name__ == '__main__':
    main()
