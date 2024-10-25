import random

# Define the rooms in the maze
maze_map = {
    'Entrance': {'North': 'Dark Hallway', 'East': None, 'South': None, 'West': None},
    'Dark Hallway': {'North': 'Treasure Room', 'East': 'Puzzle Room', 'South': 'Entrance', 'West': None},
    'Treasure Room': {'North': None, 'East': None, 'South': 'Dark Hallway', 'West': None},
    'Puzzle Room': {'North': None, 'East': None, 'South': None, 'West': 'Dark Hallway'}
}

items = ['Shiny Gem', 'Old Key', 'Mystic Sword']
found_items = []

current_room = 'Entrance'
game_over = False


def print_intro():
    print("Welcome to the **Text Adventure Maze**!\n")
    print("You find yourself at the entrance of a mysterious maze. Explore the rooms, solve puzzles, and find treasures.")
    print("Type commands like 'go North', 'take [item]', or 'solve puzzle'.")
    print("Let's begin!\n")


def describe_room(room):
    print(f"\nYou are in the {room}.")
    if room == 'Treasure Room' and 'Shiny Gem' not in found_items:
        print("You see something shiny in the corner!")
    if room == 'Puzzle Room' and 'Old Key' not in found_items:
        print("A mysterious puzzle blocks your way.")


def move(direction):
    global current_room
    if maze_map[current_room].get(direction):
        current_room = maze_map[current_room][direction]
        describe_room(current_room)
    else:
        print(f"You can't go {direction} from here!")


def take_item():
    global found_items
    if current_room == 'Treasure Room' and 'Shiny Gem' not in found_items:
        print("You picked up the Shiny Gem!")
        found_items.append('Shiny Gem')
    elif current_room == 'Puzzle Room' and 'Old Key' not in found_items:
        print("You solved the puzzle and found the Old Key!")
        found_items.append('Old Key')
    else:
        print("There's nothing to take here.")


def solve_puzzle():
    global game_over
    if current_room == 'Puzzle Room' and 'Old Key' not in found_items:
        answer = input("Solve the puzzle: What is 7 + 5? ")
        if answer == '12':
            print("Puzzle solved! The path is clear.")
            take_item()
        else:
            print("Wrong answer! Try again.")
    elif current_room == 'Treasure Room' and 'Shiny Gem' in found_items:
        print("You have found all treasures and solved the maze. Congratulations!")
        game_over = True
    else:
        print("There's no puzzle here to solve.")


def handle_input(user_input):
    if user_input.startswith('go'):
        direction = user_input.split()[1].capitalize()
        move(direction)
    elif user_input.startswith('take'):
        take_item()
    elif user_input.startswith('solve'):
        solve_puzzle()
    else:
        print("Invalid command! Try 'go [direction]', 'take [item]', or 'solve puzzle'.")


def play_game():
    print_intro()
    describe_room(current_room)
    
    while not game_over:
        user_input = input("\nWhat would you like to do? ").lower()
        handle_input(user_input)


if __name__ == "__main__":
    play_game()
