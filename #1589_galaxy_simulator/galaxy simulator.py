import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm
import argparse

# ---------- (1) Generate Spiral Galaxy Points ----------
def generate_spiral_points(n_points=2000, n_arms=3, spiral_strength=5.0):
    """
    Generate points roughly distributed in a galaxy-like spiral pattern.
    - n_points: total stars
    - n_arms: number of spiral arms
    - spiral_strength: how tightly the arms are wound
    """
    # Input validation
    if n_points < 1:
        raise ValueError("n_points must be positive")
    if n_arms < 1:
        raise ValueError("n_arms must be positive")
    if spiral_strength <= 0:
        raise ValueError("spiral_strength must be positive")
    
    # Random radius (normalized 0..1)
    r = np.random.rand(n_points) ** 0.5  # more dense at center
    # Base angle for each point
    theta = 2 * np.pi * r * spiral_strength
    # Assign each point to an arm
    arm_offset = (np.random.randint(0, n_arms, n_points) * 2 * np.pi / n_arms)
    # Add small random jitter to angle
    theta += arm_offset + np.random.normal(0, 0.1, n_points)
    # Convert polar → Cartesian
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # Random brightness and color tint
    colors = np.random.rand(n_points)
    sizes = 2 + 6 * (1 - r) ** 2  # smaller at edges
    return x, y, colors, sizes


# ---------- (2) Create Galaxy Animation ----------
def make_galaxy_animation(out_path='galaxy_spiral.mp4', n_frames=300, fps=30):
    """
    Create an animated rotating spiral galaxy visualization.
    """
    # Generate initial galaxy
    x, y, colors, sizes = generate_spiral_points(n_points=2000, n_arms=4)

    # Set up plot
    fig, ax = plt.subplots(figsize=(6, 6))
    sc = ax.scatter(x, y, c=colors, s=sizes, cmap='plasma', alpha=0.8, lw=0)
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    ax.set_title("🌌 Rotating Spiral Galaxy", fontsize=14, pad=10)

    # Animation update
    def update(frame):
        angle = 2 * np.pi * (frame / n_frames)  # rotation over time
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        x_rot = x * cos_a - y * sin_a
        y_rot = x * sin_a + y * cos_a
        sc.set_offsets(np.column_stack((x_rot, y_rot)))
        # Optionally make colors pulse subtly
        sc.set_array((colors + 0.5 * np.sin(2 * np.pi * frame / n_frames)) % 1)
        return sc,

    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=tqdm(range(n_frames), desc="Generating frames"), 
        interval=1000/fps, 
        blit=True
    )

    # Try to save as mp4
    try:
        ani.save(out_path, writer='ffmpeg', fps=fps, dpi=150)
        print(f"🎬 Animation saved to {out_path}")
    except Exception:
        gif_path = out_path.replace('.mp4', '.gif')
        ani.save(gif_path, writer='pillow', fps=fps)
        print(f"🎞️ Animation saved as GIF to {gif_path}")

    plt.close(fig)


# ---------- (3) Run Example ----------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a rotating galaxy animation")
    parser.add_argument("--out", default="galaxy_spiral.mp4", help="Output file path")
    parser.add_argument("--frames", type=int, default=400, help="Number of frames")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    args = parser.parse_args()
    
    make_galaxy_animation(out_path=args.out, n_frames=args.frames, fps=args.fps)
