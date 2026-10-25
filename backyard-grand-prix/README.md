# Backyard Grand Prix 🏁 — parent notes

A cute top-down kart racing game for the family collection. Tiny animal karts
(🐱🐶🐰🐼) zoom around a big pastel backyard on 3 dirt tracks, with boost pads,
skid marks, birds, and gentle AI rivals that always finish their laps.

Part of the free, MIT-licensed **Play & Code** collection — every game is a
single folder, 100% offline, with a 🛠️ Game Master Lab where kids tune the
real code.

## How to run
Double-click `index.html` (open the **whole folder** — the `lib/` folder with
Vue + Tailwind must sit next to it). Works fully offline in any modern browser,
desktop or tablet. Nothing is installed, nothing is sent anywhere.

## How to play
- **↑ / W / Space** = gas, **↓ / S** = brake or reverse, **← → / A D** = steer.
- On a tablet there are big on-screen buttons (steer left/right, gas, brake).
- **P** or **Esc** = pause. Race 3 laps; finish 1st to unlock the next track
  and a new kart color. Stars: 1st = 3⭐, 2nd = 2⭐, 3rd/4th = 1⭐ (always friendly).

## 🛠️ Game Master Lab
From the menu (or the pause screen mid-race), kids become the race engineer:
- **4 sliders** bound to the real physics constants — **MAXS** (top speed),
  **ACC** (acceleration), **STEER** (turn rate), **GRASS** (how much speed the
  grass lets you keep). Every change applies **live**, even mid-race.
- **3 backyard themes** (Sunny Day / Sunset / Starry Night) that recolor the
  whole page.
- **3 lesson cards** (variables, loops, conditions) written for ages 6–11, each
  naming the exact constant it demos.
- A **mini code box** where kids type real assignments like `MAXS = 300` or
  `STEER = 1 + 1`. A tiny hand-written parser (no `eval`, ever) checks the
  math, keeps values inside safe ranges with friendly messages, and snaps
  off-step numbers to the dial's grid.
- **Reset to normal** restores the defaults. Lab settings are saved alongside
  everything else.

## Tweak difficulty
Start with the **Game Master Lab** — it's the kid-friendly front end for the
constants below. Parents who want to edit `index.html` (top of the main script)
can go further:
- `PH.MAXS / ACC / BRK / STEER` — kart physics (speed, acceleration, braking, turn rate).
- `PH.GRASS` — how slow grass makes you (0.44 = 44% of top speed).
- `AI_SPEEDS` — the three AI racers' base speed as a fraction of top speed
  (lower = easier, e.g. `[0.80, 0.76, 0.72]`).
- Rubber-banding strength is in `Race.aiInput` (`±0.12` behind / `-0.20` ahead).
- `LAP_COUNT` — laps per race (default 3).
- `TRACK_DEFS` — the hand-tuned centerline points, widths and themes per track.

## Kid-safe summary
- No ads, no external links, no accounts, no purchases, no loot boxes, no
  timers or streaks. 100% offline (zero network requests).
- No fail states or punishment: grass only slows you (you can never get stuck),
  every finish gets stars and a happy line, instant retry anytime.
- All characters and art are original (emoji + canvas shapes).

## What gets saved (localStorage key `backyardGrandPrixSave1`)
Racer choice, kart color, unlocked track count, stars + best time per track,
tracks won, sound on/off, races played, races won — plus all Game Master Lab
values (sliders + theme). "Reset everything" in Settings erases it all
(two-tap confirm).

v1.1 · Play & Code · made with ❤️ for young coders
