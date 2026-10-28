# TINTIN PSP Theme

An independent fan-made standard PSP PTF theme by **Amir Saeid Dehghan**, inspired by Tintin, Snowy and classic European adventure comics. A map wallpaper is joined by custom category, first- and second-level icons and focus artwork. This is not an official or licensed release.

**Status:** compiled and software-validated; installation and appearance have **not** been tested on physical PSP hardware or an emulator. Treat this as a candidate build, especially on PSP Go. See [testing](docs/TESTING.md).

- [Download the PTF](release/TINTIN_PSP_Theme.ptf) · [فارسی](README_FA.md) · [Checksum](release/SHA256SUMS.txt)
- [Simulated Settings preview](previews/simulated-xmb-settings.png) · [Game preview](previews/simulated-xmb-game.png) · [Network preview](previews/simulated-xmb-network.png)

These previews are layout illustrations with a substitute font: **they are not screenshots from a PSP or emulator**. The wallpaper master is AI-generated raster art, not a frame from the television series; icon masters are editable SVG. The illustrations have not been authenticated against production artwork.

## Installation

1. Download `TINTIN_PSP_Theme.ptf`. No development tools or custom firmware are needed for standard PTF themes.
2. Connect the PSP in USB mode or mount its Memory Stick. At the **root** of the chosen storage, create `PSP/THEME` if needed; copy the `.ptf` there.
3. Safely eject and disconnect. Open **Settings → Theme Settings → Theme**, select **TINTIN PSP Theme**, then choose **Apply**.
4. If an unrelated wallpaper remains visible, choose **Settings → Theme Settings → Background → Custom Theme**.
5. To restore the default, return to **Settings → Theme Settings → Theme** and choose **Original**.

### PSP Go

Choose internal system storage as the USB device in System Settings, connect by USB, and copy the PTF to `PSP/THEME` at the root of internal storage (often called `ef0:/PSP/THEME` in technical tools). Alternatively use the same path on an M2 card. Then select it under **Settings → Theme Settings → Theme**. The PSP may prompt before replacing the custom theme held in system memory. [Sony's instructions](https://manuals.playstation.net/document/en/psp/current/settings/theme.html) describe both storage locations.

## Models and limitations

Designed for PSP-1000, 2000, 3000, Go (N1000) and Street (E1000), using standard PTF rather than CTF. None has been physically tested. Firmware versions and model-specific menus differ. PTF Studio's universal schema uses a fallback first-level graphic for Go-specific storage and resume entries rather than invented PTF slots. The build uses the tool's 48×48 first-level bodies and 64×64 focus assets; Sony's older converter guidance describes 32×32 and 48×48 input artwork, so actual firmware behavior needs device verification. Standard PTF cannot replace firmware layouts, fonts, system functions or wave animation.

## Rebuild

The exported image assets are checked in. The build uses Node.js 20+ (with `CompressionStream`), the `pngjs` package, and the PTF Studio 1.0 source at commit `3b2c6407201bf02a22412725c9009a52bbdf1517`. PTF Studio is GPL-3.0; see its [source and license](https://github.com/S1implyBlue/PTF-Studio/tree/3b2c6407201bf02a22412725c9009a52bbdf1517). Obtain the source and install `pngjs` in a local development environment (`npm install pngjs` in this project directory), then:

```sh
PTF_STUDIO_DIR=/path/to/PTF-Studio node tools/build_ptf.cjs
python3 tools/verify_ptf.py
sha256sum release/TINTIN_PSP_Theme.ptf
```

To regenerate focus images and previews from checked-in PNGs, run `python3 tools/prepare_assets.py` and `python3 tools/make_previews.py` with Pillow and NumPy installed. `tools/create_category_icons.py` and `tools/create_first_level_icons.py` regenerate editable SVG masters; raster export uses Sharp. PTF Studio embeds a build timestamp, so independently rebuilt binary checksums may differ. The release checksum identifies the checked-in binary.

## Credits and rights

Concept and project credit: Amir Saeid Dehghan. Wallpaper master generated with OpenAI image generation; original vector icons and build integration prepared for this project. PTF encoding and decoding use PTF Studio 1.0. PSP installation guidance: [Sony PSP manual](https://manuals.playstation.net/document/en/psp/current/settings/theme.html). Tintin, Snowy and related visual elements belong to their respective rights holders. This fan work is unaffiliated; authorization to distribute derivative artwork has not been established. See [credits](docs/CREDITS.md).
