import json, os

# Save the JSON file in the current working directory
DATA_FILE = os.path.join(os.getcwd(), "tree_data.json")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"total": 0, "goal": 50}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def show_progress(total, goal):
    percent = min(100, int((total / goal) * 100))
    filled = percent // 5
    bar = "█" * filled + "-" * (20 - filled)
    print(f"\nProgress: [{bar}] {percent}% ({total}/{goal} trees)")
    forest = "🌲" * min(total, 50)
    print(forest or "No trees yet! Start planting 🌱")

def plant_trees(data):
    try:
        n = int(input("How many trees do you want to plant? 🌳 -> "))
        if n <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Invalid input.")
        return
    data["total"] += n
    save_data(data)
    print(f"\n✅ You planted {n} tree(s)! Total: {data['total']}")
    if data["total"] >= data["goal"]:
        print("🎉 Congratulations! You've reached your goal!\n")
    show_progress(data["total"], data["goal"])

def set_goal(data):
    try:
        g = int(input("Enter your new tree goal 🌿 -> "))
        if g <= 0:
            print("Goal must be positive!")
            return
    except ValueError:
        print("Invalid input.")
        return
    data["goal"] = g
    save_data(data)
    print(f"🎯 New goal set to {g} trees!\n")

def reset_data():
    confirm = input("Type 'RESET' to clear all data: ")
    if confirm.strip().upper() == "RESET":
        save_data({"total": 0, "goal": 50})
        print("⚠️ Data reset successfully!\n")
    else:
        print("Reset cancelled.\n")

def main():
    print("\n🌲 Welcome to Virtual Tree Planter 🌲")
    data = load_data()
    while True:
        print("\nMenu:")
        print("1️⃣  Plant Trees")
        print("2️⃣  Show Progress")
        print("3️⃣  Set Goal")
        print("4️⃣  Reset Data")
        print("5️⃣  Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            plant_trees(data)
        elif choice == "2":
            show_progress(data["total"], data["goal"])
        elif choice == "3":
            set_goal(data)
        elif choice == "4":
            reset_data()
            data = load_data()
        elif choice == "5":
            print("\nGoodbye! Keep planting 🌳")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
