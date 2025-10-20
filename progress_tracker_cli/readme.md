# Progress Tracker CLI

A simple, persistent command-line tool built with Python and Pandas to track daily tasks, habits, and progress. All data is saved locally in a `progress.csv` file.

## Features

* **New User Setup**: Initializes a new `progress.csv` file and allows you to define the custom tasks (columns) you want to track.
* **Track Daily Tasks**: Prompts you for each of your defined tasks and saves your progress for the current date as a new row in the CSV.
* **Add New Tasks**: Dynamically add new tasks (columns) to your tracker at any time without losing existing data.
* **View Report**: Displays the entire history of your tracked progress in a clean, table-like format directly in the terminal.

## File Structure

* `progress_tracker_cli.py`: The main entry point for the application. It displays the user menu, handles user input, and calls the appropriate functions from the `tasks` module.
* `tasks.py`: The core logic module. It contains all functions for file handling (reading/writing to `progress.csv`), setting up the tracker, adding new tasks, and viewing the report.
* `progress.csv`: (Generated after first run) The CSV file where all dates and task data are stored.

## Prerequisites

This project requires the **pandas** library.

## Installation

1.  Make sure you have Python 3 installed.
2.  Install the `pandas` library using pip:
    ```bash
    pip install pandas
    ```

## How to Use

1.  Place `progress_tracker_cli.py` and `tasks.py` in the same directory.
2.  Run the main application from your terminal:
    ```bash
    python progress_tracker_cli.py
    ```
3.  The main menu will appear:

    ```
    ------------------------------------------------
    |                                              |
    |         Welcome to Progress Tracker          |
    |                                              |
    ------------------------------------------------
    [ 1 ] -> New User Setup Tracker
    [ 2 ] -> Track Today's Task
    [ 3 ] -> Add new Task
    [ 4 ] -> View Report
    [ 0 ] -> Exit
    Enter your choice:
    ```

### Example Workflow

1.  **First-time users**: Choose `[ 1 ] New User Setup Tracker`.
    * You will be prompted to name your daily tasks (e.g., "Workout", "Read", "Code").
    * Type `s` to save and finish.

2.  **Daily Tracking**: Choose `[ 2 ] Track Today's Task`.
    * The script will ask for your progress on each task you defined (e.g., `Workout : Yes`, `Read : 30 mins`, `Code : 1 hour`).
    * Your answers will be saved with today's date.

3.  **Adding a Task**: Choose `[ 3 ] Add new Task`.
    * If you decide you also want to track "Meditate", you can add it here.
    * The "Meditate" column will be added to `progress.csv`, and previous entries will have a blank value for this task.

4.  **Viewing Progress**: Choose `[ 4 ] View Report`.
    * This will print a formatted table of all your entries, like this:

    ```
    date         Workout   Read      Code
    2025-10-20   Yes       30 mins   1 hour
    2025-10-21   No        15 mins   2 hours
    ```