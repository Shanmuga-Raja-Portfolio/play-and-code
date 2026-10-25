# Security Policy

## Scope

This repository is a **fully static, fully offline** collection of browser
games for children. There is no server, no backend, no analytics, no login,
and no data collection of any kind — the only thing that can ever load when
a child plays is the files in this repository, and the games work with the
network cable unplugged.

The realistic risks here are:

- A committed secret (API key, token) — ours or a contributor's.
- A change that introduces an external URL, network call, or script
  execution path into a game (every game is audited to have **zero** of
  these; CI enforces it on every pull request).
- A change to vendored libraries in a game's `lib/` folder
  (`vue.global.prod.js`, `tailwind.js`).
- Code in a game that does something beyond what its text and UI claim.

The CI greps catch direct patterns (literal `eval(`, network APIs, URLs).
Deliberately obfuscated JavaScript (string-concatenated API names, base64
payloads) can't be caught by pattern matching alone — which is why `lib/` is
vendored, commits are reviewed by a human, and every game is MIT-licensed
auditable source. If you spot behavior a game's UI doesn't explain, treat it
as a security issue and report it.

## Reporting a vulnerability

**Please do not open a public issue for security reports.**

Use GitHub's private reporting: this repository's **Security tab →
"Report a vulnerability"**. You should receive an acknowledgment within a
few days.

If the issue is in Vue.js or Tailwind CSS themselves (not our code), please
also report it to the upstream project so everyone benefits.

## Supported versions

Only `main` receives fixes. This is a collection of static pages, not a
service — the live site redeploys automatically on every merge to `main`.

## What we commit to

- Secrets committed to this repo are treated as compromised: revoked first,
  investigated second.
- The game guard (`tools/check_games.py`) runs in CI on every PR and push:
  it fails the build on any external URL, network API, `eval`, dialog popup,
  or folder-hygiene violation in any game.
- Everything in this repository is MIT-licensed, including vendored
  libraries, so anyone can audit every byte a child would run.
