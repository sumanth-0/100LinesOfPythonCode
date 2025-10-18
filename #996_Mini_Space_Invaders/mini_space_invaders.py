import os
import sys
import random
import time
from msvcrt import getch, kbhit if os.name == 'nt' else None

class SpaceInvaders:
    def __init__(self):
        self.width, self.height = 40, 20
        self.player_pos = self.width // 2
        self.enemies = [[i * 4 + 5, j * 2 + 2] for j in range(3) for i in range(6)]
        self.bullets = []
        self.enemy_bullets = []
        self.score = 0
        self.game_over = False
        self.direction = 1
        self.move_down = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw(self):
        self.clear_screen()
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw player
        if 0 <= self.player_pos < self.width:
            grid[self.height - 1][self.player_pos] = '^'
        
        # Draw enemies
        for ex, ey in self.enemies:
            if 0 <= ex < self.width and 0 <= ey < self.height:
                grid[ey][ex] = 'W'
        
        # Draw player bullets
        for bx, by in self.bullets:
            if 0 <= bx < self.width and 0 <= by < self.height:
                grid[by][bx] = '|'
        
        # Draw enemy bullets
        for bx, by in self.enemy_bullets:
            if 0 <= bx < self.width and 0 <= by < self.height:
                grid[by][bx] = 'v'
        
        # Print grid
        print('=' * (self.width + 2))
        for row in grid:
            print('|' + ''.join(row) + '|')
        print('=' * (self.width + 2))
        print(f'Score: {self.score} | Enemies: {len(self.enemies)} | Controls: A/D - Move, SPACE - Shoot, Q - Quit')
    
    def move_enemies(self):
        if not self.enemies:
            return
        
        edge = any(ex <= 0 or ex >= self.width - 1 for ex, ey in self.enemies)
        if edge:
            self.direction *= -1
            self.move_down = True
        
        for i in range(len(self.enemies)):
            if self.move_down:
                self.enemies[i][1] += 1
            self.enemies[i][0] += self.direction
        
        self.move_down = False
        
        # Random enemy shooting
        if self.enemies and random.random() < 0.1:
            shooter = random.choice(self.enemies)
            self.enemy_bullets.append([shooter[0], shooter[1] + 1])
    
    def update_bullets(self):
        # Update player bullets
        self.bullets = [[bx, by - 1] for bx, by in self.bullets if by > 0]
        
        # Update enemy bullets
        self.enemy_bullets = [[bx, by + 1] for bx, by in self.enemy_bullets if by < self.height]
        
        # Check bullet-enemy collisions
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break
        
        # Check enemy bullet-player collision
        for bullet in self.enemy_bullets:
            if bullet[0] == self.player_pos and bullet[1] >= self.height - 1:
                self.game_over = True
        
        # Check if enemies reached bottom
        if any(ey >= self.height - 2 for ex, ey in self.enemies):
            self.game_over = True
    
    def run(self):
        print("Mini Space Invaders - Press any key to start...")
        input()
        frame_count = 0
        
        while not self.game_over and self.enemies:
            self.draw()
            time.sleep(0.1)
            
            # Input handling (non-blocking)
            if os.name == 'nt' and kbhit():
                key = getch().decode('utf-8').lower()
                if key == 'a' and self.player_pos > 0:
                    self.player_pos -= 1
                elif key == 'd' and self.player_pos < self.width - 1:
                    self.player_pos += 1
                elif key == ' ':
                    self.bullets.append([self.player_pos, self.height - 2])
                elif key == 'q':
                    break
            
            frame_count += 1
            if frame_count % 5 == 0:
                self.move_enemies()
            
            self.update_bullets()
        
        self.clear_screen()
        if not self.enemies:
            print(f"Victory! Final Score: {self.score}")
        else:
            print(f"Game Over! Final Score: {self.score}")

if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()
