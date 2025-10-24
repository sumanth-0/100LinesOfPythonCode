import tasks.tasks as tasks

def main():
    print("------------------------------------------------")
    print("|                                              |")
    print("|         Welcome to Progress Tracker          |")
    print("|                                              |")
    print("------------------------------------------------")

    print("[ 1 ] -> New User Setup Tracker")
    print("[ 2 ] -> Track Today's Task")
    print("[ 3 ] -> Add new Task")
    print("[ 4 ] -> View Report")
    print("[ 0 ] -> Exit")
    
    while True:
            try:
                option = int(input("Enter your choice: "))

                if option > 5 or option < 0:
                    raise ValueError("Out of bound")

                break
            except ValueError:
                print("Invalid input : Try again")

    match option:
            case 1:
                tasks.new_user_setup_tracker()
            case 2:
                tasks.track_today_task()
            case 3:
                tasks.add_new_task()
            case 4:
                tasks.view_report()
            case 0:
                print("See you later !!!")


if __name__ == "__main__":
    main()