import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT, BLOCK_SIZE = 400, 400, 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK, WHITE, GREEN, RED = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)

# Snake settings
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (0, -BLOCK_SIZE)
score = 0

# Food settings
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))  # Draw food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))  # Draw snake

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake):
        running = False  # Game over if snake hits wall or itself

    snake.insert(0, new_head)
    if new_head == food:  # If snake eats food
        score += 1
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
    else:
        snake.pop()  # Remove tail if food not eaten

    pygame.display.flip()
    clock.tick(10)  # Set game speed

pygame.quit()
print(f"Game Over! Score: {score}")
