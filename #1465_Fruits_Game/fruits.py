import pygame, random
pygame.init()

# Screen setup
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruits Collecting Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors & basket settings
WHITE, BLACK, RED, GREEN = (255,255,255), (0,0,0), (255,0,0), (0,255,0)
basket_w, basket_h = 80, 20
basket_x, basket_y = WIDTH//2 - basket_w//2, HEIGHT - basket_h - 10
basket_speed = 7

# Fruit settings
fruit_w, fruit_h = 30, 30
fruit_speed = 3
fruits = []
spawn_delay = 80  # frames between fruit spawns
frame_count = 0

score, lives = 0, 3

def draw_basket(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, basket_w, basket_h))

def draw_fruit(f):
    pygame.draw.ellipse(screen, RED, f)

def check_collision(fruit, basket):
    return fruit.colliderect(basket)

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Event handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # Basket movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed
    basket_x = max(0, min(WIDTH - basket_w, basket_x))

    # Spawn fruits periodically
    frame_count += 1
    if frame_count >= spawn_delay:
        frame_count = 0
        fruits.append(pygame.Rect(random.randint(0, WIDTH - fruit_w), 0, fruit_w, fruit_h))

    basket_rect = pygame.Rect(basket_x, basket_y, basket_w, basket_h)

    # Move fruits and check for catch/miss
    for f in fruits[:]:
        f.y += fruit_speed
        if f.y > HEIGHT:  # Missed fruit
            fruits.remove(f)
            lives -= 1
        elif check_collision(f, basket_rect):  # Caught fruit
            fruits.remove(f)
            score += 1
            # Increase difficulty
            if score % 5 == 0 and fruit_speed < 10:
                fruit_speed += 0.5
                if spawn_delay > 20:
                    spawn_delay -= 5

    # Draw basket and fruits
    draw_basket(basket_x, basket_y)
    for f in fruits:
        draw_fruit(f)

    # Display score and lives
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, BLACK), (WIDTH - 110, 10))

    # Game over condition
    if lives <= 0:
        go_text = font.render("Game Over! Press R to Restart", True, RED)
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    waiting = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                    # Reset game
                    score, lives = 0, 3
                    fruit_speed = 3
                    spawn_delay = 80
                    fruits.clear()
                    basket_x = WIDTH//2 - basket_w//2
                    waiting = False

    pygame.display.flip()

pygame.quit()
