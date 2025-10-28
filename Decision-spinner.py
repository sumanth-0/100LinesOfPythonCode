import random
import time
import sys

print("🎯 Welcome to the Decision Spinner 🎯")
print("Can't decide? Let fate choose for you!\n")

options = input("Enter your choices separated by commas: ").split(",")
options = [opt.strip() for opt in options if opt.strip()]

if len(options) < 2:
    print("Please enter at least two options to spin!")
    sys.exit()

spinner_icons = ["🍕", "🍔", "🍟", "🍝", "🍣", "🌮", "🥗", "🍩", "🍿", "🥪"]

print("\nSpinning the wheel...\n")

for i in range(20):
    icon = random.choice(spinner_icons)
    choice = random.choice(options)
    sys.stdout.write(f"\r{icon} {choice} {icon}")
    sys.stdout.flush()
    time.sleep(0.15)

print("\n")
for _ in range(3):
    print("🤔 Choosing", "." * (_ + 1))
    time.sleep(0.5)

final_choice = random.choice(options)
print("\n🎉 The spinner has spoken! 🎉")
print(f"✨ Your choice is: {final_choice.upper()} ✨")

print(random.choice([
    "Fate never lies 🔮",
    "That’s destiny, my friend 😄",
    "No take-backs now 😜",
    "Perfect pick! 🍀",
    "You were meant to choose this 💫"
]))
