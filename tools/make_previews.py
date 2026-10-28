#!/usr/bin/env python3
"""Create explicitly simulated XMB previews, not screenshots from a PSP."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'previews'
OUT.mkdir(exist_ok=True)
fontpath = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fsmall = ImageFont.truetype(fontpath, 11)
fbody = ImageFont.truetype(fontpath, 14)
cats = ['settings','photo','music','video','game','network','extras']
views = [
 ('settings', 'Settings', [('22-system-settings','System Settings'),('24-theme-settings','Theme Settings'),('26-date-time','Date & Time Settings')], 1),
 ('game', 'Game', [('08-game-sharing','Game Sharing'),('10-saved-data','Saved Data Utility'),('02-memory-stick','Memory Stick')], 1),
 ('network', 'Network', [('44-internet-radio','Internet Radio'),('48-browser','Internet Browser'),('50-search','Internet Search')], 1),
]
def text(d, xy, value, font, fill=(255,255,255,255)):
    d.text(xy, value, font=font, fill=fill, stroke_width=1, stroke_fill=(34,40,44,210))
def compose(bg, asset, pos, opacity=1):
    img=Image.open(asset).convert('RGBA')
    if opacity<1: img.putalpha(img.getchannel('A').point(lambda a: round(a*opacity)))
    bg.alpha_composite(img,pos)
for selected, label, items, active in views:
    canvas=Image.open(ROOT/'assets/wallpaper-480x272.bmp').convert('RGBA')
    cur=cats.index(selected)
    for i,name in enumerate(cats):
        cx=110+(i-cur)*82
        if -32<=cx<512: compose(canvas,ROOT/f'assets/icons/category/{name}.png',(cx-32,48), 1 if i==cur else .62)
    d=ImageDraw.Draw(canvas)
    box=d.textbbox((0,0),label,font=fsmall,stroke_width=1)
    text(d,(110-(box[2]-box[0])/2,98),label,fsmall)
    for j,(stem,name) in enumerate(items):
        # PTF Studio places earlier rows in a separate upper lane.
        cy=24+(j-active+1)*64 if j<active else 137+(j-active)*64
        if j==active: compose(canvas,ROOT/f'assets/icons/first-focus/{stem}.png',(78,cy-32))
        compose(canvas,ROOT/f'assets/icons/first-level/{stem}.png',(86,cy-24),1 if j==active else .35)
        d=ImageDraw.Draw(canvas)
        text(d,(149,cy-9),name,fbody, (255,255,255,255 if j==active else 130))
    d=ImageDraw.Draw(canvas)
    text(d,(376,6),'10/28  12:00',fsmall)
    canvas.convert('RGB').resize((960,544),Image.Resampling.NEAREST).save(OUT/f'simulated-xmb-{selected}.png')
print('Created three explicitly simulated XMB previews')
