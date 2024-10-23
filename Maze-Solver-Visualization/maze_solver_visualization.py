import pygame
import random
import math
from queue import PriorityQueue

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Directions for maze generation
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left
        self.visited = False

    def draw(self, win):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.visited:
            pygame.draw.rect(win, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
        if self.walls[0]:
            pygame.draw.line(win, BLACK, (x, y), (x + CELL_SIZE, y))  # Top
        if self.walls[1]:
            pygame.draw.line(win, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))  # Right
        if self.walls[2]:
            pygame.draw.line(win, BLACK, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))  # Bottom
        if self.walls[3]:
            pygame.draw.line(win, BLACK, (x, y + CELL_SIZE), (x, y))  # Left

def random_choice(lst):
    return lst[random.randint(0, len(lst) - 1)]

def generate_maze(grid, start_cell):
    stack = [start_cell]
    start_cell.visited = True

    while stack:
        current_cell = stack[-1]
        neighbors = []
        
        for i, (dx, dy) in enumerate(DIRECTIONS):
            nx, ny = current_cell.x + dx, current_cell.y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                neighbor = grid[ny][nx]
                if not neighbor.visited:
                    neighbors.append((neighbor, i))

        if neighbors:
            neighbor, direction = random_choice(neighbors)
            current_cell.walls[direction] = False
            neighbor.walls[(direction + 2) % 4] = False
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def a_star(start, end, grid):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {cell: float('inf') for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float('inf') for row in grid for cell in row}
    f_score[start] = heuristic(start, end)

    while not open_set.empty():
        current = open_set.get()[1]

        if current == end:
            return reconstruct_path(came_from, current)

        for direction in range(4):
            if not current.walls[direction]:
                dx, dy = (0, 1) if direction == 0 else (1, 0) if direction == 1 else (0, -1), (-1, 0)
                neighbor = grid[current.y + dy][current.x + dx]
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set.queue]:
                        open_set.put((f_score[neighbor], neighbor))

    return []

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def draw_grid(win, grid, path=[]):
    for row in grid:
        for cell in row:
            cell.draw(win)
    
    for cell in path:
        pygame.draw.rect(win, GREEN, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver Visualization")

    grid = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
    generate_maze(grid, grid[0][0])
    start = grid[0][0]
    end = grid[ROWS - 1][COLS - 1]

    running = True
    while running:
        win.fill(WHITE)
        draw_grid(win, grid)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        path = a_star(start, end)
        draw_grid(win, grid, path)
        pygame.display.flip()
        pygame.time.delay(1000)  # Wait for a second to show the path

    pygame.quit()

if __name__ == "__main__":
    main()
