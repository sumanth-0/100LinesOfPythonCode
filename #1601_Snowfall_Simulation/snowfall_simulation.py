import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowfall Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(2, 8)
        self.speed = random.uniform(1, 3)
        self.drift = random.uniform(-0.5, 0.5)
    
    def fall(self):
        self.y += self.speed
        self.x += self.drift
        
        # Reset snowflake when it goes off screen
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)
        
        # Wrap around horizontally
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
    
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size)

# Create snowflakes
num_snowflakes = 150
snowflakes = [Snowflake() for _ in range(num_snowflakes)]

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background
    screen.fill(BLACK)
    
    # Update and draw snowflakes
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()
