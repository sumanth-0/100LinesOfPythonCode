import random

# Dungeon map configuration
WIDTH = 20   # Width of the dungeon
HEIGHT = 10  # Height of the dungeon

def generate_room():
    return random.choice([".", "#", " "])  # '.' represents room, '#' represents wall, ' ' represents empty space

def generate_dungeon(width, height):
    # Create a grid with random rooms and hallways
    dungeon = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(generate_room())
        dungeon.append(row)
    return dungeon

def display_dungeon(dungeon):
    # Display the dungeon in ASCII format
    for row in dungeon:
        print("".join(row))

def add_features(dungeon):
    # Add random doors ('D') and treasures ('T')
    num_doors = random.randint(1, 5)
    num_treasures = random.randint(1, 3)
    
    for _ in range(num_doors):
        x = random.randint(0, WIDTH-1)
        y = random.randint(0, HEIGHT-1)
        dungeon[y][x] = "D"  # Door

    for _ in range(num_treasures):
        x = random.randint(0, WIDTH-1)
        y = random.randint(0, HEIGHT-1)
        dungeon[y][x] = "T"  # Treasure

def main():
    dungeon = generate_dungeon(WIDTH, HEIGHT)  # Generate the dungeon layout
    add_features(dungeon)  # Add special features like doors and treasures
    print("Generated Random Dungeon Map:")
    display_dungeon(dungeon)  # Display the dungeon

if __name__ == "__main__":
    main()
