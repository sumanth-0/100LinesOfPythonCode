import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_stars = 3000  # total number of stars
num_arms = 4      # spiral arms
rotation_speed = 0.01  # rotation speed
spread = 0.3      # spread of stars around arms
arm_offset = 2 * np.pi / num_arms  # angle between arms
arm_width = 0.5   # not used, but could control arm thickness

# Generate star positions
radii = np.random.rand(num_stars) ** 0.5 * 10  # denser center
arms = np.random.randint(0, num_arms, num_stars)
angles = (
    radii * 0.5
    + arms * arm_offset
    + np.random.randn(num_stars) * spread  # add randomness
)

x = radii * np.cos(angles)  # x positions
y = radii * np.sin(angles)  # y positions

# Assign colors and sizes
colors = np.random.choice(
    ['white', 'lightblue', 'lightcyan'],
    num_stars,
    p=[0.7, 0.2, 0.1]
)
sizes = np.random.choice(
    [0.5, 1, 2, 3],
    num_stars,
    p=[0.5, 0.3, 0.15, 0.05]
)

fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
scat = ax.scatter(x, y, s=sizes, c=colors, alpha=0.8)
ax.set_facecolor('black')
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Spiral Galaxy Rotation', color='white', fontsize=16, pad=20)
core = plt.Circle((0, 0), 0.3, color='yellow', alpha=0.8, zorder=10)  # galaxy core
ax.add_patch(core)


def update(frame):
    global angles
    # inner stars rotate faster
    rotation_rates = rotation_speed * (1 + 2 / (radii + 1))
    angles += rotation_rates
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    scat.set_offsets(np.c_[x, y])
    return scat,


ani = animation.FuncAnimation(
    fig,
    update,
    frames=None,
    interval=30,
    blit=True,
    repeat=True,
    cache_frame_data=False 
)

plt.tight_layout()
plt.show()