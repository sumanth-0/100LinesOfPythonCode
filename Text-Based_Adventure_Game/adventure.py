def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go 'left' or 'right'.")
    first_choice()

def first_choice():
    choice = input("Which way do you want to go? (left/right): ").lower()
    if choice == "left":
        encounter_wolf()
    elif choice == "right":
        encounter_village()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def encounter_wolf():
    print("You encounter a hungry wolf!")
    choice = input("Do you want to 'run' or 'fight'? ").lower()
    if choice == "run":
        print("You ran away safely!")
        end_game()
    elif choice == "fight":
        print("You fought bravely but the wolf was too strong. Game Over.")
    else:
        print("Invalid choice. Try again.")
        encounter_wolf()

def encounter_village():
    print("You arrive at a peaceful village.")
    choice = input("Do you want to 'rest' or 'explore'? ").lower()
    if choice == "rest":
        print("You rested and regained your strength. You can continue your adventure!")
        end_game()
    elif choice == "explore":
        encounter_bear()
    else:
        print("Invalid choice. Try again.")
        encounter_village()

def encounter_bear():
    print("You stumble upon a bear!")
    choice = input("Do you want to 'climb a tree' or 'back away'? ").lower()
    if choice == "climb a tree":
        print("You climbed the tree safely! The bear left.")
        end_game()
    elif choice == "back away":
        print("You backed away slowly and the bear didn't notice you. Safe!")
        end_game()
    else:
        print("Invalid choice. Try again.")
        encounter_bear()

def end_game():
    print("Thank you for playing! Would you like to play again? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        start_game()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    start_game()
