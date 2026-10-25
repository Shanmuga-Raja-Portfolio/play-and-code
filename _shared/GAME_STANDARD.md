# Play & Code — Game Standard v2 (READ FULLY BEFORE BUILDING)

Every game in this open collection follows these rules. They exist so anyone can trust
every folder blindly. Reference implementation: `../whisker-warriors/index.html` — read it
first and reuse its patterns (head boilerplate, Sfx class, save handling, UI button styles,
Vue setup, canvas DPR handling).

## Folder & files
- You build exactly: `<your-folder>/index.html` and `<your-folder>/README.md`.
- `lib/vue.global.prod.js` and `lib/tailwind.js` are ALREADY copied into your folder. Reference them as `<script src="lib/vue.global.prod.js"></script>` and `<script src="lib/tailwind.js"></script>`.
- Touch NOTHING outside your own folder.

## Offline & security (non-negotiable, the parent audits these)
- ZERO external URLs. No CDN, no web fonts, no remote images, no `//` protocol-relative URLs. The ONLY `http://` allowed in the file is the xmlns string inside the inline SVG favicon (copy the favicon line from whisker-warriors).
- Copy the head pattern from whisker-warriors including the "files incomplete" fallback check (the `if (!window.Vue || !window.tailwind)` block). No document.write CDN fallbacks — there is no internet, ever.
- FORBIDDEN: `fetch(`, `XMLHttpRequest`, `WebSocket`, `EventSource`, `navigator.sendBeacon`, dynamic `import(`, `<link href="http...">`, `<img src="http...">`, `@import`, `url(http...)`.
- No `alert/confirm/prompt` — build two-tap in-UI confirms instead.
- No free text inputs. Choices come from buttons/emoji pickers. If any user string must ever render, only via Vue `{{ }}` interpolation (auto-escaped).
- localStorage wrapped in try/catch. One versioned key per game (e.g. `cloudHopperSave1`). Load = merge over defaults. Settings must include a two-step "Reset everything".

## Kid-safe design (non-negotiable)
- No ads, external links, purchases, loot boxes, gambling-style randomness, energy/lives, wait timers that punish leaving, daily streaks, or guilt mechanics. Nothing bad happens because a child stopped playing.
- Fail states are gentle + instant retry: poof/bounce/"oops" language only. No blood, no scary imagery, no punishment language ("you failed" → say "Good try!").
- All characters, names, and art are original. Art = emoji + canvas-drawn shapes + CSS only.

## Tech requirements
- Vue 3 global build, Options API, one root app, template in the HTML body (v-if screens). Tailwind via the local play build (`tailwind.config` inline like whisker-warriors).
- Canvas games: `requestAnimationFrame` loop; `dt = Math.min(0.05, ...)`; the loop MUST stop (running=false / cancel) when leaving the game screen or opening a result overlay that ends play; devicePixelRatio scaling capped at 2.
- Sound: copy the `Sfx` WebAudio class pattern from whisker-warriors (tiny oscillator envelopes; `ensure()` on first pointerdown; master `on` flag). Include: UI click, positive event, win jingle (ascending arpeggio), gentle "oops" (descending). Sound toggle in Settings, persisted.
- Screens: Menu (bouncing emoji row + big buttons Play / How to Play / Settings, footer "🐱 Play & Code · made with ❤️ for young coders" (emoji matches each game), small version tag), the game itself, How to Play, Settings (sound toggle + reset + tiny stats line). Pause overlay where a session is longer than ~30s (Esc/P).
- Keyboard: prevent default on Space/arrows during play so the page never scrolls. Guard hotkeys to the active screen.

## Visual style — "cute" is the spec
- Pastel palette, rounded-2xl+ corners, chunky `.btn` styles (copy the CSS block from whisker-warriors), pressed animation, soft shadows, font stack `'Comic Sans MS','Chalkboard SE','Marker Felt','Segoe UI',sans-serif`.
- Canvas cuteness: squash-and-stretch (sin-based bob while moving), blinking eyes, soft ellipse shadows under characters, floating "+1" feedback text with stroke, particle poofs (💫✨) on events, gentle scenery (clouds, flowers) with slight parallax.
- Wins: stars that pop in sequence (CSS keyframes like whisker-warriors), emoji confetti, happy jingle.
- Empty states and buttons must be big enough for small hands. Minimum hit target ~44px.

## Game Master Lab (required in every game)
The Lab is how kids go from playing the game to mastering its code. It is a first-class
screen, as polished as everything else.
- Entry: a chunky "🛠️ Game Master" button on the Menu screen (same visual weight as Play),
  and reachable from the Pause overlay where one exists.
- Controls: 3–5 sliders/toggles/color or emoji pickers bound to REAL constants in the game
  code (gravity, speed, spawn rates, colors, ...). Every control applies live so the game
  visibly changes the moment it moves. Include a "Reset to normal" button. Chosen values
  persist inside the game's existing versioned localStorage save (merge over defaults, same
  try/catch rules).
- Lesson cards: 2–4 short cards (written for ages 6–11) tied to those exact controls,
  teaching what fits the game from: variables, numbers, conditions (if), loops,
  functions/events. Each card names the constant it demos.
- Mini code box: accepts `name = expression` or a bare expression. Implement a tiny
  whitelist tokenizer/parser — only numbers, `+ - * / ( )`, and identifiers from the
  exposed-constants list. NEVER `eval` or `new Function`. Clamp results to each constant's
  min/max. Bad input gets a friendly "Oops —" teaching error (unknown name, bad math).
  Code-box input is parsed, never rendered as HTML.
- The Lab must pause or safely coexist with the game loop per the existing loop-stop rules
  (no double rAF loops; the loop stays stopped while a play-ending overlay is open).

## Self-check before you finish (do all of these)
1. `grep -nE "https?://|fetch\(|XMLHttpRequest|WebSocket|sendBeacon|EventSource" index.html` → ONLY the favicon xmlns line may match.
2. Syntax-check your JS: extract each `<script>` block content (the ones WITHOUT a src attribute) to a temp .js file and run `node --check` on it (node is available). Fix every error.
3. Re-read your Vue template line by line: every method/computed/property referenced in the template exists in the app; NO `Math.` calls inside template expressions (define computeds); every screen is reachable; every button does something.
4. Mentally play fresh-save → win → replay → reset. No dead ends, no stuck states.
5. Balance for ages ~6–11: winnable, words simple, challenge in the game not the UI.
6. README.md for parents: how to run (double-click index.html), what gets saved, the kid-safe summary, and which constants to tweak for difficulty.
7. Game Master Lab is reachable from the Menu (and Pause where one exists).
8. Every Lab control visibly changes the game the moment it moves.
9. The mini code box rejects bad input gracefully (friendly "Oops —" errors, no crash, no eval) and clamps out-of-range values.
10. Lab values persist across reload inside the versioned save, and "Reset to normal" restores defaults.

## Final report format (keep under 200 words)
- What you built + folder name
- Controls / how to play in 3 lines
- Save key + what's saved
- Anything you could not verify yourself (the orchestrator browser-tests after you)
