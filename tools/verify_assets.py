#!/usr/bin/env python3
"""Check source exports and the transparency invariants of focus artwork."""
from pathlib import Path
from PIL import Image
root = Path(__file__).resolve().parents[1] / 'assets'
specs = {'category':(8,(64,48)), 'first-level':(29,(48,48)), 'first-focus':(29,(64,64)), 'second-level':(2,(32,32)), 'second-focus':(2,(48,48))}
for name,(count,size) in specs.items():
    files=sorted((root/'icons'/name).glob('*.png'))
    assert len(files)==count,(name,len(files))
    for file in files:
        with Image.open(file) as source:
            source.load()
            assert source.size==size,(file,source.size)
            pixels=list(source.convert('RGBA').getdata())
        assert any(p[3]==0 for p in pixels) and any(p[3]>0 for p in pixels),file
        if 'focus' in name:
            assert all((p[0:3] == (255,255,255) if p[3] else p[0:3] == (0,0,0)) for p in pixels),file
            assert len(set(p[3] for p in pixels))<=64,file
        else:
            assert any(p[3]==255 for p in pixels),file
    print(f'PASS {name}: {count} readable, correctly sized RGBA images')
wall=Image.open(root/'wallpaper-480x272.bmp'); assert wall.size==(480,272) and wall.mode=='RGB'
print('PASS wallpaper: 480×272 RGB BMP')
