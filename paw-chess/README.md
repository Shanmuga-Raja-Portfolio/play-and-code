# ♟️ Paw Chess

Real, complete chess with a warm, cute skin — part of the **Play & Code** collection
for young coders (ages 6–11, MIT licensed).
The rules are proper chess (the whole family can trust it): castling with every legality
condition, en passant, promotion (Queen/Rook/Bishop/Knight picker), check, checkmate,
stalemate, and draws by insufficient material, the 50-move rule and threefold repetition.

## How to run
Double-click `index.html` (this folder must include the `lib` folder — everything is 100%
offline; no internet is used or needed, ever).

## What you can play
- **vs Computer** — 🐱 Kitten (easy), 🐶 Friend (medium), 🦉 Wise Owl (hard). Pick White or Black.
- **👥 Two players** on one screen; the board can flip each turn (toggle, ON by default, remembered).
- **Kid helpers** (all gentle, nothing is ever punished):
  - 🎯 dots showing where the selected piece may move (ON by default, toggleable),
  - 💡 Hint — unlimited, highlights a good move for whoever's turn it is,
  - ↩️ Undo — unlimited; vs the computer it takes back a full round so it stays the child's turn.
- Illegal taps just get a gentle shake and a soft sound; the child can retry instantly.

## 🛠️ Game Master Lab
A first-class screen (big button on the menu, also reachable from Pause) where kids
**tune the real game constants** with sliders and even **type tiny lines of code** in a
safe mini code box (a hand-written tokenizer + parser — never `eval`). Everything applies
live and is saved automatically. The Lab teaches variables, conditions and functions
through the game's own numbers:
- `thinkTime` (×0.5–2) — how long the computer partner may think,
- `aiSkill` (−1 to +1) — how deep the computer looks (gentler or tougher),
- `hintBrain` (1–4) — how hard the Hint button thinks,
- `pieceHop` (0–0.8 s) — the happy hop animation of a piece that just moved,
- 🎨 three page themes (Meadow / Berry / Ocean) that recolor the whole game.

## Kid safety
No ads, no external links, no purchases, no accounts, no free-text inputs (only the Lab's
safe code box), no timers, no punishment language ("Owl wins this one — try again! 💪"
instead of "you lost"). Losses are never shown as failure; every end screen offers a
friendly rematch.

## What gets saved (localStorage key `pawChessSave1`)
- The game in progress (board, full history, mode, difficulty, side) — saved after every
  move and offered back via a "Resume" button on the Play screen.
- Win/draw/loss record vs each computer difficulty.
- Settings: sound, show-legal-dots default state, two-player board flip.
- Game Master Lab values (slider settings + chosen theme).
- "Reset everything" in Settings is a two-step confirm and clears all of the above.

## Tweaking difficulty (for parents)
**Start with the 🛠️ Game Master Lab inside the game** — the sliders above change the
computer's thinking time, skill and hint power live, with no code editing needed, and
they persist for your child. If you want more, open `index.html` in a text editor:
- `LEVELS` (in the app script) — per-partner search depth, time/node caps and Kitten's
  `jitter` (how randomly it plays among near-equal moves; raise for an easier Kitten).
- `VAL` — piece values; `PST` — piece-square tables; `evaluate()` — add/remove terms
  (material / position / mobility).
- `aiChooseMove()` — `timeCap` (ms) and `nodeCap` keep every reply fast; it always
  returns a legal move.

## For the curious: how it was verified
Headless tests (deleted afterward) checked perft node counts — start position
20 / 400 / 8,902 / 197,281, Kiwipete 48 / 2,039 / 97,862, plus three other standard
perft positions — castling-through-check, en passant, under-promotion, stalemate,
checkmate (Fool's mate), all draw rules, threefold repetition, and 60 AI searches on
random self-play positions (all legal, all well under 2 seconds). The v1.1 Game Master
Lab was additionally live-tested in headless Chrome (sliders, code box success/error
paths, themes, persistence).

♟️ Play & Code · made with ❤️ for young coders · v1.1
