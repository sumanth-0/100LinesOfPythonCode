"""
Simple Orbiting Solar System Simulation
Simulates planets orbiting around the sun with colored circles
"""

import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)      # Sun
GRAY = (169, 169, 169)      # Mercury
ORANGE = (255, 165, 0)      # Venus
BLUE = (0, 100, 255)        # Earth
RED = (255, 0, 0)           # Mars
BROWN = (205, 133, 63)      # Jupiter
GOLD = (255, 215, 0)        # Saturn
CYAN = (0, 255, 255)        # Uranus
DARK_BLUE = (0, 0, 139)     # Neptune

# Planet class
class Planet:
    def __init__(self, name, color, distance, radius, speed):
        self.name = name
        self.color = color
        self.distance = distance  # Distance from sun
        self.radius = radius      # Planet size
        self.speed = speed        # Orbital speed
        self.angle = 0            # Current angle in orbit
        
    def update(self):
        """Update planet position"""
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360
    
    def draw(self, screen, sun_x, sun_y):
        """Draw planet at current position"""
        # Calculate position based on angle
        x = sun_x + int(self.distance * math.cos(math.radians(self.angle)))
        y = sun_y + int(self.distance * math.sin(math.radians(self.angle)))
        
        # Draw orbit path
        pygame.draw.circle(screen, (50, 50, 50), (sun_x, sun_y), self.distance, 1)
        
        # Draw planet
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
        
        return x, y

# Create sun and planets
sun_x, sun_y = WIDTH // 2, HEIGHT // 2
sun_radius = 30

planets = [
    Planet("Mercury", GRAY, 60, 4, 4.15),
    Planet("Venus", ORANGE, 90, 7, 1.62),
    Planet("Earth", BLUE, 120, 8, 1.0),
    Planet("Mars", RED, 150, 6, 0.53),
    Planet("Jupiter", BROWN, 200, 15, 0.08),
    Planet("Saturn", GOLD, 250, 13, 0.03),
    Planet("Uranus", CYAN, 300, 10, 0.01),
    Planet("Neptune", DARK_BLUE, 340, 9, 0.006),
]

# Font for labels
font = pygame.font.Font(None, 20)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw sun
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)
    sun_label = font.render("Sun", True, (255, 255, 255))
    screen.blit(sun_label, (sun_x - 15, sun_y + sun_radius + 5))
    
    # Update and draw planets
    for planet in planets:
        planet.update()
        x, y = planet.draw(screen, sun_x, sun_y)
        
        # Draw planet label
        label = font.render(planet.name, True, (255, 255, 255))
        screen.blit(label, (x - 20, y + planet.radius + 5))
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit
pygame.quit()
sys.exit()
