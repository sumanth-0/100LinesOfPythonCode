import random, math
import matplotlib.pyplot as plt
from matplotlib import animation

# ---------- Parameters ----------
FIGSIZE = (6, 8)
BG_COLOR = "#0b1220"
LINE_COLOR = (0.8, 0.9, 1.0)
MAX_DEPTH = 6       # branch recursion depth
BRANCH_ANGLE = 30   # max deviation in degrees
BRANCH_LEN = 0.15
FPS = 20

# ---------- Branch model ----------
class Branch:
    def __init__(self, x, y, angle, depth):
        self.x = x
        self.y = y
        self.angle = angle
        self.depth = depth
        self.children = []

    def generate_children(self):
        if self.depth >= MAX_DEPTH:
            return
        n_children = random.choice([1,2])
        for _ in range(n_children):
            delta_angle = random.uniform(-BRANCH_ANGLE, BRANCH_ANGLE)
            new_angle = self.angle + math.radians(delta_angle)
            length = BRANCH_LEN * (0.7 + 0.6*random.random())
            new_x = self.x + length * math.cos(new_angle)
            new_y = self.y + length * math.sin(new_angle)
            child = Branch(new_x, new_y, new_angle, self.depth +1)
            self.children.append(child)
            child.generate_children()

# ---------- Generate lightning ----------
def generate_lightning():
    root = Branch(0, 1, -math.pi/2, 0)  # start from top center going down
    root.generate_children()
    return root

# ---------- Flatten branches for drawing ----------
def flatten_branches(branch):
    lines = []
    for child in branch.children:
        lines.append((branch.x, branch.y, child.x, child.y))
        lines += flatten_branches(child)
    return lines

# ---------- Setup plot ----------
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(-1,1)
ax.set_ylim(0,1.5)
ax.axis("off")

lightning_lines = []

# ---------- Animation ----------
def update(frame):
    ax.clear()
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(-1,1)
    ax.set_ylim(0,1.5)
    ax.axis("off")
    # generate new random lightning each frame
    root = generate_lightning()
    for x0,y0,x1,y1 in flatten_branches(root):
        ax.plot([x0,x1],[y0,y1], color=LINE_COLOR, lw=1.5)
    return ax.lines

ani = animation.FuncAnimation(fig, update, frames=100, interval=1000/FPS, blit=False)
plt.title("Random Lightning Simulation", color="white", pad=12)
plt.show()
