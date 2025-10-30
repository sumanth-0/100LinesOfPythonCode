# Persistent To-Do List (with SQLite)

This is a simple but powerful command-line to-do list application that **saves your tasks permanently** using Python's built-in `sqlite3` database.

## Description

Unlike simple in-memory scripts, this to-do list creates a small database file (`todo.db`) in the same directory. Any tasks you add are saved to this database. You can close the script, turn off your computer, and when you run it again, your tasks will still be there.

## Features

* **Persistent Storage:** Uses `sqlite3` to save tasks.
* **Add Tasks:** Add new items to your list.
* **Remove Tasks:** Remove items by their unique ID.
* **List Tasks:** View all your current tasks, numbered by ID.
* **Database Creation:** Automatically creates the `todo.db` file and `tasks` table on first run.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Run the script from your terminal:
    ```sh
    python todo_list_db.py
    ```
3.  A `todo.db` file will be created in the directory to store your tasks.
4.  Follow the on-screen menu (1-4) to manage your list.

## Modules Used

* **`sqlite3`**: (Python's built-in module for an on-disk SQL database)
* **`sys`**: (Built-in module for exiting the script on a critical error)