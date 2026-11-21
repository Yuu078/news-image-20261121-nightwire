"""Screenshot poster.html into entry.png (headless Chromium, Playwright).

The sheet is designed at 1024x1024. We capture it in a taller window so
this Chromium build does not clip the last rows, crop the top square,
and verify size and byte caps before writing the preview.
"""

import glob
import os
import subprocess

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def find_browser():
    cache = os.path.expanduser("~/.cache/ms-playwright")
    hits = sorted(
        glob.glob(os.path.join(cache, "chromium-*", "chrome-linux*", "chrome")),
        reverse=True,
    )
    if not hits:
        raise SystemExit("no playwright chromium found")
    return hits[0]


def main():
    raw = os.path.join(HERE, ".shot.png")
    subprocess.run(
        [
            find_browser(), "--headless=new", "--no-sandbox", "--disable-gpu",
            "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=1024,1350", "--screenshot=" + raw,
            "file://" + os.path.join(HERE, "poster.html"),
        ],
        check=True,
        capture_output=True,
    )
    img = Image.open(raw).crop((0, 0, 1024, 1024))
    img.save(os.path.join(HERE, "entry.png"))
    img.resize((512, 512)).save(os.path.join(HERE, "entry-512.png"))
    os.remove(raw)
    size = os.path.getsize(os.path.join(HERE, "entry.png"))
    print(f"entry.png {img.size[0]}x{img.size[1]} {size} bytes")
    assert img.size == (1024, 1024) and size <= 1_048_576


if __name__ == "__main__":
    main()
