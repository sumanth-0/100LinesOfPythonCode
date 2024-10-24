import pygame
import random
from queue import PriorityQueue

WIDTH, HEIGHT, ROWS, COLS, CELL_SIZE = 600, 600, 30, 30, 600 // 30
WHITE, BLACK, GRAY, GREEN = (255, 255, 255), (0, 0, 0), (200, 200, 200), (0, 255, 0)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Cell:
    def __init__(self, x, y):
        self.x, self.y, self.walls, self.visited = x, y, [True] * 4, False

    def draw(self, win):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.visited: pygame.draw.rect(win, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
        if self.walls[0]: pygame.draw.line(win, BLACK, (x, y), (x + CELL_SIZE, y))
        if self.walls[1]: pygame.draw.line(win, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
        if self.walls[2]: pygame.draw.line(win, BLACK, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))
        if self.walls[3]: pygame.draw.line(win, BLACK, (x, y + CELL_SIZE), (x, y))

def generate_maze(grid, start):
    stack, start.visited = [start], True
    while stack:
        current = stack[-1]
        neighbors = [(grid[current.y + dy][current.x + dx], i) for i, (dx, dy) in enumerate(DIRECTIONS) 
                     if 0 <= current.x + dx < COLS and 0 <= current.y + dy < ROWS 
                     and not grid[current.y + dy][current.x + dx].visited]
        if neighbors:
            neighbor, direction = random.choice(neighbors)
            current.walls[direction], neighbor.walls[(direction + 2) % 4] = False, False
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()

def heuristic(a, b): return abs(a.x - b.x) + abs(a.y - b.y)

def a_star(start, end, grid):
    open_set = PriorityQueue(); open_set.put((0, start))
    g_score, f_score = {cell: float('inf') for row in grid for cell in row}, {cell: float('inf') for row in grid for cell in row}
    g_score[start], f_score[start] = 0, heuristic(start, end)
    came_from = {}

    while not open_set.empty():
        current = open_set.get()[1]
        if current == end: return reconstruct_path(came_from, current)

        for direction in range(4):
            if not current.walls[direction]:
                dx, dy = (1, 0) if direction == 1 else (0, 1) if direction == 0 else (-1, 0), (0, 1) if direction == 0 else (0, -1)
                neighbor = grid[current.y + dy][current.x + dx]
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current; g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set.queue]: open_set.put((f_score[neighbor], neighbor))
    return []

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from: current = came_from[current]; total_path.append(current)
    return total_path[::-1]

def draw_grid(win, grid, path=[]):
    for row in grid: for cell in row: cell.draw(win)
    for cell in path: pygame.draw.rect(win, GREEN, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init(); win = pygame.display.set_mode((WIDTH, HEIGHT)); pygame.display.set_caption("Maze Solver Visualization")
    grid = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
    generate_maze(grid, grid[0][0])
    path = a_star(grid[0][0], grid[ROWS - 1][COLS - 1])

    running = True
    while running:
        win.fill(WHITE); draw_grid(win, grid, path); pygame.display.flip()
        for event in pygame.event.get(): running = event.type != pygame.QUIT
    pygame.quit()

if __name__ == "__main__": main()
