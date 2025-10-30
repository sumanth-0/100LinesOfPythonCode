import matplotlib.pyplot as plt
import numpy as np

def det2d(a, b):
    return a[0] * b[1] - a[1] * b[0]

def reflect(v, n):
    n = n / np.linalg.norm(n)
    return v - 2 * np.dot(v, n) * n

def intersect_ray_segment(p, d, a, b):
    v_segment = b - a
    v_start = a - p
    denom = det2d(d, v_segment)
    if abs(denom) < 1e-6:
        return None
    t = det2d(v_start, v_segment) / denom
    u = det2d(v_start, d) / denom
    if t >= 1e-6 and 0 <= u <= 1:
        return p + t * d
    return None

mirrors, rays, click_points = [], [], []
mode = 'mirror'
fig, ax = plt.subplots()
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect('equal'); ax.grid(True)

def draw_scene():
    ax.clear()
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.grid(True)
    
    for a, b in mirrors:
        ax.plot([a[0], b[0]], [a[1], b[1]], 'k-', lw=2)
    
    for ray_pos, ray_dir in rays:
        points, pos, dir = [ray_pos.copy()], ray_pos.copy(), ray_dir / np.linalg.norm(ray_dir)
        
        for _ in range(10):
            closest_dist, closest_point, closest_normal = float('inf'), None, None
            
            for a, b in mirrors:
                pt = intersect_ray_segment(pos, dir, a, b)
                
                if pt is not None:
                    dist = np.linalg.norm(pt - pos)
                    
                    if dist < closest_dist:
                        closest_dist, closest_point = dist, pt
                        edge = b - a
                        normal = np.array([-edge[1], edge[0]])
                        if np.dot(normal, dir) > 0: normal = -normal
                        closest_normal = normal
            
            if closest_point is None:
                points.append(pos + dir * 20)
                break
            
            points.append(closest_point)
            pos = closest_point
            dir = reflect(dir, closest_normal)
        
        points = np.array(points)
        ax.plot(points[:, 0], points[:, 1], 'r-')
        ax.scatter(points[0, 0], points[0, 1], color='blue', s=50)

def onclick(event):
    global click_points, mode
    if event.inaxes != ax: return
    click_points.append(np.array([event.xdata, event.ydata]))
    
    if len(click_points) == 2:
        p1, p2 = click_points[0], click_points[1]
        if mode == 'mirror': mirrors.append((p1, p2))
        elif mode == 'ray': rays.append((p1, p2 - p1))
            
        click_points = []
        draw_scene()
        fig.canvas.draw()
        
def onkey(event):
    global mode, mirrors, rays
    if event.key == 'm': mode = 'mirror'
    elif event.key == 'l': mode = 'ray'
    elif event.key == 'c': mirrors, rays = [], []

    if event.key in ['m', 'l', 'c']:
        draw_scene()
        fig.canvas.draw()

    title = f"Mode: {mode.upper()} | Press 'm' (Mirror) or 'l' (Ray) | 'c' (Clear)"
    plt.title(title)
    
fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkey)
plt.title(f"Mode: {mode.upper()} | Press 'm' (Mirror) or 'l' (Ray) | 'c' (Clear)")
plt.show()
