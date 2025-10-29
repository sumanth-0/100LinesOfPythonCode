import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon

def resample_poly(pts, n):
    pts = np.asarray(pts)
    if np.allclose(pts[0], pts[-1]):
        pts = pts[:-1]
    # compute cumulative distances along closed curve
    closed = np.vstack([pts, pts[0]])
    seg = np.sqrt(((closed[1:] - closed[:-1])**2).sum(axis=1))
    cum = np.r_[0, np.cumsum(seg)]
    total = cum[-1]
    # target distances
    t = np.linspace(0, total, n+1)[:-1]
    xs = np.interp(t, cum, closed[:,0])
    ys = np.interp(t, cum, closed[:,1])
    return np.column_stack([xs, ys])

def morph(a_pts, b_pts, frames=60):
    n = max(len(a_pts), len(b_pts), 32)
    A = resample_poly(a_pts, n)
    B = resample_poly(b_pts, n)
    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_aspect('equal'); ax.axis('off')
    poly = Polygon(A, closed=True, facecolor='#ffcc66', edgecolor='#330000', alpha=0.9)
    ax.add_patch(poly)
    ax.set_xlim(min(A[:,0].min(), B[:,0].min())-0.5, max(A[:,0].max(), B[:,0].max())+0.5)
    ax.set_ylim(min(A[:,1].min(), B[:,1].min())-0.5, max(A[:,1].max(), B[:,1].max())+0.5)

    def interp(t):
        # smoothstep easing
        s = t*t*(3 - 2*t)
        return (1-s)*A + s*B

    def update(i):
        t = i/(frames-1)
        pts = interp(t)
        poly.set_xy(pts)
        return (poly,)

    return FuncAnimation(fig, update, frames=frames, interval=30, blit=True)

if __name__ == "__main__":
    # Example polygons (star -> rounded blob)
    star = [(0,1.0),(0.22,0.22),(1.0,0.0),(0.22,-0.22),(0,-1.0),(-0.22,-0.22),(-1.0,0.0),(-0.22,0.22),(0,1.0)]
    theta = np.linspace(0,2*np.pi,9)[:-1]
    blob = [(0.6*np.cos(t)+0.2*np.sin(2*t), 0.7*np.sin(t)) for t in theta]
    anim = morph(star, blob, frames=80)
    plt.show()
