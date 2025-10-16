import time
import random

# --- List of random sentences ---
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast takes patience and practice.",
    "Keep calm and code in Python.",
    "Simple projects build strong skills.",
    "Learning never exhausts the mind.",
    "Creativity is intelligence having fun."
]

# --- Utility for colored text ---
def color(txt, code): return f"\033[{code}m{txt}\033[0m"

def typing_test():
    """Run one typing round and return elapsed time, WPM, accuracy"""
    sentence = random.choice(sentences)
    print(color("\n=== 🧠 Typing Speed Challenge ===", "1;36"))
    print("\nType this sentence exactly:\n")
    print(color(sentence, "33"))
    input("\nPress Enter when ready to start...")

    # Start timing
    start = time.time()
    typed = input("\nStart typing:\n")
    end = time.time()

    # --- Calculations ---
    elapsed = end - start
    time_in_min = elapsed / 60
    words = len(typed.split())
    wpm = words / time_in_min if time_in_min > 0 else 0

    # Accuracy and errors
    correct = sum(1 for i, c in enumerate(typed) if i < len(sentence) and c == sentence[i])
    accuracy = (correct / len(sentence)) * 100
    errors = abs(len(sentence) - len(typed)) + sum(
        1 for i in range(min(len(sentence), len(typed))) if sentence[i] != typed[i]
    )

    # --- Display Results ---
    print(color("\n--- 📊 Results ---", "1;34"))
    print(f"⏱️  Time taken  : {elapsed:.2f} seconds")
    print(f"💨 Speed       : {wpm:.2f} WPM")
    print(f"🎯 Accuracy    : {accuracy:.1f}%")
    print(f"❌ Errors      : {errors}")
    return elapsed, wpm, accuracy

def main():
    times = []
    print(color("Welcome to the Typing Speed Challenge! 🚀", "1;32"))

    try:
        while True:
            elapsed, wpm, acc = typing_test()
            times.append(elapsed)

            # Best and worst times
            best = min(times)
            worst = max(times)

            print(color("\n--- 🏁 Session Stats ---", "1;35"))
            print(f"🔥 Best Time  : {best:.2f} s")
            print(f"🐢 Worst Time : {worst:.2f} s")
            print(f"🧮 Rounds     : {len(times)}")

            again = input(color("\nPlay again? (y/n): ", "1;33")).strip().lower()
            if again == 'n':
                break
    except KeyboardInterrupt:
        print("\nExiting...")

    if times:
        print(color("\n=== 🏆 Final Summary ===", "1;36"))
        print(f"Rounds Played : {len(times)}")
        print(f"Best Time     : {min(times):.2f} s")
        print(f"Worst Time    : {max(times):.2f} s")
        print(color("\nThanks for playing! 🎉", "1;32"))

if __name__ == "__main__":
    main()