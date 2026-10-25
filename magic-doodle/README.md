# Magic Doodle 🎨

A gentle drawing & coloring app for kids (ages ~6–11). No scores, no timers,
no losing — pure creative play. Part of the free, MIT-licensed **Play & Code**
collection of offline games for young coders.

## How to run
Double-click `index.html` (keep the `lib/` folder next to it — Vue and Tailwind are
bundled inside, so it works with no internet at all).

## What kids can do
- **Free Draw** — draw with finger or mouse (smooth strokes), 12 pastel colors, a 🌈
  rainbow magic brush that cycles hues and sprinkles sparkles, 3 brush sizes, eraser,
  undo (last 20 strokes), emoji stamps that pop with a wobble, and 3 papers
  (cream / meadow / night sky). Save doodles to the Gallery.
- **Coloring** — 10 original line-art pages (Cat, Fish, Butterfly, Rocket, Flower,
  House, Tree, Dino, Car, Crown), all drawn from simple canvas shapes. Tap a region
  to fill it with the selected color; fills fade in with a soft pop. Reset any page
  any time; fills survive page switching and app restarts until reset.
- **Gallery** — up to 12 saved doodles as thumbnails. Tap to view large,
  ⬇️ "Save as picture" downloads a real PNG file (fully local, no network), and
  🗑️ delete uses a two-tap confirm. When full, the oldest doodle is removed to make
  room (the UI says so kindly).

## 🛠️ Game Master Lab
The "🛠️ Game Master" button on the menu opens the Lab, where kids become the boss
of the app. Four chunky sliders multiply real constants in the code, live:
- **🖌️ Brush Size** (`brushSize`) — multiplies every brush stroke's width.
- **🌈 Rainbow Speed** (`rainbowSpeed`) — how fast the rainbow brush cycles colors.
- **🐾 Stamp Size** (`stampSize`) — how big emoji stamps land.
- **✨ Sparkles** (`sparkles`) — how many sparkles the rainbow brush sprinkles (0 = off).
- Plus a **page theme** picker (Candy / Sunset / Starry) that changes the whole sky
  behind the app instantly.

The Lab also has three lesson cards (variables, events & functions, loops) tied to
those exact constants, and a **mini code box** where kids can type real assignments
like `brushSize = 2` or `sparkles = brushSize / 2`. The box uses a tiny hand-written
tokenizer and parser (never `eval`), only knows numbers, `+ - * / ( )` and the four
Lab names, clamps results to each slider's range, snaps to its step, and answers
mistakes with friendly "Oops —" teaching messages.

"Reset to normal" in the Lab restores all defaults. Lab values persist in the save.

## What gets saved (this browser only)
localStorage key **`magicDoodleSave1`**:
- sound on/off and total "doodles saved" counter,
- Game Master Lab values (sliders + theme),
- coloring fills per page,
- the gallery: up to 12 PNG dataURLs stored at **half resolution** (500×325) to stay
  well under the localStorage quota. All storage access is wrapped in try/catch with
  a friendly toast if it ever fills up.

"Reset everything" in Settings (two-step) erases all of the above, Lab included.

## Kid-safe summary
100% offline (zero external URLs), no ads/links/accounts/purchases, no free text
input (the Lab code box is parsed, never rendered), no scores or fail states,
soft short sound effects only (no music), volume low, all confirms are gentle
two-tap in-UI buttons, all artwork is original.

## Tweak-constants guide (top of the `<script>` in index.html)
Most kid-facing knobs are already in the Game Master Lab — prefer tweaking there
(they persist safely and reset cleanly). For deeper changes:
- `MAX_STROKES` (20) — undo history depth in Free Draw.
- `GALLERY_MAX` (12) — gallery capacity.
- `SIZES` ([6,14,26]) — base brush sizes (Lab `brushSize` multiplies these).
- `PALETTE` — available colors.
- `FILL_MS` (220) — coloring fill fade-in duration.
- `LAB_DEFS` — the Lab sliders: keys, min/max/step and defaults.
- `PAGES` — the 10 coloring pages; each lists its fill regions (add/remove entries freely).
