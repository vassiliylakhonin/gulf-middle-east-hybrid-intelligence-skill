#!/usr/bin/env python3
"""
Structural validator for the Gulf + Middle East Hybrid Intelligence Skill.
Checks skill file structure, example evidence-mode discipline, and forbidden patterns.
This is a structural check — it does not verify factual correctness.
"""

import os
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ERRORS = []
WARNINGS = []


def err(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}")


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def ok(msg):
    print(f"  OK:    {msg}")


# ── 1. SKILL.md structure ──────────────────────────────────────────────────────

def check_skill_md():
    print("\n[1] skills/claude/SKILL.md")
    path = ROOT / "skills" / "claude" / "SKILL.md"
    if not path.exists():
        err("skills/claude/SKILL.md missing")
        return

    text = path.read_text()

    # YAML frontmatter
    if not text.startswith("---"):
        err("Missing YAML frontmatter (must start with ---)")
    else:
        ok("YAML frontmatter present")

    required_frontmatter = ["name:", "description:"]
    for field in required_frontmatter:
        if field in text[:500]:
            ok(f"Frontmatter field '{field}' present")
        else:
            err(f"Frontmatter field '{field}' missing")

    # Required sections
    required_sections = [
        "## Core Contract",
        "## Intake",
        "## Evidence Discipline",
        "## Output Structure",
        "## Failure handling",
        "## Self-check",
    ]
    for section in required_sections:
        if section in text:
            ok(f"Section '{section}' present")
        else:
            err(f"Required section '{section}' missing")

    # Must contain Iran actor distinction
    if "IRGC" in text and "Iran-state" in text and "Iran-private" in text:
        ok("Iran actor distinction (Iran-state / IRGC-affiliated / Iran-private) present")
    else:
        err("Iran actor distinction (Iran-state / IRGC-affiliated / Iran-private commercial) missing or incomplete")

    # Must contain evidence mode list
    modes = ["live-source-backed", "user-provided sources", "illustrative source packet", "reasoning-only"]
    for mode in modes:
        if mode in text:
            ok(f"Evidence mode '{mode}' defined")
        else:
            err(f"Evidence mode '{mode}' not defined in SKILL.md")

    # Limitation / safety section
    if "limitation" in text.lower() or "not legal" in text.lower() or "not advice" in text.lower():
        ok("Limitation / safety language present")
    else:
        warn("No explicit limitation or 'not advice' language found in SKILL.md")


# ── 2. Examples: evidence mode and limitation note ────────────────────────────

EVIDENCE_MODES = [
    "live-source-backed",
    "user-provided sources",
    "illustrative source packet",
    "reasoning-only",
]

FORBIDDEN_PATTERNS = [
    (r"this is (?:legal|compliance|sanctions|aml|investment) advice", "Claims to give advice"),
    (r"guarantees? (?:compliance|accuracy|correctness)", "Guarantee claim"),
    (r"production.grade", "Production-grade claim"),
    (r"fully autonomous", "Fully autonomous claim"),
    (r"vessel\s+\w+,?\s+IMO\s+\d{7}", "Specific vessel IMO number without source citation"),
]

REQUIRED_IN_EXAMPLES = [
    ("Evidence mode", r"evidence mode.*`"),
    ("Limitation note", r"limitation note"),
]


def check_examples():
    print("\n[2] examples/")
    examples_dir = ROOT / "examples"
    if not examples_dir.exists():
        err("examples/ directory missing")
        return

    md_files = [f for f in examples_dir.glob("*.md") if f.name != "README.md"]
    if not md_files:
        warn("No example files found in examples/")
        return

    modes_seen = set()

    for f in sorted(md_files):
        print(f"\n  [{f.name}]")
        text = f.read_text().lower()
        original = f.read_text()

        # Evidence mode declared
        mode_found = None
        for mode in EVIDENCE_MODES:
            if mode in text:
                mode_found = mode
                modes_seen.add(mode)
                break
        if mode_found:
            ok(f"Evidence mode declared: {mode_found}")
        else:
            err(f"No evidence mode declared in {f.name}")

        # live-source-backed must have retrieval date
        if mode_found == "live-source-backed":
            if re.search(r"retrieval.*(date|20\d\d)", text) or re.search(r"retrieved.*20\d\d", text):
                ok("Retrieval date present (required for live-source-backed)")
            else:
                err(f"live-source-backed example missing retrieval date: {f.name}")

        # Limitation note
        if "limitation note" in text:
            ok("Limitation note present")
        else:
            err(f"No limitation note in {f.name}")

        # Forbidden patterns (case-insensitive on original)
        for pattern, description in FORBIDDEN_PATTERNS:
            if re.search(pattern, original, re.IGNORECASE):
                err(f"Forbidden pattern [{description}] in {f.name}")

    print(f"\n  Evidence modes seen across examples: {modes_seen}")
    for mode in EVIDENCE_MODES:
        if mode in modes_seen:
            ok(f"Mode '{mode}' demonstrated")
        else:
            warn(f"Mode '{mode}' not demonstrated in any example")


# ── 3. Signals: structure and disclaimer ─────────────────────────────────────

