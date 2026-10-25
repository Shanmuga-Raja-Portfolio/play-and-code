# 🐱 Whisker Warriors

A kid-friendly "cats vs dogs" lane-battle game, part of the free, MIT-licensed
**Play & Code** collection. Inspired by the fun of tower-defense lane battlers —
with all the predatory stuff deliberately left out.

## ▶ How to run
Double-click **`index.html`** — it opens in any modern browser (Chrome, Edge, Firefox).

That's it. No install, no account, no internet required (Vue + Tailwind are bundled in `lib/`).

**Copy the whole folder.** If someone copies only `index.html` without the `lib/` folder,
the game shows a friendly "files incomplete" screen instead of breaking.

## 💻 Installing on another computer
Copy this **whole folder** (`whisker-warriors`, including `lib/`) to a USB stick or shared drive,
drop it anywhere on the other computer, and double-click `index.html`.

**Note on saves:** progress (stars, coins, upgrades, Game Master Lab settings) is stored in the
browser's local storage on each computer. Saves live per-browser per-machine — moving the folder
does not move saves. To wipe a save: in-game **Settings → Reset everything**.

## 🛡️ Kid-safe by design (what's intentionally NOT in this game)
- **No ads and no external links** — the game code contains **zero external web addresses**; it cannot load ads, trackers, or anything else from the internet.
- **No purchases, no loot boxes, no gacha** — every upgrade is deterministic; kids always know exactly what they're buying.
- **No energy meters, lives, or wait timers** — quitting and restarting is always free and instant.
- **No daily-login pressure or FOMO mechanics** — nothing nags them to come back.
- **No accounts and no data collection** — nothing is sent anywhere, ever.
- **Gentle content** — cartoon "poof" knock-outs with sparkles, no gore; silly cats-vs-dogs theme.
- **Optional break reminder** — a friendly non-shaming "water break" pop-up after 25 minutes of play (toggle in Settings).

## 🎮 What's in the game
- 12 stages across 3 chapters (Living Room → Backyard → The Moon), each ending with a boss.
- 7 unlockable cat heroes (unlocked by clearing stages — earned, never gambled for).
- Fish economy: fish fill over time; deploy heroes; enemies drop fish when defeated.
- 1–3 star ratings per stage based on how healthy your tower stayed.
- Cat College: spend coins to level up heroes, fish wallet, and tower.
- Speed toggle (1x/2x), pause, keyboard shortcuts (1–7 deploy, P pause), sound effects (synthesized, no files).

## 🛠️ Game Master Lab (the "learn to code" bit)
Open it from the big **🛠️ Game Master** button on the menu (or from the pause screen during a battle).
Kids can:
- **Move sliders** bound to real game constants — `fishRate` (fish fill speed), `heroDmg` (hero power),
  `heroSpeed` (hero walk speed), `foeHp` (dog toughness) — plus a sky-theme picker. Everything applies live.
- **Read tiny lesson cards** about variables, numbers & math, and loops, each tied to one of those constants.
- **Type real code** in the mini code box, e.g. `fishRate = 2` or `foeHp = heroDmg * 2`. It's parsed by a
  small hand-written parser (never `eval`), clamped to safe ranges, and explains mistakes with friendly "Oops —" hints.
- Lab settings are saved inside the normal game save and **Reset to normal** restores defaults.

## 🔧 For parents: tweaking the game
Open `index.html` in any text editor (Notepad works). Inside the main `<script>` you'll find:

- `BREAK_EVERY_MIN` — break reminder cadence (default 25 minutes).
- `CATS` — hero stats (cost, HP, damage...). Lower costs = easier.
- `FOES` — enemy stats. Lower HP/damage = easier.
- `STAGES` — enemy base HP, spawn timing, and coin rewards per stage.
- `LAB_DEFS` — the Game Master Lab sliders (names, min/max ranges).

Change a number, save the file, refresh the browser. Nothing can break permanently —
**Settings → Reset everything** always restores a fresh save.

## 📜 License
MIT — free to copy, share, and remix. See `../LICENSE`.
