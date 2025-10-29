import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm

# ---- Config ----
W, H = 480, 320         # canvas resolution
SCALE = 3.0             # spatial frequency scale
OCTAVES = 5             # number of layered sine fields
SPEED = 0.6             # global time speed
FPS = 30
DURATION = 20           # seconds

# ---- helper: layered drifting sinusoids to simulate organic noise ----
rng = np.random.default_rng(1234)
kx = np.linspace(0, SCALE * 2*np.pi, W)
ky = np.linspace(0, SCALE * 2*np.pi, H)
X, Y = np.meshgrid(kx, ky)

# Pre-generate random params for octaves
amps = np.exp(-np.linspace(0, 2.5, OCTAVES))  # decreasing amplitudes
freqs = 2.0 ** np.arange(OCTAVES)             # increasing frequencies
phases = rng.uniform(0, 2*np.pi, size=(OCTAVES, 2))  # (phase_x, phase_y) per octave
directions = rng.normal(size=(OCTAVES, 2))
directions /= np.linalg.norm(directions, axis=1)[:, None]

def field(t):
    """Compute 2D scalar field at time t (0..inf)."""
    f = np.zeros((H, W), dtype=np.float32)
    for i in range(OCTAVES):
        fx = freqs[i]
        amp = amps[i]
        dx, dy = directions[i]
        # drifting phase offsets
        ox = phases[i,0] + t * SPEED * (0.2 + 0.6*i/OCTAVES) * dx
        oy = phases[i,1] + t * SPEED * (0.2 + 0.6*i/OCTAVES) * dy
        # layered sinusoids with slightly different orientation
        f += amp * np.sin(fx * (X * (1.0 + 0.02*i)) + ox) * np.cos(fx * (Y * (1.0 - 0.015*i)) + oy)
    # add radial hotspot to feel like lava pool
    cx, cy = W*0.5, H*0.45
    rx = (np.linspace(0, W-1, W) - cx)[None, :]
    ry = (np.linspace(0, H-1, H) - cy)[:, None]
    r = np.sqrt((rx**2 + ry**2)) / (min(W,H)*0.6)
    f += 1.6 * np.exp(-3.5 * r**2)
    # subtle perturbation for veins
    f += 0.2 * np.sin(3.0 * (X*0.7 + Y*0.3 + 0.8*t))
    return f

# ---- visualization ----
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_axis_off()
img = ax.imshow(np.zeros((H, W)), interpolation='bicubic', vmin= -2.0, vmax=2.8, cmap=cm.inferno)

# custom color modulation to add bright lava veins
def shade(field_arr, t):
    # normalize and bias
    A = field_arr
    A = (A - A.min()) / (A.max() - A.min() + 1e-9)
    # boost contrast with gamma and a moving threshold to make veins pulse
    A = np.power(A, 0.6)
    vein = np.clip((A - 0.78 + 0.08*np.sin(2.0*t)) * 6.0, 0, 1)
    # mix base inferno colormap with white-hot veins
    base = cm.inferno(A)
    # add glowing veins by blending toward yellow/white
    glow = np.stack([np.ones_like(A), 0.95*np.ones_like(A), 0.6*np.ones_like(A), vein], axis=-1)
    out = np.clip(base * (1 - vein[...,None]) + glow * vein[...,None], 0, 1)
    # slight vignette darkening
    yy = np.linspace(-1,1,H)[:,None]
    xx = np.linspace(-1,1,W)[None,:]
    vign = 1.0 - 0.35*(xx**4 + yy**4)
    out[..., :3] *= vign[...,None]
    return out

TOTAL_FRAMES = int(FPS * DURATION)
def update(frame):
    t = frame / FPS
    f = field(t)
    img.set_data(shade(f, t))
    return (img,)

anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)
plt.show()
