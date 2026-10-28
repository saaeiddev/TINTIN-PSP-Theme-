# Validation and compatibility report

Build: candidate 1.0, 2026-10-28. PTF Studio source: `3b2c6407201bf02a22412725c9009a52bbdf1517` (1.0). The PTF is 466,908 bytes, under the tool's 768 KiB preflight limit. SHA-256 is in `release/SHA256SUMS.txt`.

## Performed

- Built with PTF Studio's own `buildPtf`, image encoders and focus encoder, invoked from `tools/build_ptf.cjs` using the checked-in source PNGs.
- Reopened the compiled bytes using PTF Studio's `parsePtf` and GIM decoder. The tool decoded and checked dimensions of all 72 GIM image resources. Wallpaper was verified as a BMP record separately; the Node environment does not have the browser's BMP canvas decoder.
- Ran an independent Python structural verifier: PTF signature and version, headers, bounded offsets, metadata, 74 records including the color record, zlib payloads, resource counts, GIM format and declared dimensions, indexed palettes, and 480×272 24-bit BMP dimensions. This is a container check, not an independent PSP firmware implementation.
- Opened 70 PNG icon and focus exports with Pillow and verified dimensions, visible and transparent pixels, white-only focus RGB, and at most 64 focus alpha levels; checked the RGB wallpaper export. Verified the SHA-256 checksum.
- Created three labeled, simulated XMB previews with a substitute font. These are not hardware captures or emulator screenshots. The previews are approximate and not a pixel-accurate representation of the original interface.

## Not performed

- No physical PSP, including PSP Go, or emulator was available. Installation, menu rendering, model and firmware compatibility, icon clipping, text legibility and performance on a device remain unverified.
- No Sony converter import test was performed. Older Sony input-size guidance differs from the PTF Studio 1.0 presets. A software round trip in one tool and structural checks do not establish that every PSP firmware accepts the resulting file.
- PSP Go's system storage, saved data on system storage, and resume entries rely on PTF Studio's documented fallback rather than dedicated first-level records. Actual fallback behavior needs a physical test.
- The source artwork is original/generated fan interpretation. It was not compared with licensed production model sheets, and redistribution rights for derivative artwork have not been established.

## Checks to repeat

```
python3 tools/verify_assets.py
python3 tools/verify_ptf.py
sha256sum -c release/SHA256SUMS.txt
```

Test by copying the file to the selected storage's `PSP/THEME` folder and selecting it under Settings → Theme Settings → Theme. Record device model, firmware, whether the theme appears and applies, wallpaper appearance, category and first-level icons, selected glows, text visibility, and PSP Go storage/resume fallback behavior. To restore, select Original in the Theme menu.
