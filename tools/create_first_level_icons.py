#!/usr/bin/env python3
"""Create PSP first-level icon masters from original editable vector shapes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artwork/icons/first-level'
OUT.mkdir(parents=True, exist_ok=True)
B, R, C, Y, N = '#3b84ad', '#c9433d', '#f7ebc8', '#e6bd63', '#273c50'

# 48-unit canvases; semantic symbols intentionally remain readable at PSP size.
shapes = {
'archive': f'<path fill="{Y}" d="M11 10h26v30H11z"/><path fill="{C}" d="M15 14h18v22H15z"/><path fill="none" d="M19 20h10m-10 5h10m-10 5h7"/>',
'disc': f'<circle fill="{C}" cx="24" cy="24" r="17"/><circle fill="{B}" cx="24" cy="24" r="11"/><circle fill="{Y}" cx="24" cy="24" r="3"/>',
'camera': f'<path fill="{C}" d="M7 17h34v23H7z"/><path fill="{N}" d="M12 13h10l3 4H12z"/><path fill="{B}" d="M8 22h32v12H8z"/><circle fill="{C}" cx="24" cy="28" r="8"/><circle fill="{N}" cx="24" cy="28" r="4"/>',
'sharing': f'<path fill="{Y}" d="M12 12h24v24H12z"/><circle fill="{B}" cx="16" cy="18" r="3"/><circle fill="{R}" cx="32" cy="16" r="3"/><circle fill="{C}" cx="30" cy="31" r="3"/><path fill="none" d="M19 18l10-2M17 21l11 9M32 19l-2 9"/>',
'save': f'<path fill="{B}" d="M10 7h25l4 5v29H10z"/><path fill="{C}" d="M16 8h16v10H16zM15 27h19v14H15z"/><path fill="none" d="M20 31h9m-9 4h9"/>',
'update': f'<circle fill="{C}" cx="24" cy="24" r="16"/><path fill="{B}" d="M24 12v18m-7-7l7 7 7-7"/><path fill="none" d="M16 34h16"/>',
'usb': f'<path fill="none" d="M24 37V12m0 0l-4 5m4-5l4 5M24 28l-8-6v-5M24 23l8-6v-4"/><circle fill="{R}" cx="16" cy="15" r="3"/><path fill="{B}" d="M29 9h6v6h-6z"/><circle fill="{Y}" cx="24" cy="39" r="3"/>',
'film': f'<path fill="{B}" d="M8 17h25v21H8z"/><path fill="{C}" d="M33 21l8-5v20l-8-5z"/><circle fill="{Y}" cx="14" cy="12" r="5"/><circle fill="{C}" cx="27" cy="12" r="5"/>',
'gears': f'<circle fill="{C}" cx="23" cy="24" r="15"/><circle fill="{B}" cx="23" cy="24" r="6"/><path fill="none" stroke-width="4" d="M23 5v5m0 28v5M4 24h5m28 0h5M10 11l4 4m19 19l4 4M10 37l4-4m19-19l4-4"/>',
'theme': f'<path fill="{C}" d="M9 9h30v30H9z"/><path fill="{B}" d="M12 27l7-8 6 6 4-5 7 8v8H12z"/><circle fill="{Y}" cx="30" cy="15" r="3"/><path fill="none" d="M12 13h8"/>',
'clock': f'<circle fill="{C}" cx="24" cy="24" r="17"/><circle fill="{B}" cx="24" cy="24" r="2"/><path fill="none" d="M24 11v13l9 5M24 8v3M40 24h-3M24 40v-3M8 24h3"/>',
'power': f'<path fill="{C}" d="M14 8h20v32H14z"/><path fill="{Y}" d="M18 12h12v24H18z"/><path fill="{R}" d="M26 14l-7 11h5l-2 9 8-13h-5z"/>',
'display': f'<rect fill="{B}" x="7" y="10" width="34" height="24" rx="3"/><path fill="{C}" d="M11 14h26v16H11z"/><path fill="none" d="M24 34v6m-9 0h18"/>',
'sound': f'<path fill="{Y}" d="M9 20h7l9-8v24l-9-8H9z"/><path fill="none" d="M30 18c4 3 4 9 0 12m4-16c7 5 7 15 0 20"/>',
'lock': f'<path fill="none" stroke-width="4" d="M16 21v-5a8 8 0 0116 0v5"/><rect fill="{Y}" x="11" y="21" width="26" height="20" rx="3"/><circle fill="{N}" cx="24" cy="29" r="2"/><path fill="none" d="M24 31v4"/>',
'rss': f'<path fill="{R}" d="M8 9h32v31H8z"/><circle fill="{C}" cx="15" cy="33" r="2"/><path fill="none" stroke="{C}" stroke-width="3" d="M14 23c7 0 10 4 10 10M14 16c11 0 17 6 17 17"/>',
'globe': f'<circle fill="{B}" cx="24" cy="23" r="16"/><path fill="{Y}" d="M12 14l7-5 4 3-2 5 3 4-4 3-4-3-5 1zM27 16l6-3 5 5-4 5-4-1-3 5-4-5zM18 30l5-2 3 3-2 6-4 1z"/><path fill="none" d="M13 38h22"/>',
'book': f'<path fill="{C}" d="M7 12c8-3 13-2 17 2 4-4 9-5 17-2v26c-8-3-13-2-17 2-4-4-9-5-17-2z"/><path fill="none" d="M24 14v26M11 18c4-1 7 0 10 1m6 0c3-2 6-2 10-1M11 24c4-1 7 0 10 1m6 0c3-2 6-2 10-1"/>',
'remote': f'<rect fill="{B}" x="7" y="14" width="34" height="22" rx="6"/><path fill="{C}" d="M12 21h10v10H12z"/><path fill="none" d="M17 23v6m-3-3h6"/><circle fill="{R}" cx="32" cy="23" r="2"/><circle fill="{Y}" cx="35" cy="29" r="2"/>',
'radio': f'<path fill="{C}" d="M9 17h30v22H9z"/><path fill="none" d="M13 17l17-9M29 22h6m-6 5h6m-6 5h6"/><circle fill="{B}" cx="19" cy="28" r="7"/><circle fill="{N}" cx="19" cy="28" r="2"/>',
'search': f'<circle fill="{C}" cx="21" cy="21" r="12"/><path fill="{B}" d="M29 29l11 9-3 3-9-11z"/><path fill="none" d="M16 18c1-3 3-4 6-4"/>',
'account': f'<circle fill="{C}" cx="24" cy="17" r="8"/><path fill="{B}" d="M10 39c1-9 6-13 14-13s13 4 14 13z"/><path fill="none" d="M16 39v-4m16 4v-4"/>',
'compass': f'<circle fill="{C}" cx="24" cy="24" r="17"/><circle fill="{B}" cx="24" cy="24" r="12"/><path fill="{R}" d="M29 16l-2 11-8 5 2-11z"/><circle fill="{Y}" cx="24" cy="24" r="2"/>',
'bluetooth': f'<path fill="{B}" d="M24 7l9 9-9 8 9 8-9 9V7z"/><path fill="none" stroke="{C}" stroke-width="2.5" d="M17 16l15 16-8 8V8l8 8-15 16"/>',
'notes': f'<path fill="{C}" d="M9 10h30v28H9z"/><path fill="none" d="M14 17h20m-20 5h20m-20 5h20m-20 5h20"/><path fill="{B}" d="M26 13v15c-5-2-7 5-2 5 3 0 4-2 4-5V17l6-2v9c-5-2-7 5-2 5 3 0 4-2 4-5V11z"/>'
}
# Actual PTF slot numbers stop at 59; Go-only system-storage entries use fallback.
slots = {2:('memory-stick','archive'),4:('umd','disc'),6:('camera','camera'),8:('game-sharing','sharing'),10:('saved-data','save'),12:('umd-update','update'),14:('network-update','update'),16:('usb','usb'),18:('video-settings','film'),20:('photo-settings','camera'),22:('system-settings','gears'),24:('theme-settings','theme'),26:('date-time','clock'),28:('power-save','power'),30:('external-display','display'),32:('sound','sound'),34:('security','lock'),36:('rss-settings','rss'),38:('network-settings','globe'),40:('manual','book'),42:('remote-play','remote'),44:('internet-radio','radio'),46:('rss','rss'),48:('browser','globe'),50:('search','search'),52:('account','account'),54:('fallback','compass'),56:('bluetooth','bluetooth'),58:('sensme','notes')}
for slot, (name, key) in slots.items():
    body = shapes[key]
    # A small badge differentiates same-object settings from the corresponding app.
    if name.endswith('-settings'):
        body += f'<circle cx="37" cy="36" r="7" fill="{C}"/><circle cx="37" cy="36" r="3" fill="{Y}"/>'
    if name == 'network-update':
        body += f'<circle cx="37" cy="36" r="7" fill="{B}"/><path fill="none" stroke="{C}" d="M31 36h12m-6-6c-3 4-3 8 0 12m0-12c3 4 3 8 0 12"/>'
    if name == 'umd-update':
        body += f'<circle cx="37" cy="36" r="7" fill="{C}"/><circle cx="37" cy="36" r="3" fill="{B}"/>'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="480" viewBox="0 0 48 48"><g stroke="{N}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>\n'
    (OUT / f'{slot:02d}-{name}.svg').write_text(svg, encoding='utf-8')
print(f'Wrote {len(slots)} editable first-level SVG masters')
