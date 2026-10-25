# Play & Code — a collection of 9 tiny games for young coders

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Guard & Deploy](https://github.com/Shanmuga-Raja-Portfolio/play-and-code/actions/workflows/ci.yml/badge.svg)](https://github.com/Shanmuga-Raja-Portfolio/play-and-code/actions/workflows/ci.yml)
[![Live site](https://img.shields.io/badge/play%20online-GitHub%20Pages-brightgreen)](https://shanmuga-raja-portfolio.github.io/play-and-code/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

**[▶ Play online](https://shanmuga-raja-portfolio.github.io/play-and-code/)** ·
**[👪 For parents](https://shanmuga-raja-portfolio.github.io/play-and-code/parents.html)** ·
or keep reading and run it offline — both are first-class.

Nine single-file web games for kids roughly ages 6–11. Each one is built to be
**opened by double-clicking `index.html`** — no install, no internet, no accounts,
no ads. Every game is also a quiet programming lesson: behind the cute surface,
real variables do real work, and the new **Game Master Lab** lets kids touch them.

```
play-and-code/
├── index.html           ← the collection's landing page (start here)
├── parents.html         ← the grown-ups' overview
├── README.md            ← this file
├── LICENSE              ← MIT
├── _shared/
│   └── GAME_STANDARD.md      the rules every game follows
├── whisker-warriors/    cat vs. critters arcade
├── cloud-hopper/        bouncy platform hopping
├── tiny-sprout-farm/    gentle growing & watering
├── magic-doodle/        draw, color, and stamp
├── mooshi/              a virtual pet cow
├── backyard-grand-prix/ little kart racing
├── bridge-buddies/      build bridges for frog buddies
├── party-meadow/        three mini party games
├── paw-chess/           friendly chess with animal pals
├── tools/               the CI guard (check_games.py)
└── .github/             workflows, issue & PR templates, policies
```

Each game folder holds exactly three things: `index.html` (the whole game),
`README.md` (notes for parents), and `lib/` (the Vue and Tailwind libraries the
game loads from disk). Keep those three together and the game just works.
Rather open a menu? Double-click the collection's own `index.html` for a
landing page of all nine games, or `parents.html` for the grown-ups' overview.

---

## What's new in v1.1 — the Game Master Lab

Every game now has a **🛠️ Game Master** button on its menu (and inside Pause,
where a game has pause). The Lab is a first-class screen where kids go from
playing a game to mastering its code:

- **4 dials that are real code constants.** Each slider is wired directly into
  the game's engine — move it and the game changes *instantly*, mid-play.
- **A theme picker.** Three page-wide color moods per game (day/sunset/night or
  each game's own set). Text always stays readable.
- **Lesson cards.** Short, ages 6–11 explanations tied to the exact constants
  on screen — variables, numbers, conditions, loops.
- **A mini code box.** Kids can type `brushSize = 3` like a real programmer.
  A tiny built-in parser (never `eval`) understands numbers, `+ - * / ( )`,
  and only the game's own constant names. Out-of-range values are gently
  clamped with an explanation; mistakes get friendly "Oops —" teaching
  messages. Nothing can break.
- **Reset to normal.** One tap restores the defaults. All Lab values are saved
  alongside the game in its normal save file.

### The constants in each game

| Game | Lab dials (real constants) |
|---|---|
| whisker-warriors | `heroSpeed`, `heroDmg`, `foeHp`, `fishRate` |
| cloud-hopper | `gravity`, `jumpPower`, `bounciness`, `fruitValue` |
| tiny-sprout-farm | `growSpeed`, `waterPower`, `coinBonus` |
| magic-doodle | `brushSize`, `rainbowSpeed`, `stampSize`, `sparkles` |
| mooshi | `snackTimer`, `boing`, `friendXp`, `wiggle` |
| backyard-grand-prix | `MAXS` (top speed), `ACC` (zoom power), `STEER`, `GRASS` (grip) |
| bridge-buddies | `plankReach`, `buddySpeed`, `bridgeSag`, `hopPower` |
| party-meadow | `bunnyPace`, `fruitSpeed`, `balloonPace`, `songTempo` |
| paw-chess | `thinkTime`, `aiSkill`, `hintBrain`, `pieceHop` |

**A note for grown-ups:** these are difficulty knobs too. If a child finds a
game too hard or too easy, open the Lab together and nudge a dial — that's the
intended way to tune the challenge, no coding required. The per-game READMEs
point at the same dials.

### Other v1.1 polish, collection-wide

- Rebranded footer on every game: "<game's emoji> Play & Code · made with ❤️ for young coders · v1.1".
- Buttons sized for small hands (44 px minimum touch targets).
- Notifications moved clear of game controls and titles.
- Keyboard guard so Space/arrows never scroll the game away mid-play.
- All nine games re-audited: security greps clean, hostile input tests passed,
  layout verified on desktop and narrow (480 px) screens.

---

## For kids: from player to game master

You don't need to know anything about coding to start — the games teach it
by letting you touch the code without knowing it's code:

1. **Play.** Pick any game and just have fun. Every button, slider, and
   critter is yours to explore.
2. **Tweak.** Open the **🛠️ Game Master** screen. Drag a dial and watch the
   game change instantly — faster karts, bigger stamps, sillier bunnies.
   That dial *is* a variable, the same kind real programs use.
3. **Read the cards.** Each Lab explains one idea — what a variable is, how
   a loop repeats, what an `if` decides — using the exact dials in front of
   you.
4. **Type real code.** In the mini code box, try `brushSize = 3` or
   `gravity = 2`. You're writing instructions the game obeys, just like a
   programmer. Make a typo on purpose — the friendly "Oops —" messages are
   part of the lesson.
5. **Invent.** Set the dials to something wild, then reset and tell a friend
   what you discovered. That's the whole job of a game designer.

**For parents and teachers:** the same dials are your difficulty settings —
if a game frustrates or bores, nudge it together. The per-game README lists
what each knob changes and what's saved where.

## Kid-safe by design
- **Fully offline.** The only network string in any file is the SVG icon
  declaration. Nothing phones home; there is nothing to track.
- **No ads, no purchases, no loot boxes, no energy timers, no streaks.** Nothing
  bad ever happens because a child stopped playing.
- **Gentle failure everywhere.** "Good try!" and instant retries, never
  punishment language.
- **No adult dialogs.** No `alert`/`confirm` popups; confirmations are big
  friendly in-screen buttons (reset always asks twice).
- **Original characters and art** — emoji and hand-drawn canvas shapes only.

## Tips

- **Save data** stays in the browser on that computer (one versioned
  `localStorage` key per game). Clearing browser site data resets everything —
  each game's Settings also has a two-step "Reset everything".
- **Sound** starts on; every game has a sound toggle in Settings. Audio is tiny
  synthesized chimes (WebAudio) — no audio files.
- **Where a game pauses** (Esc or the pause button), it truly stops — safe to
  walk away mid-race.

## For the curious

- Built with Vue 3 (global build) + Tailwind, one HTML file per game, MIT-licensed.
- The Lab's code box is a hand-written whitelist tokenizer and recursive-descent
  parser — identifiers, numbers and `+ - * / ( )` only. It is mathematically
  incapable of executing arbitrary code.
- The shared rules all nine games follow (and future ones must) live in
  `_shared/GAME_STANDARD.md`.
