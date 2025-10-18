import random
from collections import deque

def generate_maze(size=10):
    """Generate a random maze with walls and paths."""
    maze = [['#' for _ in range(size)] for _ in range(size)]
    
    def carve_path(x, y):
        maze[y][x] = ' '
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                carve_path(nx, ny)
    
    carve_path(1, 1)
    maze[1][1] = 'S'
    maze[size - 2][size - 2] = 'E'
    return maze

def display_maze(maze, path=None):
    """Display the maze with optional path."""
    display = [row[:] for row in maze]
    
    if path:
        for x, y in path[1:-1]:
            if display[y][x] == ' ':
                display[y][x] = '.'
    
    for row in display:
        print(''.join(row))

def find_shortest_path(maze):
    """Find shortest path using BFS."""
    size = len(maze)
    start = (1, 1)
    end = (size - 2, size - 2)
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end:
            return path
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < size and 0 <= ny < size and 
                maze[ny][nx] != '#' and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None

def main():
    """Main game function."""
    print("=== Random Maze Escape ===")
    print("\nGenerating maze...\n")
    
    size = 15
    maze = generate_maze(size)
    
    print("\nOriginal Maze (S=Start, E=Exit):\n")
    display_maze(maze)
    
    print("\n\nFinding shortest path...\n")
    path = find_shortest_path(maze)
    
    if path:
        print(f"\nPath found! Length: {len(path)} steps\n")
        print("Maze with solution path (. = path):\n")
        display_maze(maze, path)
        print(f"\nTotal steps to escape: {len(path)}")
    else:
        print("\nNo path found!")

if __name__ == "__main__":
    main()
