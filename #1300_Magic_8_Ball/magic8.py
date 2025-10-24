import random, time

RESPONSES = [
    "Yes, definitely!",
    "Nope, Never, Dont even think about it!",
    "Nope, try again later 😏",
    "Maybe... if you're lucky 🍀",
    "Absolutely not 😂",
    "Yes, but only on weekends 🗓️",
    "Ask again after pizza 🍕",
    "Unclear... blame quantum physics 🌀",
    "Sure thing, it's obvious 😎",
    "Possibly... but keep dreaming 💭"
]

def magic_8ball():
    print("🎱 Welcome to the Magic 8-Ball 🎱\n")
    question = input("Ask your question: ")
    print("\nShaking the ball", end="")
    for _ in range(3):
        time.sleep(0.6)
        print(".", end="")
    time.sleep(0.8)

    print("\n\n")
    print(f"The 8-Ball says: \n{random.choice(RESPONSES)}\n")

if __name__ == "__main__":
    magic_8ball()
