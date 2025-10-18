import random, time, os

# --- Config ---
COLOR_MAP = {'R':"RED",'B':"BLUE",'G':"GREEN",'Y':"YELLOW",'P':"PURPLE",'O':"ORANGE"}
MIN_LEN, MAX_LEN, DISPLAY_TIME = 3, 8, 2.0
# --------------

def clear(): os.system('cls' if os.name=='nt' else 'clear')

def generate_sequence():
    """Create random mix of colors and numbers with random length."""
    n = random.randint(MIN_LEN, MAX_LEN)
    seq, shown = [], []
    for _ in range(n):
        if random.choice([1,0]): 
            c = random.choice(list(COLOR_MAP.keys()))
            seq.append(c); shown.append(COLOR_MAP[c])
        else:
            num = random.randint(0,100000)
            seq.append(num); shown.append(str(num))
    return seq, shown

def get_user_input(seq):
    """Prompt user to recall the sequence."""
    n = len(seq)
    print(f"Enter the {n} items you saw (R,B,G,Y,P,O or 0–9):")
    while True:
        try:
            ans = input("Your sequence: ").upper().split()
            if len(ans)!=n: print(f"Enter exactly {n} items."); continue
            out=[]
            for x in ans: out.append(x if x in COLOR_MAP else int(x))
            return out
        except ValueError:
            print("Invalid input. Use only color letters or digits.")

def main():
    seq, shown = generate_sequence()
    clear(); print("✨ REMEMBER THIS SEQUENCE! ✨\n")
    print(' | '.join(shown)); time.sleep(DISPLAY_TIME); clear()
    user = get_user_input(seq)
    score = sum(a==b for a,b in zip(seq,user))
    fmt = lambda x: COLOR_MAP.get(x,str(x))
    clear()
    print("--- RESULTS ---")
    print("Original:", ' | '.join(shown))
    print("Your Input:", ' | '.join(fmt(x) for x in user))
    print(f"\nScore: {score} / {len(seq)}")
    print("🔥 PERFECT RECALL! 🔥" if score==len(seq) else "🧠 Keep practicing!")
    print("-----------------")

if __name__=="__main__": main()
