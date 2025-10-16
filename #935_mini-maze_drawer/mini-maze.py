import random

def generate_maze(width, height):
    grid_height = 2 * height + 1
    grid_width = 2 * width + 1
    maze = [[1] * grid_width for _ in range(grid_height)]
    
    visited = [[False] * width for _ in range(height)]

    start_x, start_y = random.randrange(width), random.randrange(height)
    stack = [(start_x, start_y)]
    visited[start_y][start_x] = True
    
    maze[2 * start_y + 1][2 * start_x + 1] = 0 

    directions = [
        (0, -1, 0, -1),
        (0, 1, 0, 1),
        (-1, 0, -1, 0),
        (1, 0, 1, 0)
    ]

    while stack:
        cx, cy = stack[-1]
        
        neighbors = []
        for dx, dy, wx_off, wy_off in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                neighbors.append((nx, ny, wx_off, wy_off))
        
        if neighbors:
            nx, ny, wx_off, wy_off = random.choice(neighbors)
            
            maze[2 * ny + 1][2 * nx + 1] = 0 
            
            wall_y = 2 * cy + 1 + wy_off 
            wall_x = 2 * cx + 1 + wx_off
            maze[wall_y][wall_x] = 0 

            visited[ny][nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()
            
    maze[1][1] = 'S'
    maze[grid_height - 2][grid_width - 2] = 'E' 

    return maze

def print_maze(maze):
    WALL = '#'
    PATH = ' '
    
    output = []
    for row in maze:
        line = ""
        for cell in row:
            if cell == 1:
                line += WALL
            elif cell == 0:
                line += PATH
            else:
                line += str(cell) 
        output.append(line)
        
    print('\n'.join(output))

MAZE_WIDTH = 25
MAZE_HEIGHT = 15

random_maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)

print_maze(random_maze)