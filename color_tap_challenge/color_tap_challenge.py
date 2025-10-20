import random, time, sys, os

# Colors (ANSI escape codes)
COLORS = {
    "RED":"\033[31m", "GREEN":"\033[32m", "YELLOW":"\033[33m",
    "BLUE":"\033[34m", "MAGENTA":"\033[35m", "CYAN":"\033[36m", "RESET":"\033[0m"
}

score = 0
combo = 0
time_limit = 30
start = time.time()

def beep(correct=True):
    if sys.platform.startswith('win'):
        import winsound
        winsound.Beep(800 if correct else 400, 150)
    else:
        # Cross-platform beep
        print('\a', end='')

print("🎨 Type the COLOR OF THE TEXT, not the word itself!")
print("⏱ You have 30 seconds. Go!\n")

while time.time()-start < time_limit:
    word = random.choice(list(COLORS.keys())[:-1])
    color = random.choice(list(COLORS.keys())[:-1])
    remaining = int(time_limit - (time.time()-start))
    print(f"Time left: {remaining}s | Score: {score} | Combo: {combo}")
    print(COLORS[color] + word + COLORS["RESET"])
    answer = input("Your answer: ").strip().upper()
    if answer==color:
        score += 1
        combo += 1
        beep(True)
    else:
        combo = 0
        beep(False)
        print(f"Wrong! The correct color was {color}\n")
    print("\033[2J\033[H", end='')  # Clear screen for next round

print(f"\n⏰ Time's up! Your Final Score: {score}")
