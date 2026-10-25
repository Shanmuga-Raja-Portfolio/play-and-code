# Tiny Sprout Farm 🌱

A cozy, zero-pressure gardening game for kids (~ages 6–11). Part of the free,
MIT-licensed **Play & Code** collection — see `../LICENSE` and
`../_shared/GAME_STANDARD.md`.

## How to run
Double-click `index.html` (any modern browser). Keep the `lib/` folder next to it —
Vue and Tailwind are bundled locally, so it works with **no internet at all**. To move
the game to another computer, copy the whole folder (including `lib/`).

## How to play
1. Tap an empty soil square → pick a seed → it sprouts (Grandpa Sprout leaves 2 free carrot seeds on a fresh start).
2. When a droplet 💧 appears, tap the square (or the little 🚿) to water it; un-watered plants wait patiently forever — they **never** wilt.
3. When a plant sparkles and bounces, tap it → harvest goes straight to coins 🪙.
4. Spend coins in the 🛒 Shop on seeds, decorations (gnome, bench, bird bath, butterfly bush, 3 fence paints) and more plots (tap any 🔒 plot on the farm).
5. First harvest of each crop earns a golden ⭐ sticker in the 📖 Seed Album — complete all 6 to unlock the **Golden Watering Can** ✨🚿 (waters every thirsty plant at once).

## 🛠️ Game Master Lab
Reachable from the Menu (big amber button) and from the Pause overlay on the farm.
Kids become the boss of the game:
- **Sliders** bound to real game constants — `growSpeed` (plant growth rate),
  `waterPower` (drinks per watering tap), `coinBonus` (harvest payout multiplier) —
  applied live and saved automatically.
- **Sky theme** picker (Sunny / Sunset / Starry) repaints the whole page background instantly.
- **Lesson cards** introduce variables (with the grow loop), numbers and multiplication using those exact constants.
- A **mini code box** accepts things like `growSpeed = 2` or `coinBonus = waterPower + 1`.
  It uses a tiny hand-written tokenizer/parser (never `eval`), whitelists only the Lab
  variable names, clamps results to the slider ranges, and answers mistakes with
  friendly "Oops —" hints.
- "Reset to normal" restores every Lab value to its default.

## The anti-dark-pattern promise
- Plants grow **only** while the farm screen is open and the tab is visible; progress is
  stored as remaining-seconds per plot. Nothing grows "while you're away", there are no
  notifications, no streaks, no energy, no guilt — leaving is always free.
- Nothing bad ever happens: no withering, no losing coins, no fail states.
- All prices and payouts are deterministic (no randomness in the economy). The only
  randomness is cosmetic confetti/critter timing.

## What gets saved (localStorage key `tinySproutFarmSave1`)
Coins, seed inventory, every plot's crop + growth seconds + waterings done, unlocked
plots, decorations owned, equipped fence color, album stickers, Golden Watering Can,
sound setting, stats (total harvests, total coins earned), and the Game Master Lab
values (`profile.lab`). Settings has a two-step "Reset everything" that clears all of
it. Growth progress is saved automatically every few seconds while things grow, and
whenever the tab is hidden or an action happens.

## Parent knobs (edit in `index.html`)
- Easiest: use the in-game **🛠️ Game Master Lab** (above) — no editing required.
- `CROPS` — seed price, waterings needed, grow seconds, sell price per crop.
- `PLOT_PRICES` — the 16 escalating plot-unlock prices (first 8 plots are free).
- `DECOR` / `FENCES` — decoration names, emojis, prices.
- `LAB_DEFS` — slider names, min/max/step and defaults for the Game Master Lab.
- `START_COINS` / `START_PLOTS` — fresh-start gifts.
- Sound envelopes live in the `Sfx` class; growth speed is just the `grow` numbers.

100% offline · no ads · no external links · no accounts · made with ❤️ for young coders
