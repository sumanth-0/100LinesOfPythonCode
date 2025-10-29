import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT, BLOCK_SIZE = 400, 400, 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK, WHITE, GREEN, RED = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)

# Font
font = pygame.font.SysFont(None, 30)

def draw_text(text, color, x, y, center=False):
    """Utility function to draw text on the screen"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def random_food(snake):
    """Generate food position that doesn't overlap with snake"""
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

def game_loop():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (0, -BLOCK_SIZE)
    score = 0
    food = random_food(snake)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))  # Draw food

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

        # Draw score
        draw_text(f"Score: {score}", WHITE, 10, 10)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        # Collision detection
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake):
            running = False

        snake.insert(0, new_head)

        # Check food collision
        if new_head == food:
            score += 1
            food = random_food(snake)
        else:
            snake.pop()  # Remove tail if food not eaten

        pygame.display.flip()
        clock.tick(10 + score)  # Speed increases slightly as you score more

    # Game over screen
    game_over_screen(score)

def game_over_screen(score):
    """Display Game Over screen with restart and quit options"""
    while True:
        screen.fill(BLACK)
        draw_text("GAME OVER", RED, WIDTH // 2, HEIGHT // 2 - 40, center=True)
        draw_text(f"Final Score: {score}", WHITE, WIDTH // 2, HEIGHT // 2, center=True)
        draw_text("Press R to Restart or Q to Quit", WHITE, WIDTH // 2, HEIGHT // 2 + 40, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()  # Restart
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Start the game
game_loop()
