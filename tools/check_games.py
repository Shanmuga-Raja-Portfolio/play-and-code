#!/usr/bin/env python3
"""Play & Code — the game guard.

Runs the same checks on every PR and push (see .github/workflows/ci.yml):
offline/security greps, folder hygiene, version/footer presence, and a
syntax check of every inline script.

Usage: python3 tools/check_games.py        (repo root as cwd)
Exit code 0 = all gates pass, 1 = at least one gate failed.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAMES = [
    "whisker-warriors", "cloud-hopper", "tiny-sprout-farm",
    "magic-doodle", "mooshi", "backyard-grand-prix",
    "bridge-buddies", "party-meadow", "paw-chess",
]

# Patterns that must NEVER appear in a game file. The collection is offline
# and kid-safe; each of these is a hard fail.
FORBIDDEN = [
    (r"\beval\s*\(", "eval()"),
    (r"new\s+Function\b", "new Function"),
    (r"\bfetch\s*\(", "fetch()"),
    (r"XMLHttpRequest", "XMLHttpRequest"),
    (r"\bWebSocket\b", "WebSocket"),
    (r"EventSource", "EventSource"),
    (r"sendBeacon", "sendBeacon"),
    (r"dynamic import|import\s*\(", "dynamic import()"),
    (r"\balert\s*\(", "alert()"),
    (r"\bconfirm\s*\(", "confirm()"),
    (r"\bprompt\s*\(", "prompt()"),
    (r"abhay|veda", "personal name residue"),
    (r"[A-Za-z]:\\\\Users\\\\", "absolute machine path"),
    (r"(?:src|href)\s*=\s*[\"']\s*//", "protocol-relative URL (//host)"),
    (r"@import\b|url\(\s*[\"']?\s*//", "protocol-relative CSS URL"),
]

# The only http(s) string allowed anywhere: the SVG favicon xmlns.
URL_RE = re.compile(r"https?://")
URL_OK = re.compile(r"w3\.org/2000/svg")

# Vendored libraries live here and are not re-audited line by line
# (they are MIT-licensed upstream; SECURITY.md covers the risk model).
VENDORED = ("lib/vue.global.prod.js", "lib/tailwind.js")

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg: str) -> None:
    print(f"  ok    {msg}")


def check_file(path: Path, allow_urls: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{rel}: not valid UTF-8")
        return
    for pattern, label in FORBIDDEN:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            line = text.count("\n", 0, m.start()) + 1
            fail(f"{rel}:{line} forbidden pattern: {label}")
    if not allow_urls:
        for m in URL_RE.finditer(text):
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line = text[line_start: line_end if line_end != -1 else len(text)]
            if not URL_OK.search(line):
                lineno = text.count("\n", 0, m.start()) + 1
                fail(f"{rel}:{lineno} external URL not allowed: {line.strip()[:80]}")


def check_game(name: str) -> None:
    print(f"[game] {name}")
    folder = ROOT / name
    if not folder.is_dir():
        fail(f"{name}: folder missing")
        return
    entries = sorted(p.name for p in folder.iterdir())
    if entries != ["README.md", "index.html", "lib"]:
        fail(f"{name}: folder must contain exactly README.md, index.html, lib/ "
             f"(found {entries})")
    index = folder / "index.html"
    if index.is_file():
        text = index.read_text(encoding="utf-8", errors="replace")
        if "Game Master" not in text:
            fail(f"{name}: Game Master Lab button not found")
        if not re.search(r"made with \u2764\ufe0f? for young coders", text):
            fail(f"{name}: Play & Code footer not found")
        if not re.search(r"v1\.1", text):
            fail(f"{name}: version tag v1.1 not found")
        check_file(index, allow_urls=False)
        check_inline_scripts(index)
    for rel in VENDORED:
        p = folder / rel
        if not p.is_file():
            fail(f"{name}: missing {rel}")
        else:
            check_file(p, allow_urls=True)


def check_inline_scripts(index: Path) -> None:
    rel = index.relative_to(ROOT).as_posix()
    text = index.read_text(encoding="utf-8", errors="replace")
    blocks = re.findall(
        r"<script(?![^>]*\bsrc\s*=)[^>]*>(.*?)</script>",
        text, re.DOTALL | re.IGNORECASE)
    if not blocks:
        fail(f"{rel}: no inline script blocks found (suspicious)")
        return
    for i, block in enumerate(blocks):
        if not block.strip():
            continue
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(
                    mode="w", suffix=".js", delete=False,
                    encoding="utf-8") as f:
                f.write(block)
                tmp = f.name
            try:
                result = subprocess.run(
                    ["node", "--check", tmp],
                    capture_output=True, text=True)
            except FileNotFoundError:
                fail(f"{rel}: 'node' is required for the syntax gate "
                     "(install Node.js or use the CI run)")
                continue
            if result.returncode != 0:
                fail(f"{rel}: inline script #{i + 1} fails node --check: "
                     f"{result.stderr.strip()[:200]}")
        finally:
            if tmp:
                os.unlink(tmp)
    ok(f"{rel}: {len(blocks)} inline script block(s) syntax-checked")


def main() -> int:
    print("[guard] Play & Code game guard")
    license_path = ROOT / "LICENSE"
    if license_path.is_file() and "MIT License" in license_path.read_text(
            encoding="utf-8", errors="replace"):
        ok("LICENSE is MIT")
    else:
        fail("LICENSE missing or not MIT")
    for name in GAMES:
        check_game(name)
    print()
    if errors:
        print(f"[guard] FAILED — {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"[guard] all gates passed for {len(GAMES)} games")
    return 0


if __name__ == "__main__":
    sys.exit(main())
