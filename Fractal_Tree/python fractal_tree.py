# fractal_tree.py — Draw a recursive fractal tree with matplotlib
# Requires: matplotlib
import math
import matplotlib.pyplot as plt

def draw_tree(ax, x, y, angle_deg, length, depth,
              shrink=0.67, spread_deg=25, min_length=1.0):
    """Recursive function to draw a fractal tree branch."""
    if depth <= 0 or length < min_length:
        return
    # compute end point
    a = math.radians(angle_deg)
    x2 = x + length * math.cos(a)
    y2 = y + length * math.sin(a)
    ax.plot([x, x2], [y, y2], linewidth=max(0.5, depth * 0.6))
    # left and right branches
    draw_tree(ax, x2, y2, angle_deg - spread_deg, length * shrink, depth - 1,
              shrink, spread_deg, min_length)
    draw_tree(ax, x2, y2, angle_deg + spread_deg, length * shrink, depth - 1,
              shrink, spread_deg, min_length)
    # optional center branch for a bushier look
    if depth % 2 == 0:
        draw_tree(ax, x2, y2, angle_deg, length * shrink, depth - 1,
                  shrink, spread_deg, min_length)

def main():
    fig, ax = plt.subplots(figsize=(7, 9))
    ax.set_aspect('equal')
    ax.axis('off')

    # initial trunk parameters
    start_x, start_y = 0.0, 0.0
    initial_angle = 90      # straight up
    initial_length = 100.0
    max_depth = 10

    draw_tree(ax, start_x, start_y, initial_angle, initial_length, max_depth,
              shrink=0.68, spread_deg=22, min_length=1.0)

    pad = 10
    ax.set_xlim(-initial_length - pad, initial_length + pad)
    ax.set_ylim(0, initial_length * 1.15 + pad)
    plt.show()

if __name__ == "__main__":
    main()
