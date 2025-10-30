#!/usr/bin/env python3
"""
Algorithmic Textile Pattern Generator
pip install pillow numpy
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random

# --- Parameters (tweak these) ---
TILE = 256            # tile size (px)
REPEAT = 4            # how many tiles per row/col for preview
WARP_FREQ = 3.5       # frequency of sinusoidal warp
WARP_AMP = 6.0        # amplitude of warp (px)
THREADS = 12          # number of threads per direction
THREAD_WIDTH = 18     # visual width of each thread
SEED = 42
PALETTE = [(230,220,200), (180,80,60), (70,110,150), (150,170,100)]

random.seed(SEED)
np.random.seed(SEED)

def smoothstep(x):
    return x*x*(3-2*x)

def make_thread_mask(sz, count, width, axis=0):
    """Create mask with alternating bright/dark bands (1d then expanded)."""
    arr = np.zeros((sz,sz), dtype=np.float32)
    spacing = sz / count
    for i in range(count):
        center = (i + 0.5) * spacing
        if axis == 0:
            x = np.arange(sz)
            band = np.clip(1 - np.abs((x - center) / (width/2)), 0, 1)
            arr += band[np.newaxis, :]
        else:
            y = np.arange(sz)
            band = np.clip(1 - np.abs((y - center) / (width/2)), 0, 1)
            arr += band[:, np.newaxis]
    # normalize and smooth
    arr = arr / arr.max()
    return smoothstep(arr)

def sinusoidal_warp_coords(sz, freq, amp, phase=0.0, axis=0):
    """Return displacement field for warp (dx,dy)"""
    x = np.linspace(0, 2*np.pi*freq, sz)
    y = np.linspace(0, 2*np.pi*freq, sz)
    if axis == 0:
        disp = np.sin(x + phase) * amp
        dx = np.zeros((sz,sz))
        dy = np.tile(disp, (sz,1))
    else:
        disp = np.cos(y + phase) * amp
        dx = np.tile(disp[:,None], (1,sz))
        dy = np.zeros((sz,sz))
    return dx, dy

def apply_warp(img_arr, dx, dy):
    """Simple backward mapping with bilinear sampling."""
    h,w = img_arr.shape[:2]
    yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')
    sx = np.clip((xx - dx).astype(np.float32), 0, w-1)
    sy = np.clip((yy - dy).astype(np.float32), 0, h-1)

    x0 = np.floor(sx).astype(np.int32); x1 = np.clip(x0+1,0,w-1)
    y0 = np.floor(sy).astype(np.int32); y1 = np.clip(y0+1,0,h-1)
    xf = sx - x0; yf = sy - y0

    out = np.zeros_like(img_arr)
    for c in range(3):
        c00 = img_arr[y0, x0, c]; c10 = img_arr[y0, x1, c]
        c01 = img_arr[y1, x0, c]; c11 = img_arr[y1, x1, c]
        out[:,:,c] = (c00*(1-xf)*(1-yf) + c10*xf*(1-yf) + c01*(1-xf)*yf + c11*xf*yf)
    return out.astype(np.uint8)

def blend_overunder(w_mask, we_mask):
    """Create an over/under boolean map: True where warp is on top."""
    # alternate by sign of combined mask and add jitter
    jitter = np.sin((w_mask + we_mask) * 12.7) * 0.08
    comb = w_mask - we_mask + jitter
    return comb > 0

def generate_tile():
    sz = TILE
    # base color variations
    bg = PALETTE[0]
    warp_col = PALETTE[1]
    weft_col = PALETTE[2]
    accent = PALETTE[3]

    # create flat threads
    w_mask = make_thread_mask(sz, THREADS, THREAD_WIDTH, axis=0)
    we_mask = make_thread_mask(sz, THREADS, THREAD_WIDTH, axis=1)

    # add per-thread color variation
    base = np.zeros((sz,sz,3), dtype=np.uint8) + np.array(bg, dtype=np.uint8)
    warp_layer = np.zeros_like(base); weft_layer = np.zeros_like(base)
    for c in range(3):
        warp_layer[:,:,c] = (warp_col[c] * (0.7 + 0.3*w_mask)).clip(0,255)
        weft_layer[:,:,c] = (weft_col[c] * (0.7 + 0.3*we_mask)).clip(0,255)

    # warp displacement fields
    dx_w, dy_w = sinusoidal_warp_coords(sz, WARP_FREQ, WARP_AMP, phase=0.0, axis=0)
    dx_e, dy_e = sinusoidal_warp_coords(sz, WARP_FREQ*0.9, WARP_AMP*0.6, phase=1.2, axis=1)

    # apply warp to layers
    warp_warped = apply_warp(warp_layer, dx_w, dy_w)
    weft_warped = apply_warp(weft_layer, dx_e, dy_e)

    # compute over/under map from original masks (so threads interlace)
    over_map = blend_overunder(w_mask, we_mask)

    # composite: where over_map True -> warp on top
    out = base.copy()
    out[~np.isclose(w_mask,0) | ~np.isclose(we_mask,0)] = out[~np.isclose(w_mask,0) | ~np.isclose(we_mask,0)]
    # blend per-pixel based on mask heights and over_map
    for y in range(sz):
        for x in range(sz):
            wm = w_mask[y,x]; em = we_mask[y,x]
            if wm < 1e-3 and em < 1e-3:
                continue
            if over_map[y,x]:
                # warp on top
                top = warp_warped[y,x]; bot = weft_warped[y,x]
            else:
                top = weft_warped[y,x]; bot = warp_warped[y,x]
            # simple lighting: darker on bottom thread edges
            shade = 0.9 + 0.1*(wm+em)
            pix = (top.astype(np.float32)*0.95 + bot.astype(np.float32)*0.05) * shade
            out[y,x] = np.clip(pix,0,255).astype(np.uint8)

    # subtle blur + noise to simulate fabric
    img = Image.fromarray(out, 'RGB').filter(ImageFilter.GaussianBlur(radius=0.6))
    noise = np.random.normal(0, 6, (sz,sz,3)).astype(np.int16)
    arr = np.array(img).astype(np.int16) + noise
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, 'RGB')

def make_pattern_preview(tile, repeat=REPEAT):
    w,h = tile.size
    canvas = Image.new('RGB', (w*repeat, h*repeat), PALETTE[0])
    for i in range(repeat):
        for j in range(repeat):
            canvas.paste(tile, (i*w, j*h))
    return canvas

if __name__ == "__main__":
    tile = generate_tile()
    tile.save("textile_tile.png")
    print("Saved textile_tile.png")
    preview = make_pattern_preview(tile, REPEAT)
    preview.save("textile_preview.png")
    print("Saved textile_preview.png (tiled preview)")
