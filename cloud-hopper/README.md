# Cloud Hopper ☁️🐰

A gentle sky-island platformer for kids ages ~6–11, part of the free,
MIT-licensed **Play & Code** collection. You are a fluffy white bunny hopping
across floating islands, collecting strawberries and bringing 8 baby animals
home to their nests.

## How to run
Double-click `index.html` (any modern browser). No internet needed, ever —
the `lib/` folder contains everything. If you move the game, move the whole
folder together.

## How to play
- Move: ← → (or A/D) · Jump: Space / ↑ / W · Pause: P or Esc
- Or use the three big on-screen buttons (works for touch and mouse)
- Each level hides 3 strawberries: all 3 = 3⭐, two = 2⭐, finishing = 1⭐
- Cloud platforms can be jumped up through; mushrooms give a super bounce;
  prickly bushes just poof you gently back to the last flag; some levels
  are windy (arrow at the top shows the direction)
- Strawberries are hat money — spend them in the 🎩 Hat Shop and wear any
  hat you own

## 🛠️ Game Master Lab
From the Menu (or the Pause overlay), kids can open the Game Master Lab:
sliders for real physics constants (**gravity**, **jumpPower**, **bounciness**,
**fruitValue**), a sky-theme picker that recolors the page and the in-game
sky, three tiny
lesson cards (variables, numbers, loops), and a mini code box that runs safe
one-liners like `jumpPower = 1.5` (a hand-written parser — never `eval`).
Lab values apply live, are clamped to safe ranges, persist in the save, and
"Reset to normal" restores defaults.

## What gets saved (and where)
One browser save under the key `cloudHopperSave1` (localStorage):
`unlocked` (how many levels are open), `stars` (best stars per level),
`wallet` (strawberry currency), `hats` + `hat` (owned / equipped),
`sound`, lifetime `stats` (fruits picked, wins, plays), and `lab`
(Game Master settings). Resetting from Settings erases only this key.
Nothing ever leaves the device.

## Kid-safe summary
100% offline, no ads, no links out, no accounts, no purchases, no loot boxes,
no timers or lives. Failing is gentle: a poof and you're back at the flag.
Replays always re-earn fruit, so nobody is ever punished for playing more.
All art is original (canvas shapes + emoji).

## Tweak difficulty (parents)
Easiest: use the in-game 🛠️ Game Master Lab (no editing needed). To go deeper,
open `index.html` and edit the constants at the top of the script:
- `GRAV` (2200) — lower = floatier jumps
- `RUN` (260), `ACC_G`/`ACC_A`/`FRIC` — speed and responsiveness
- `JUMP_V` (760) — jump height (~3.2 tiles), `JUMP_CUT` — short-hop height
- `MUSH_V` (1120) — mushroom super-jump power
- `COYOTE_T` (0.1) / `JUMP_BUF` (0.12) — forgiveness windows (bigger = kinder)
- `wind` per level in the `LEVELS` list (0 = no wind)

Levels are string tilemaps (one string per row, 14 rows). Legend:
`.` empty · `#` solid grass block · `=` cloud platform (one-way) ·
`F` fruit · `S` start · `C` checkpoint flag · `B` bouncy mushroom ·
`^` spiky bush · `G` goal nest. Keep exactly one `S`, one `G` and three `F`
per level, and make sure every row has the same length.

---
☁️ Play & Code · made with ❤️ for young coders · v1.1
