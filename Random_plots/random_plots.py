"""
Generate random numbers and save histogram and scatter plot.

Usage:
    python tools/random_plots.py --count 1000 --outdir output --seed 42

This script creates two files in the output directory:
- histogram.png
- scatter.png
"""
from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt


def generate_random_data(count: int, seed: int | None = None):
    rng = np.random.default_rng(seed)
    # create two correlated random variables for scatter
    x = rng.normal(loc=0.0, scale=1.0, size=count)
    y = 0.5 * x + rng.normal(loc=0.0, scale=1.0, size=count)
    return x, y


def save_histogram(x, outpath: Path, bins: int = 50):
    plt.figure(figsize=(8, 5))
    plt.hist(x, bins=bins, color="#4C72B0", edgecolor="black", alpha=0.8)
    plt.title("Histogram of generated values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(outpath / "histogram.png", dpi=150)
    plt.close()


def save_scatter(x, y, outpath: Path):
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=10, alpha=0.6, color="#DD8452")
    plt.title("Scatter plot of correlated random variables")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(outpath / "scatter.png", dpi=150)
    plt.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1000, help="Number of random points to generate")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--outdir", type=str, default="tools/output", help="Directory to save plots")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    x, y = generate_random_data(args.count, args.seed)
    save_histogram(x, outdir)
    save_scatter(x, y, outdir)

    print(f"Saved histogram and scatter to {outdir}")


if __name__ == "__main__":
    main()
