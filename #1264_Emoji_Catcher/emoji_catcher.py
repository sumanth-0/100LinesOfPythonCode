import random
import time
import os

WIDTH = 20
HEIGHT = 10
BASKET = "🧺"
FALLING = ["🍎", "🍌", "🍒", "🍇", "🍉"]

def clear(): os.system('cls' if os.name=='nt' else 'clear')

def draw(basket_pos, emoji_pos):
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if (x, y) == emoji_pos:
                line += random.choice(FALLING)
            elif y == HEIGHT-1 and x == basket_pos:
                line += BASKET
            else:
                line += " "
        print(line)
    print("-"*WIDTH)

def main():
    basket = WIDTH // 2
    score = 0
    while True:
        emoji_x = random.randint(0, WIDTH-1)
        for y in range(HEIGHT):
            clear()
            draw(basket, (emoji_x, y))
            time.sleep(0.1)
        if emoji_x == basket:
            print("🎉 Caught it!")
            score += 1
        else:
            print("💥 Missed!")
            score -= 1
        print(f"Score: {score}")
        move = input("Move Left [a], Right [d], Quit [q]: ").lower()
        if move == 'a' and basket > 0:
            basket -= 1
        elif move == 'd' and basket < WIDTH-1:
            basket += 1
        elif move == 'q':
            break
    print(f"Game Over! Final Score: {score}")

if __name__ == "__main__":
    main()
