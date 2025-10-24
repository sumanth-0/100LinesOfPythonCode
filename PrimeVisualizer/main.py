import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

def generate_ulam_spiral(size):
    x, y = 0, 0
    dx, dy = 0, -1
    coords = []
    for n in range(1, size**2 + 1):
        if abs(x) <= size//2 and abs(y) <= size//2:
            if is_prime(n):
                coords.append((x, y))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return zip(*coords)

def plot_primes(size=101):
    print(f"Generating Ulam Spiral of size {size}×{size}...")
    xs, ys = generate_ulam_spiral(size)
    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, s=1, color='blue')
    plt.axis('off')
    plt.title(f"Ulam Spiral of Primes (size={size})")
    plt.show()

if __name__ == "__main__":
    plot_primes()