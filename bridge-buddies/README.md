# Bridge Buddies 🌉

A cozy bridge-building puzzle game for young coders (ages ~6–11). Snap wooden
planks between smiling steel bolts, then send a buddy animal across the canyon
to the flag. 12 levels with a gentle difficulty ramp, plus a free-build Sandbox.
Part of the free, MIT-licensed "Play & Code" collection.

## How to run
Double-click `index.html` (any modern browser). No internet needed — Vue and
Tailwind are bundled in the `lib/` folder. Copy the WHOLE folder if you move it.

## How to play
1. Tap one bolt, then tap another bolt nearby — a plank snaps in (dashed line
   shows your reach). Tap a plank to take it back; 🧹 Clear all resets.
2. Press "▶ Go buddy!" — the level's buddy (🦔 strolls, 🦆 waddles, 🐸 hops)
   follows your bridge. If the path stops short, they shrug, show a friendly
   "Need more bridge!" bubble and walk back so you can rebuild — no penalty.
3. Reach the flag for fireworks and stars: 3⭐ = par planks or fewer,
   2⭐ = par+1, 1⭐ = any solution. From level 5, gold-banded LONG planks
   reach extra far. Rock pillar tops are free walking.

## 🛠️ Game Master Lab (kids become game masters!)
The big "🛠️ Game Master" button on the Menu (and in the Pause overlay) opens the
Lab, where kids tune the game's real code with live sliders and a tiny safe
code box (`plankReach = 1.2` really works — no eval, hand-parsed only):
- **Plank Length** (`plankReach`, ×0.5–×1.5) — how long planks can stretch
- **Buddy Speed** (`buddySpeed`, ×0.5–×2) — how fast buddies walk
- **Bridge Droop** (`bridgeSag`, ×0–×2) — how much planks dip mid-span
- **Hop Power** (`hopPower`, ×0.5–×2) — how bouncy the frog's hops are
- A 3-theme page recolor (Sunny / Sunset / Starry) and short lesson cards that
  name the constants. "Reset to normal" restores defaults.

## What gets saved
One browser-storage key: `bridgeBuddiesSave1` — stars per level, highest
unlocked level, sandbox unlocked, sound on/off, bridges-built counter, plus
all Game Master Lab values. Settings → "Reset everything" (two-tap confirm)
erases it all.

## Kid-safe summary
100% offline, zero external URLs, no ads/links/purchases/accounts, no timers
or punishment. Buddies never get hurt: they follow the plank path (no physics
engine — wobble is just pretty), and a defensive lily-pad catch makes any
glitch a cute splash-and-paddle-back. All art is emoji + canvas shapes.

## Tweak difficulty
Parents: try the **Game Master Lab first** — the sliders above change the same
constants the code uses, live. For permanent changes, edit in `index.html`:
- `REACH` (170) — max span of a normal plank.
- `LONG_REACH` (240) — max span of a long plank.
- `LEVELS` — per level: `shorts`/`longs` (plank inventory, -1 = infinite),
  `par` (planks for 3⭐), pillar/bolt positions.
- `BUDDIES` — walking speeds and styles.

Levels unlock in order; finishing level 12 unlocks the Sandbox (level 13).
