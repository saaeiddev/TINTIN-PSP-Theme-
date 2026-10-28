#!/usr/bin/env python3
"""Create editable, consistent vector category artwork; raster export is separate."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artwork/icons/category'
OUT.mkdir(parents=True, exist_ok=True)
BLUE, RED, CREAM, YELLOW, NAVY = '#3b84ad', '#c9433d', '#f7ebc8', '#e6bd63', '#273c50'

# The objects use only original geometric artwork. The common outline, palette,
# size and baseline are intentional so the set can be edited as ordinary SVG.
icons = {
  'settings': f'''<path fill="{CREAM}" d="M19 38h28l4 5H15z"/><path fill="{BLUE}" d="M20 36h25v3H20z"/><path fill="{YELLOW}" d="M22 33c-3-6-2-12 3-17l4 3c-3 4-3 8 0 11l-2 3z"/><path fill="{BLUE}" d="M27 14l7-6 5 6-7 7z"/><path fill="{CREAM}" d="M34 9l3-3 5 6-3 3z"/><circle fill="{RED}" cx="32" cy="30" r="3"/><path fill="none" d="M37 19c5 2 7 7 7 13M40 32h8"/>''',
  'photo': f'''<path fill="{CREAM}" d="M10 18h44v25H10z"/><path fill="{NAVY}" d="M14 18v-5h11l3 5"/><path fill="{BLUE}" d="M12 23h40v14H12z"/><circle fill="{CREAM}" cx="32" cy="30" r="10"/><circle fill="{NAVY}" cx="32" cy="30" r="6"/><circle fill="{BLUE}" cx="30" cy="28" r="2"/><path fill="{RED}" d="M45 15h5v3h-5z"/>''',
  'music': f'''<path fill="{YELLOW}" d="M30 29c-2-7-10-6-16-10 3-3 5-8 6-13 6 7 12 9 15 14z"/><path fill="{CREAM}" d="M14 19c5 1 9 4 11 7M19 7c0 5 2 9 6 12"/><path fill="none" d="M30 29c1 5 5 6 10 6h4M45 35v-5h4"/><path fill="{RED}" d="M13 37h39v6H13z"/><path fill="{CREAM}" d="M17 43h31l-2 3H19z"/><circle fill="{NAVY}" cx="30" cy="39" r="1"/>''',
  'video': f'''<path fill="{BLUE}" d="M13 23h31v19H13z"/><path fill="{CREAM}" d="M44 27l9-5v20l-9-5z"/><circle fill="{YELLOW}" cx="21" cy="16" r="7"/><circle fill="{CREAM}" cx="37" cy="16" r="7"/><circle fill="{NAVY}" cx="21" cy="16" r="2"/><circle fill="{NAVY}" cx="37" cy="16" r="2"/><path fill="none" d="M19 45h21M29 42v3"/>''',
  'tv': f'''<rect x="10" y="13" width="44" height="29" rx="4" fill="{CREAM}"/><rect x="15" y="17" width="29" height="20" rx="2" fill="{BLUE}"/><path fill="none" d="M24 10l-5-5m13 5l5-5M18 46h29"/><circle fill="{RED}" cx="49" cy="22" r="1.5"/><circle fill="{YELLOW}" cx="49" cy="30" r="1.5"/>''',
  'game': f'''<path fill="{CREAM}" d="M32 4c-7 6-11 17-10 30l10 6 10-6C43 21 39 10 32 4z"/><path fill="{RED}" d="M32 4c-4 4-6 8-8 13h16c-2-5-4-9-8-13zM22 29h10v7l-10-3zM32 20h10v9H32z"/><circle fill="{BLUE}" cx="32" cy="20" r="4"/><path fill="{RED}" d="M22 30l-7 9 7-1zM42 30l7 9-7-1zM28 40l4 7 4-7z"/>''',
  'network': f'''<circle fill="{BLUE}" cx="31" cy="24" r="17"/><path fill="{YELLOW}" d="M18 14l7-4 4 3-3 4 3 4-4 3-3-3-5 1zM35 17l7-3 5 5-3 5-4-1-3 4-4-4zM25 31l5-2 3 3-2 6-4 1z"/><path fill="none" d="M14 36c8 10 22 12 32 4M43 36l3 4-5 3M31 43v3M22 46h18"/>''',
  'extras': f'''<path fill="{YELLOW}" d="M11 23l4-10h34l4 10v20H11z"/><path fill="{CREAM}" d="M11 23h42v20H11z"/><path fill="{BLUE}" d="M15 13h6v30h-6zM43 13h6v30h-6z"/><path fill="none" d="M11 23h42M11 32h42"/><path fill="{RED}" d="M28 28h8v8h-8z"/><circle fill="{NAVY}" cx="32" cy="32" r="1"/>'''
}
for name, body in icons.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="480" viewBox="0 0 64 48"><g stroke="{NAVY}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>\n'''
    (OUT / f'{name}.svg').write_text(svg, encoding='utf-8')
print(f'Wrote {len(icons)} editable SVG masters to {OUT}')
