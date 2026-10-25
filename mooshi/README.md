# Mooshi 🐮 — the anti-tamagotchi

A virtual pet with **zero guilt mechanics** for kids ages ~6–11, part of the free,
MIT-licensed **Play & Code** collection. Mooshi is a round pastel blob-cow who is
*never* sad, sick, hungry-looking or punished.

## How to run
Double-click `index.html` (any modern browser). No internet needed, ever —
the `lib/` folder contains everything. If you move the game, move the whole
folder together.

## What makes it guilt-free
- **Friendship only ever goes UP.** It never decays, never resets on its own.
- **Absence is never punished.** Nothing decays while the game is closed. Away for a while?
  Mooshi simply "napped happily waiting for you".
- **Fullness is not hunger.** It only means "would enjoy a snack 🍎" vs "full and happy 💤".
  A full Mooshi politely declines a snack — no penalty, no sad text. Fullness drifts down
  by 1 point per ~40 s *only while the tab is open*, and never below 0.
- No ads, no links out, no accounts, no purchases, no loot boxes, no streaks, no timers.
- All sounds are soft oscillator tones; nothing startling. Sound can be turned off.

## Things to do
- Poke Mooshi (click) — happy boing + heart. Eyes follow the pointer; Space works too.
- 🍎 **Feed** — 6 snacks; Mooshi waddles to the bowl and munches (3 chomps + crumbs).
- 🎾 **Play** — bouncy ball (click it; Mooshi watches and hops), tickle (wiggle pointer fast
  over Mooshi), and a nap toggle (Zzz → wake with a big stretch + yawn).
- 🫧 **Clean** — ~6 s of soap bubbles; click bubbles to pop; ends sparkly-clean.
- 🎀 **Dress-up** — hats + extras drawn on canvas, unlocked in a **fixed order** by
  Friendship Level: 2 party hat, 3 bow tie, 4 flower, 5 glasses, 6 scarf, 7 beanie, 8 crown.
- The window sky matches the real local time of day (decorative only).
- P or Esc pauses; the animation loop stops when the tab is hidden.

## 🛠️ Game Master Lab
From the Menu (or the Pause overlay), kids can open the Game Master Lab:
sliders for real game constants (**snackTimer** — how slowly the tummy empties,
**boing** — poke & ball hop strength, **friendXp** — how fast friendship grows,
**wiggle** — breathing / ear / tail animation speed), a page-theme picker that
recolors the whole page live, three tiny lesson cards (variables, timers & loops,
conditions), and a mini code box that runs safe one-liners like `boing = 2`
(a hand-written parser — never `eval`). Lab values apply live, are clamped to
safe ranges, persist in the save, and "Reset to normal" restores defaults.

## What gets saved (and where)
One browser save under the key `mooshiSave1` (localStorage): friendship XP,
fullness, unlocked cosmetics, equipped hat + accessory, naps / pokes / feeds
counts, sound setting, a `lastSeen` timestamp (used only for the friendly
welcome-back bubble after more than ~4 hours away), and `lab` (Game Master
settings). Resetting from Settings erases only this key.
Nothing ever leaves the device.

## Kid-safe summary
100% offline, no ads, no links out, no accounts, no purchases, no loot boxes,
no timers or lives. Friendship never goes down and absence is never punished.
All art is original (canvas shapes + emoji).

## Tweak difficulty (parents)
Easiest: use the in-game 🛠️ Game Master Lab (no editing needed). To go deeper,
open `index.html` and edit the constants at the top of the script:
- `LEVEL_STEP` (25) — level N needs about N×25 XP total.
- `XP` / `XP_CD` — XP per action and its gentle cooldown in seconds.
- `FOODS` — snacks and how much fullness each restores (`yum`).
- `FULLNESS_DECAY_S` (40) — base seconds of open-tab time per 1 fullness point
  (the Lab's `snackTimer` multiplies this).
- `CLEAN_TIME` (6) — seconds of bubble rain.
- `WELCOME_AWAY_MS` — away-time threshold for the welcome-back bubble.

---
🐮 Play & Code · made with ❤️ for young coders · v1.1
