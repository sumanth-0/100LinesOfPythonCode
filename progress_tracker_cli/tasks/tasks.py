import pandas as pd
import csv, os
from datetime import date
from progress_tracker_cli import main

# create file if not exists
filename = "progress.csv"

def new_user_setup_tracker():
    headers = ['date']
    if os.path.exists(filename):
        progress_file = pd.read_csv(filename)
        if progress_file.empty:
            print("But no Daily Tasks \n Add new Task")
    else:
        with open(filename, 'w', newline="") as progresscsv:
            while (True):
                task_input = input("Name your daily tasks ('s' to save): ")
                if task_input == 's' or task_input == 'q':
                    print("Data save...")
                    break
                headers.append(task_input)

            df = pd.DataFrame(columns=headers)
            df.to_csv(filename, index=False)

    dfread = pd.read_csv(filename)
    new_header = dfread.columns
    print("---- Your Daily Tasks ----")
    for i in new_header:
        print(i, end=" ")
    print(" ")
    main()


def track_today_task():
    # insert daily progress in it
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        print('-------------')

    t_day = date.today()
    today_task = [t_day]
    print(f"Add task for : {t_day}")
    for col in header[1:]:
        data = input(f"{col} : ")
        today_task.append(data)

    # Convert to DataFrame and append to CSV
    new_df = pd.DataFrame([today_task], columns=header)
    new_df.to_csv(filename, mode='a', header=False, index=False)
    print("Task added successfully!")
    main()


def add_new_task():
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    print("Enter new tasks (type 'q' to finish):")
    new_columns = []

    while True:
        col = input("Column name: ").strip()
        if col.lower() == 'q':
            break
        if col and col not in df.columns:
            new_columns.append(col)
        elif col in df.columns:
            print(f"Column '{col}' already exists, skipping.")
    
    if not new_columns:
        print("No new columns entered.")
        return


    for col in new_columns:
        df[col] = pd.NA
    # Save back without removing data
    df.to_csv(filename, index=False)
    print(f"Added new columns {new_columns} to '{filename}' successfully (no new rows added).")

    main()

def view_report():
    try:
        df = pd.read_csv(filename)
        df_len = len(df.columns)
        if df.empty:
            print("No Record Available")
        else:
            print(df.to_string(index=False))
    except:
        print("No Task Present")

    main()