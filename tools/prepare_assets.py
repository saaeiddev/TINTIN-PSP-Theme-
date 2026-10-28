#!/usr/bin/env python3
"""Prepare focus graphics and preview resources from exported PNGs."""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'

def focus(source, dest):
    image = Image.open(source).convert('RGBA')
    width, height = image.size
    w, h = width + 16, height + 16
    core = np.zeros((h, w), dtype=np.float64)
    core[8:8+height, 8:8+width] = np.asarray(image)[:, :, 3]
    radius = 6
    kernel = np.array([math.exp(-(i*i)/(2*3*3)) for i in range(-radius, radius+1)])
    kernel /= kernel.sum()
    def blur_axis(a, axis):
        return np.apply_along_axis(lambda row: np.convolve(np.pad(row, (radius, radius), mode='edge'), kernel, mode='valid'), axis, a)
    blurred = blur_axis(blur_axis(core, 1), 0)
    halo = np.maximum(0, blurred * .9 - core)
    level = np.where(halo < 3, 0, np.maximum(1, np.minimum(63, np.floor(halo / 255 * 63 + .5))))
    alpha = np.floor(level * 255 / 63 + .5).astype(np.uint8)
    pixels = np.zeros((h, w, 4), dtype=np.uint8)
    pixels[:, :, :3] = np.where(alpha[:, :, None] > 0, 255, 0)
    pixels[:, :, 3] = alpha
    dest.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(pixels, 'RGBA').save(dest)

for path in (ASSETS / 'icons/first-level').glob('*.png'):
    focus(path, ASSETS / 'icons/first-focus' / path.name)
for path in (ASSETS / 'icons/second-level').glob('*.png'):
    focus(path, ASSETS / 'icons/second-focus' / path.name)

preview = ASSETS / 'preview'
preview.mkdir(parents=True, exist_ok=True)
wallpaper = Image.open(ASSETS / 'wallpaper-480x272.bmp').convert('RGB')
ImageOps.fit(wallpaper, (300,170), Image.Resampling.LANCZOS).save(preview / 'preview.png')
Image.open(ASSETS / 'icons/category/game.png').convert('RGBA').resize((16, 16), Image.Resampling.LANCZOS).save(preview / 'icon.png')
print('Prepared focus artwork and preview images')
