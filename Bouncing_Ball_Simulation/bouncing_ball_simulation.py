import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen configuration
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball bouncing simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball Configuration
ball_radius = 10
ball_x = ball_radius  # Start position on the left edge
ball_y = HEIGHT // 2  # Vertical center
ball_speed_x = 5  # Horizontal speed
ball_speed_y = 8  # Vertical speed

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen with white background
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_speed_x
    
    ball_y -= ball_speed_y
    
    # Bounce off the edges
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x  # Reverse direction

    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y
    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Update the display
    pygame.display.flip()
    
    # Delay to control frame rate
    pygame.time.delay(20)

# Quit Pygame
pygame.quit()
sys.exit()
