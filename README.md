[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Yuu078/news-image-20261121-nightwire/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Yuu078/news-image-20261121-nightwire/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The Night Wire — news-image-20261121 (late edition)

The dark-edition front page for **Saturday 21 November 2026**: 35 stories
across 7 regions, led by the AI selloff that sank the S&P 500 into
correction and rolled through Asia, with the war in Europe, the strikes
in Yemen and the COP31 endgame inside.

## Layout

- `poster.html` — the page itself (1024x1024): masthead, a markets lead
  with a week-in-numbers box, a numbers strip, and seven labelled
  region sections on a night-black sheet.
- `render_poster.py` — screenshots `poster.html` with headless Chromium
  into `entry.png` and checks the competition caps.
- `stories.md` — headline, region, source and summary for every story.
- `main.ts` — the entrypoint: verifies the committed `entry.png`
  (signature, dimensions, size cap) and copies it to the output.
- `entry-512.png` — half-size legibility preview.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Sources

Reuters, AP, BBC, UN News, Al Jazeera, CNBC and the outlets named per
story in `stories.md`. All stories are from the 21 November 2026 cycle.
