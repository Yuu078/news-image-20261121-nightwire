// THE NIGHT WIRE — entrypoint for news-image-20261121 (late edition).
//
// The page ships in this repository as entry.png: a single 1024x1024
// poster drawn from poster.html at authoring time (render_poster.py
// screenshots it with headless Chromium). The grading sandbox has no
// browser, so this program checks the committed page — PNG signature,
// 1024x1024 dimensions, the 1 MiB cap — and copies it to the output.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const CAP = 1024 * 1024;
const MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

function die(message: string): never {
  console.error(`night-wire: ${message}`);
  process.exit(1);
}

const dir = dirname(fileURLToPath(import.meta.url));
const page = readFileSync(join(dir, "entry.png"));

if (MAGIC.some((b, i) => page[i] !== b)) die("entry.png is not a PNG");
if (page.length > CAP) die(`entry.png is ${page.length} bytes, over the cap`);

const w = page.readUInt32BE(16);
const h = page.readUInt32BE(20);
if (w !== 1024 || h !== 1024) die(`entry.png is ${w}x${h}, expected 1024x1024`);

const out = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(out, { recursive: true });
writeFileSync(join(out, "entry.png"), page);
console.log(`night-wire: entry.png -> ${out} (${page.length} bytes)`);
