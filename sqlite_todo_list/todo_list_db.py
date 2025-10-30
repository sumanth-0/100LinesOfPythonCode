import sqlite3
import sys

# The name of the database file
DB_NAME = "todo.db"

def initialize_db(conn):
    """Creates the 'tasks' table if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        # Use 'IF NOT EXISTS' to safely run this every time
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        );
        """)
        conn.commit()
        print("Database initialized.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)

def add_task(conn):
    """Adds a new task to the database."""
    desc = input("Enter the task description: ")
    if not desc:
        print("Task description cannot be empty.")
        return
        
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (desc,))
    conn.commit()
    print(f"Added task: '{desc}'")

def remove_task(conn):
    """Removes a task from the database by its ID."""
    list_tasks(conn, quiet=True) # Show the list first
    try:
        task_id = int(input("Enter the task ID to remove: "))
        cursor = conn.cursor()
        # Use 'changes()' to see if a row was actually deleted
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print(f"No task found with ID {task_id}.")
        else:
            conn.commit()
            print(f"Removed task {task_id}.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def list_tasks(conn, quiet=False):
    """Lists all current tasks in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM tasks ORDER BY id")
    rows = cursor.fetchall()
    
    if not rows:
        if not quiet:
            print("\nYour to-do list is empty.")
    else:
        print("\n--- Your To-Do List ---")
        for row in rows:
            print(f"  [{row[0]}] {row[1]}") # e.g., [1] Buy milk

def main():
    """Main application loop."""
    # 'with' statement handles connection closing
    with sqlite3.connect(DB_NAME) as conn:
        initialize_db(conn)
        
        while True:
            print("\n--- Persistent To-Do List ---")
            print("1. List tasks")
            print("2. Add task")
            print("3. Remove task")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                list_tasks(conn)
            elif choice == '2':
                add_task(conn)
            elif choice == '3':
                remove_task(conn)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()