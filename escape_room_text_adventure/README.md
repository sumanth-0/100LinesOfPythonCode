# Escape Room Text Adventure

## Description
A simple text-based adventure game where the player must solve puzzles to escape a virtual room. The player wakes up in a locked room and must explore the environment, find clues, solve puzzles, and ultimately find the key to escape.

## Features
- Interactive text-based gameplay
- Inventory system to collect and use items
- Multiple objects to examine (desk, painting, safe, vent, window, door)
- Safe code puzzle with limited attempts
- Typing effect for immersive storytelling
- Multiple commands for interaction

## How to Run
```bash
python escape_room_text_adventure.py
```

Or:
```bash
python3 escape_room_text_adventure.py
```

## How to Play
1. Run the program
2. Read the introduction and available commands
3. Type commands to interact with objects in the room
4. Explore the room by examining different objects
5. Collect items and solve puzzles
6. Find the safe code and unlock the safe
7. Take the key from the safe
8. Use the key to unlock the door and escape!

## Available Commands
- `LOOK` - Look around the room
- `DESK` - Examine the desk
- `PAINTING` - Examine the painting
- `SAFE` - Try to open the safe
- `VENT` - Examine the vent
- `WINDOW` - Examine the window
- `DOOR` - Try to open the door
- `TAKE KEY` - Take the key from the safe
- `INVENTORY` - Check your inventory
- `HELP` - Show available commands
- `QUIT` - Exit the game

## Expected Output
The game will display:
- An introduction to the scenario
- The current state of the room
- Your inventory
- Responses to your commands
- Clues and hints as you explore
- Success or failure messages

## Walkthrough (Spoiler Alert!)
1. Type `DESK` to search the desk and find a flashlight
2. Type `PAINTING` to examine the painting with the flashlight and find the safe code
3. Type `SAFE` and enter the code `7328` to open the safe
4. Type `TAKE KEY` to take the key from the safe
5. Type `DOOR` to unlock the door with the key and escape!

## Requirements
- Python 3.x
- No external dependencies required (uses only standard library)

## Author
Created for the 100 Lines of Python Code repository
Issue #1176: Escape Room Text Adventure

## License
This project is part of the 100LinesOfPythonCode repository and follows its licensing terms.
