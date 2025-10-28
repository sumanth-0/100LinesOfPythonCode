import time

print("=== Focus Timer ===")
mins = int(input("Enter focus time (in minutes): "))
end = time.time() + mins * 60
distractions = []

while time.time() < end:
    left = int(end - time.time())
    print(f"\rTime left: {left//60}:{left%60:02d}  |  Type distraction or Enter to skip:", end=" ")
    thought = input()
    if thought.strip():
        distractions.append(thought)

print("\n⏰ Time’s up! Great job focusing!")
if distractions:
    with open("distractions.txt", "a") as f:
        for d in distractions:
            f.write(d + "\n")
    print("💭 Distractions saved in distractions.txt")
