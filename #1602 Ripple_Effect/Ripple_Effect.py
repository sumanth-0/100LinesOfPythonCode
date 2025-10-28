import math, random, time
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle

# ---------- Parameters ----------
FIGSIZE = (6, 6)
BG_COLOR = "#0b1220"
RIPPLE_COLOR = (0.4, 0.8, 1.0)  # RGB
MAX_RADIUS = 1.5
SPEED = 0.6
RINGS_PER_DROP = 4
RING_SPACING = 0.08
FPS = 30

# ---------- Drop model ----------
class Drop:
    def __init__(self, x, y, t0=None):
        self.x = x
        self.y = y
        self.t0 = time.time() if t0 is None else t0
        self.rings = RINGS_PER_DROP
        self.speed = SPEED * (0.8 + 0.4 * random.random())
        self.max_r = MAX_RADIUS * (0.8 + 0.5 * random.random())

    def age(self, now):
        return now - self.t0

    def ring_radius(self, age, i):
        return self.speed * age + i * RING_SPACING

    def alive(self, now):
        return self.ring_radius(self.age(now), 0) < self.max_r

# ---------- Setup plot ----------
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', 'box')
ax.axis("off")

drops = []

def on_click(event):
    if event.inaxes != ax:
        return
    x, y = event.xdata, event.ydata
    drops.append(Drop(x, y))
    splash = Circle((x, y), 0.01, color=RIPPLE_COLOR, alpha=0.9)
    ax.add_patch(splash)
    fig.canvas.draw_idle()
    plt.pause(0.05)
    splash.remove()

fig.canvas.mpl_connect("button_press_event", on_click)

# ---------- Animation ----------
def update(frame):
    now = time.time()
    # Remove previous ripple patches
    for patch in ax.patches[:]:
        patch.remove()
    live = []
    for drop in drops:
        if not drop.alive(now):
            continue
        age = drop.age(now)
        for i in range(drop.rings):
            r = drop.ring_radius(age, i)
            if r <= 0:
                continue
            life_frac = r / drop.max_r
            alpha = max(0, 1 - life_frac)
            ring_alpha = alpha * (1 - i / (drop.rings + 1))
            lw = 2.2 * (1 - life_frac) + 0.4
            col = (*RIPPLE_COLOR, ring_alpha)
            circ = Circle((drop.x, drop.y), r, linewidth=lw, fill=False, edgecolor=col)
            ax.add_patch(circ)
        live.append(drop)
    drops[:] = live
    return ax.patches

ani = animation.FuncAnimation(fig, update, frames=200, interval=1000/FPS, blit=False)
plt.title("Click to drop — ripples expand outward", color="white", pad=12)
plt.show()