def check_signals():
    print("\n[3] signals/")
    signals_dir = ROOT / "signals"
    if not signals_dir.exists():
        err("signals/ directory missing")
        return

    template = signals_dir / "TEMPLATE.md"
    if template.exists():
        ok("TEMPLATE.md present")
    else:
        err("signals/TEMPLATE.md missing")

    index = signals_dir / "index.json"
    if index.exists():
        ok("index.json present")
    else:
        err("signals/index.json missing")

    feed = signals_dir / "feed.json"
    if feed.exists():
        ok("feed.json present")
    else:
        err("signals/feed.json missing")

    latest = signals_dir / "latest.md"
    if latest.exists():
        ok("latest.md present")
    else:
        err("signals/latest.md missing")

    if index.exists() and feed.exists() and latest.exists():
        try:
            index_payload = json.loads(index.read_text(encoding="utf-8"))
            feed_payload = json.loads(feed.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"signals JSON is invalid: {exc}")
        else:
            latest_entry = index_payload.get("latest", {})
            latest_path = ROOT / latest_entry.get("path", "")
            if latest_path.exists():
                ok("signals/index.json latest path exists")
            else:
                err(f"signals/index.json latest path missing: {latest_entry.get('path')}")

            latest_text = latest.read_text(encoding="utf-8")
            if latest_entry.get("title") and latest_entry["title"] in latest_text:
                ok("signals/latest.md matches signals/index.json latest title")
            else:
                err("signals/latest.md does not contain signals/index.json latest title")

            index_urls = {item.get("url") for item in index_payload.get("signals", [])[:20]}
            feed_urls = {item.get("url") for item in feed_payload.get("items", [])}
            missing = sorted(index_urls - feed_urls)
            if missing:
                err(f"signals/feed.json missing URLs from signals/index.json: {missing}")
            else:
                ok("signals/feed.json covers signals/index.json entries")

    signal_files = list(signals_dir.rglob("*.md"))
    signal_files = [f for f in signal_files if f.name not in ("TEMPLATE.md", "README.md", "latest.md")]

    for f in signal_files:
        print(f"\n  [{f.name}]")
        text = f.read_text().lower()
        if "evidence mode" in text:
            ok("Evidence mode stated")
        else:
            err(f"No evidence mode in signal {f.name}")
        if "disclaimer" in text or "not official intelligence" in text:
            ok("Disclaimer present")
        else:
            err(f"No disclaimer in signal {f.name}")


# ── 4. Evals: required files ──────────────────────────────────────────────────

def check_evals():
    print("\n[4] evals/")
    required = ["checklist.md", "failure-modes.md", "starter-rubric.md"]
    for name in required:
        path = ROOT / "evals" / name
        if path.exists():
            ok(f"{name} present")
            text = path.read_text().lower()
            if "benchmark" in text and "not a benchmark" not in text:
                warn(f"{name} uses 'benchmark' without 'not a benchmark' caveat")
        else:
            err(f"evals/{name} missing")


# ── 5. docs/: required files ─────────────────────────────────────────────────

def check_docs():
    print("\n[5] docs/")
    required = ["source-guide.md", "regional-logic.md", "risk-archetypes.md"]
    for name in required:
        path = ROOT / "docs" / name
        if path.exists():
            ok(f"{name} present")
        else:
            err(f"docs/{name} missing")

    # source-guide.md must have re-verification horizons table
    sg = ROOT / "docs" / "source-guide.md"
    if sg.exists():
        text = sg.read_text().lower()
        if "re-verification" in text or "re-verify" in text:
            ok("source-guide.md has re-verification horizons")
        else:
            err("source-guide.md missing re-verification horizons")


# ── 6. Root files ─────────────────────────────────────────────────────────────

def check_root():
    print("\n[6] Root files")
    required = ["AGENTS.md", "CLAUDE.md", "README.md", "STATUS.md", "llms.txt"]
    for name in required:
        path = ROOT / name
        if path.exists():
            ok(f"{name} present")
        else:
            err(f"{name} missing")

    claude = ROOT / "CLAUDE.md"
    if claude.exists():
        first_line = claude.read_text(encoding="utf-8").splitlines()[0].strip()
        if first_line == "@AGENTS.md":
            ok("CLAUDE.md imports AGENTS.md")
        else:
            err("CLAUDE.md must import AGENTS.md on the first line")

    # AGENTS.md must not claim Bar 2 cleared if STATUS.md says otherwise
    agents = ROOT / "AGENTS.md"
    if agents.exists():
        text = agents.read_text().lower()
        if "bar 2" in text and "not cleared" not in text and "partially cleared" not in text:
            warn("AGENTS.md mentions Bar 2 without 'not cleared' or 'partially cleared' language — verify honesty")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Gulf + Middle East Hybrid Intelligence Skill — Validator")
    print("Structural check only. Does not verify factual correctness.")
    print("=" * 60)

    check_root()
    check_skill_md()
    check_examples()
    check_signals()
    check_evals()
    check_docs()

    print("\n" + "=" * 60)
    print(f"Errors:   {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")

    if ERRORS:
        print("\nFailed checks:")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    elif WARNINGS:
        print("\nPassed with warnings.")
        sys.exit(0)
    else:
        print("\nAll checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
