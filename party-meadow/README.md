# 🌼 Party Meadow

A cheerful mini-game party pack for young coders — six little games in one
sunny meadow, built for siblings and friends taking turns on the same PC and
chasing each other's best scores. Part of the free, MIT-licensed **Play & Code**
collection.

## How to run
Double-click **`index.html`** (open it in any modern browser). Keep the `lib`
folder next to it — Vue and Tailwind are bundled there, so the game is 100%
offline. No install, no internet, no accounts.

## The six games
| Game | Idea | Controls | Stars |
|---|---|---|---|
| 🐰 Bunny Pops (45s) | tap bunnies popping from 6 burrows; bees cost −2 | tap / click | 15 / 10 / 5 |
| 🦉 Memory Grove | 4×4 card-flip pairs, moves counted | click cards | ≤10 / ≤14 moves |
| 🌸 Flower Song | Simon-style tune on 4 singing flowers | tap flowers | round 10 / 8 / 6 |
| 🍎 Fruit Catch (40s) | basket catches fruit, dodges boots | ← → or A/D or big on-screen buttons | 20 / 14 / 8 |
| 🔍 Odd One Out (8 rounds) | spot the different emoji, grid grows 2×2 → 5×5 | tap | under 20 / 30 / 45 s |
| 🎈 Balloon Pop (30s) | pop floating balloons; golden = +3 | tap / click | 18 / 12 / 7 |

Any finished game always earns at least ⭐ (gentle by design). Every game can be
paused with **P / Esc** (or the ⏸️ button).

## 🛠️ Game Master Lab
The Lab (big purple button on the Menu, also in every Pause overlay) turns kids
into game masters. It has:
- **4 live sliders** bound to real code constants: `bunnyPace` (how fast bunnies
  pop out), `fruitSpeed` (basket sliding speed), `balloonPace` (how many
  balloons float by) and `songTempo` (how fast the flowers sing). Changes apply
  instantly and persist between visits.
- **3 meadow themes** (Sunny / Sunset / Starry) that repaint the whole page.
- **Lesson cards** (ages 6–11) explaining variables, numbers, loops and timing
  using those exact constants.
- **A mini code box** where kids can type real assignments like
  `bunnyPace = 2` or `fruitSpeed = 1 + 1`. A tiny built-in parser checks the
  math (never `eval`), keeps values in a safe range, and explains anything
  that goes wrong in friendly words.
- **Reset to normal** restores all defaults.

## What gets saved
One browser-save in `localStorage`, key **`partyMeadowSave1`**:
- `sound` — sound on/off
- `plays` — total games played
- `best` — per game: best score (moves for Memory, seconds for Odd One Out,
  round for Flower Song) and best stars
- `lab` — Game Master Lab slider values and theme

"Meadow Stars" on the Family Scores screen is simply the sum of all best stars
(max 18). Reset everything via Settings → *Reset everything* (two taps).

## Kid-safe summary
No ads, external links, purchases, loot boxes, gambling-style randomness,
energy/lives or wait timers. Nothing bad happens when a child stops playing.
All art is emoji + canvas + CSS; all names are original; fail states are gentle
("Good try!") with instant replay. The only text input anywhere is the Lab's
mini code box, which is parsed, never executed.

## Difficulty knobs
**Parents:** the easiest way to tune difficulty is the in-game **Game Master
Lab** — no code editing needed, and kids can do it themselves. For deeper
tweaks, edit `index.html`:
- `starsFor()` — star thresholds per game
- `BunnyEngine` / `FruitEngine` / `BalloonEngine` constructors — round length
  (`total`), spawn speed, bee/boot/golden chance
- `MEM_POOL`, `ODD_GRIDS`, `ODD_PAIRS` — memory animals and odd-one boards
- `FLOWERS` — the four flower tones (C4 E4 G4 C5) and names
- `SONG_MAX_ROUND` — Flower Song victory cap (12)
- `LAB_DEFS` — the Lab sliders' ranges, steps and labels
