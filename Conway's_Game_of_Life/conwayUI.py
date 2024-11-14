import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 20, 20      # Number of cells in the grid
CELL_SIZE = 20              # Size of each cell in pixels
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid with random live (1) or dead (0) cells
def create_grid():
    return [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Draw the grid on the screen
def draw_grid(grid):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, rect)

# Get the number of live neighbors for a given cell
def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            count += grid[nx][ny]
    return count

# Apply the rules of the Game of Life to update the grid
def update_grid(grid):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x in range(HEIGHT):
        for y in range(WIDTH):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[x][y] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                new_grid[x][y] = 1  # Cell survives
            elif grid[x][y] == 0 and live_neighbors == 3:
                new_grid[x][y] = 1  # Cell is born
            else:
                new_grid[x][y] = 0  # Cell dies
    return new_grid

# Main game loop
def main():
    grid = create_grid()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update grid and draw to screen
        grid = update_grid(grid)
        draw_grid(grid)
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
