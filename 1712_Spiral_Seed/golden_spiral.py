#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

def make_spiral(n=500, angle_deg=137.5, scale=4.0):
    theta = np.deg2rad(angle_deg)
    i = np.arange(1, n + 1)
    angles = i * theta
    radii = scale * np.sqrt(i)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y, i

def plot_spiral(x, y, i, size=10, cmap="viridis", background="white", figsize=(7,7), save=None):
    plt.figure(figsize=figsize, facecolor=background)
    ax = plt.gca()
    ax.set_facecolor(background)
    sizes = size * (1 + (i / i.max()))  # slight growth with index
    scatter = ax.scatter(x, y, s=sizes, c=i, cmap=cmap, linewidths=0, alpha=0.95)
    ax.set_aspect("equal")
    ax.axis("off")
    if save:
        plt.savefig(save, bbox_inches="tight", dpi=300, facecolor=background)
    else:
        plt.show()
    plt.close()

def main():
    p = argparse.ArgumentParser(description="Draw sunflower-like seed spiral using the golden angle")
    p.add_argument("-n", "--num", type=int, default=1000, help="number of seeds")
    p.add_argument("-a", "--angle", type=float, default=137.5, help="angle in degrees (golden angle ≈ 137.5)")
    p.add_argument("-s", "--scale", type=float, default=3.2, help="radial scale factor")
    p.add_argument("-p", "--point", type=float, default=6.0, help="base point size")
    p.add_argument("-c", "--cmap", default="viridis", help="matplotlib colormap")
    p.add_argument("-b", "--bg", default="white", help="background color")
    p.add_argument("-o", "--output", default=None, help="output filename (png or svg). If omitted, shows window")
    args = p.parse_args()

    x, y, i = make_spiral(n=args.num, angle_deg=args.angle, scale=args.scale)
    plot_spiral(x, y, i, size=args.point, cmap=args.cmap, background=args.bg, save=args.output)

if __name__ == "__main__":
    main()
