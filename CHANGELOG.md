# Changelog

All notable changes to the Play & Code collection are documented here.
This project follows [Semantic Versioning](https://semver.org/) at the
collection level (individual games carry their own small version tag).

## [1.1.0] — 2026-10-24

The "Game Master Lab" release. Every game in the collection leveled up.

### Added — in all 9 games
- **Game Master Lab**: a first-class in-game screen (reachable from the menu
  and from Pause) where kids tweak the real code constants behind each game:
  - 4 live sliders per game, wired directly into each game's engine — changes
    apply instantly, mid-play.
  - A 3-option theme picker that recolors the whole page (text always stays
    readable).
  - 3–4 short lesson cards (written for ages 6–11) tied to the exact
    constants on screen — variables, numbers, conditions, loops.
  - A safe mini code box: kids type real assignments like `brushSize = 3`.
    A built-in whitelist parser (never `eval`) accepts numbers,
    `+ - * / ( )`, and the game's own constant names only; out-of-range
    values are gently clamped with an explanation, and mistakes get friendly
    "Oops —" teaching messages.
  - "Reset to normal" restores defaults. Lab values persist in the game's
    existing versioned save.
- Collection landing page (`index.html`) and parents' page (`parents.html`).

### Changed — collection-wide polish
- Rebranded footer on every game: "<game's emoji> Play & Code · made with ❤️
  for young coders · v1.1".
- All interactive controls raised to a 44px minimum touch target.
- Toast notifications repositioned so they never cover game controls, hints,
  or screen titles.
- Keyboard guard: Space/arrows no longer scroll the page away during play
  (inputs like the Lab code box are exempt).
- `ESC` closes the Game Master Lab everywhere.
- Every game re-audited: security greps clean, hostile input tests passed,
  layouts verified at 1280×800 and 480×800.

### Fixed (found by hostile review during this release)
- **party-meadow**: flowerbed emoji rendered as replacement diamonds on every
  non-game screen (UTF-16 split in `v-for`) — now iterates whole code points.
  Canvas meadow backdrop now follows the selected theme.
- **paw-chess**: chessboard rows could be unequal heights and reflow on moves
  (missing `grid-template-rows`); menu/Lab text could be white-on-pastel in
  the Berry theme (now theme-adaptive ink color); Lab readout showed the wrong
  AI depth and poor grammar mid-game.
- **magic-doodle**: a strict-mode slip could crash every code-box assignment
  (undeclared variable) — caught in verification and fixed.
- **mooshi / backyard-grand-prix / bridge-buddies**: toast placement and small
  button sizes polished per audit.

## [1.0.0] — 2026-10-23

Initial public collection: 9 offline, kid-safe, single-file games
(whisker-warriors, cloud-hopper, tiny-sprout-farm, magic-doodle, mooshi,
backyard-grand-prix, bridge-buddies, party-meadow, paw-chess), each with a
menu, How to Play, Settings (sound + two-step reset), synthesized sound
effects, and gentle fail states — all under the MIT license.

[1.1.0]: https://github.com/Shanmuga-Raja-Portfolio/play-and-code/releases
[1.0.0]: https://github.com/Shanmuga-Raja-Portfolio/play-and-code/releases
