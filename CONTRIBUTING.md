# Contributing to Play & Code

First: thank you. These games exist so any child can play for free and,
almost without noticing, meet the ideas that power real software. Every
contribution that makes a game clearer, kinder, or more fun matters — and
every contribution is read by families, so craft counts double here.

## The hard rules (non-negotiable — CI enforces every one)

1. **Kid-safe, offline, always.** Games must run with the network
   unplugged. Forbidden in any game file:
   - external URLs of any kind (the single allowed `http://` string is the
     SVG favicon `xmlns`),
   - `fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource`,
     `navigator.sendBeacon`, dynamic `import(`,
   - `eval` and `new Function` — the Lab code box uses the whitelist
     parser pattern from `whisker-warriors`,
   - `alert` / `confirm` / `prompt` — build two-tap in-UI confirms instead,
   - free-text inputs except the Lab code box (parsed, never rendered).
2. **Follow the standard.** Read `_shared/GAME_STANDARD.md` fully before
   writing code. It defines the folder shape, the save-key rules, the sound
   pattern, the visual style, and the Game Master Lab requirements.
3. **Folder hygiene.** A game folder contains exactly `index.html`,
   `README.md`, and `lib/`. Nothing else ships.
4. **No personal traces.** No names of real children, no machine paths
   (`C:\`, `/Users/`), no inside jokes a stranger wouldn't get. The games
   are for everyone.
5. **Gentle by design.** No punishment, no timers that scold, no gambling
   mechanics, no scary imagery. Fail states say "Good try!" and offer an
   instant retry.
6. **No CLA, ever.** We will never ask you to sign a Contributor License
   Agreement or assign your copyright. Instead we use the
   [Developer Certificate of Origin](https://developercertificate.org/) —
   sign off your commits with `git commit -s`, which simply certifies you
   wrote the change or have the right to submit it under this project's
   license.

## Making a change

1. Fork, branch, hack. Every game is a single HTML file — no build step,
   no install. Double-click to play.
2. Run the gates locally (same checks as CI; you need Python 3 and
   [Node.js](https://nodejs.org) on your PATH — CI provides both):
   ```bash
   python3 tools/check_games.py     # or: python tools/check_games.py
   ```
   It greps for every forbidden pattern, checks folder hygiene, verifies
   each game still carries its v1.1 footer and version tag, and syntax-checks
   every inline script with `node --check`.
3. Play your change. Fresh save → win → replay → reset. No dead ends, no
   stuck states, and the game must still feel good at 480px wide.
4. Commit with `-s` (DCO sign-off), open a PR, and fill in the template —
   including how you tested it.

## What makes a good contribution here

- **Playfulness with purpose.** The lesson hides inside the fun: a slider
  should change something a kid can *see* immediately.
- **Words for a 6-year-old, ideas for an 11-year-old.** Short sentences,
  warm tone, no jargon without an explanation.
- **Small PRs.** One game, one fix, one idea. A racing game and a typo fix
  should not travel together.
- **Parents are readers too.** README changes should stay accurate about
  what's saved and what the knobs do.

## Releases

Maintainer cuts releases from `main`: bump the collection version in
`CHANGELOG.md`, update each game's footer tag, and the site redeploys
automatically via GitHub Pages.

## Code of Conduct

Applies to all project spaces: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
Be kind; everyone here is learning — including us.

## Questions?

Open an issue with the `question` label. If it's about safety, use the
private channel in [SECURITY.md](SECURITY.md) instead.
