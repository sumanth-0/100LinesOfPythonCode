import random, sys

class M:
    def __init__(self, r=9, c=9, m=10):
        if m >= r * c: raise ValueError("too many mines")
        self.r, self.c, self.m = r, c, m
        self.b = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
        p = random.sample(range(r * c), m)
        for i in p: self.b[i // c][i % c][0] = 1
        for i in range(r):
            for j in range(c):
                if not self.b[i][j][0]:
                    self.b[i][j][1] = sum(self.b[x][y][0] for x in range(max(0, i-1), min(r, i+2))
                                          for y in range(max(0, j-1), min(c, j+2)) if (x, y) != (i, j))
        self.v, self.o, self.n = 0, 0, 0

    def R(self, i, j):
        if self.o or self.v or self.b[i][j][2] or self.b[i][j][3]: return
        self.b[i][j][2] = 1; self.n += 1
        if self.b[i][j][0]: self.o = 1; return
        if self.b[i][j][1] == 0:
            for x in range(max(0, i-1), min(self.r, i+2)):
                for y in range(max(0, j-1), min(self.c, j+2)):
                    if not self.b[x][y][2]: self.R(x, y)
        if self.n == self.r * self.c - self.m: self.v = 1

    def F(self, i, j):
        if self.o or self.v or self.b[i][j][2]: return
        self.b[i][j][3] = 1 - self.b[i][j][3]

    def D(self, a=0):
        print("   " + " ".join(f"{j+1:2}" for j in range(self.c)))
        print("  +" + "--" * (self.c) + "+")
        for i in range(self.r):
            l = []
            for j in range(self.c):
                if a or self.b[i][j][2]:
                    ch = "*" if self.b[i][j][0] else " " if self.b[i][j][1] == 0 else str(self.b[i][j][1])
                else: ch = "F?"[not self.b[i][j][3]]
                l.append(f"{ch:2}")
            print(f"{i+1:2}|" + " ".join(l) + "|")
        print("  +" + "--" * (self.c) + "+")
        print(f"Mines left: {self.m - sum(self.b[i][j][3] for i in range(self.r) for j in range(self.c))}")
        if self.o: print("BOOM! Game over.")
        if self.v: print("Victory!")

def P(p, d):
    try: r = input(f"{p} [{d}]: ").strip(); return int(r) if r else d
    except: print("Invalid, using default."); return d

def H(): print("r row col: reveal\nf row col: flag\nq: quit")

def G(r=9, c=9, m=10):
    try: g = M(r, c, m)
    except ValueError as e: print(e); return
    print("Minesweeper"); H()
    while 1:
        g.D()
        if g.o or g.v: break
        x = input("Command: ").strip().lower().split()
        if not x: continue
        if x[0] == 'q': break
        if len(x) != 3 or x[0] not in 'r f': print("Invalid"); H(); continue
        try: i, j = int(x[1]) - 1, int(x[2]) - 1
        except: print("Numbers?"); continue
        if not (0 <= i < r and 0 <= j < c): print("Out of range"); continue
        if x[0] == 'r': g.R(i, j)
        else: g.F(i, j)

def main():
    r = P("Rows", 9); c = P("Cols", 9); m = P("Mines", 10)
    m = max(1, min(m, r * c - 1))
    print(f"{r}x{c} with {m} mines")
    G(r, c, m)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("\nBye")