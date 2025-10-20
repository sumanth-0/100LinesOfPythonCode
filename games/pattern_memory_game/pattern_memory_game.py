## Pattern Memory Game (≤100 lines)
# Rules: Watch the flashing sequence, then type it back. Longest streak = your score.
import os, random, time, sys

SYMBOLS = [
    ("R", "Red",    "\033[91m"),
    ("G", "Green",  "\033[92m"),
    ("B", "Blue",   "\033[94m"),
    ("Y", "Yellow", "\033[93m"),
]
RESET = "\033[0m"

def clear():
    # Cross-platform-ish clear; ANSI works in most terminals
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\033[2J\033[H"); sys.stdout.flush()

def show_banner():
    print("=== Pattern Memory Game ===")
    print("Type the sequence as letters without spaces (e.g., RGYB).")
    print("Keys: R=Red, G=Green, B=Blue, Y=Yellow\n")

def flash(seq, speed):
    clear(); show_banner()
    print("Memorize:")
    for s in seq:
        ch, name, color = next(x for x in SYMBOLS if x[0] == s)
        print(color + ch + " " + name + RESET, flush=True)
        time.sleep(speed)
        clear(); show_banner()
        print("Memorize:")
        time.sleep(0.12)
    time.sleep(0.15)

def get_user(len_expected):
    ans = input(f"Repeat {len_expected} letters (R/G/B/Y): ").strip().upper()
    return "".join(c for c in ans if c in "RGBY")

def main():
    random.seed()  # fresh each run
    seq, round_no, speed = [], 0, 0.6
    best = 0
    while True:
        seq.append(random.choice("RGBY"))
        round_no += 1
        flash(seq, speed=max(0.25, speed * 0.97))  # slight speed-up
        user = get_user(len(seq))
        if user != "".join(seq):
            print("\n💥 Wrong! Final score:", round_no - 1, "| Best:", max(best, round_no - 1))
            again = input("Play again? (y/n): ").strip().lower()
            if again.startswith("y"):
                seq, round_no, speed = [], 0, 0.6
                clear(); show_banner()
                continue
            else:
                break
        best = max(best, round_no)
        print("✅ Correct! Next round...\n")
        time.sleep(0.6)
        clear(); show_banner()
    print("Thanks for playing!")

if __name__ == "__main__":
    clear(); show_banner(); main()
