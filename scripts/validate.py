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

            feed_by_id = {item.get("id"): item for item in feed_payload.get("items", [])}
            for signal in index_payload.get("signals", []):
                slug = signal.get("slug")
                feed_item = feed_by_id.get(slug)
                if not feed_item:
                    err(f"signals/feed.json missing item id for slug: {slug}")
                    continue

                if feed_item.get("title") == signal.get("title"):
                    ok(f"signals/feed.json title matches index for {slug}")
                else:
                    err(f"signals/feed.json title mismatch for {slug}")

                expected_date = f"{signal.get('date')}T00:00:00Z"
                if feed_item.get("date_published") == expected_date:
                    ok(f"signals/feed.json date matches index for {slug}")
                else:
                    err(f"signals/feed.json date mismatch for {slug}: expected {expected_date}")

                if feed_item.get("url") == signal.get("url"):
                    ok(f"signals/feed.json URL matches index for {slug}")
                else:
                    err(f"signals/feed.json URL mismatch for {slug}")

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

    readme = ROOT / "README.md"
    status = ROOT / "STATUS.md"

    if readme.exists():
        text = readme.read_text(encoding="utf-8").lower()
        forbidden_claims = [
            "production-grade",
            "guarantees compliance",
            "guarantees accuracy",
            "detects sanctions evasion",
            "detects dark-fleet activity",
            "fully autonomous",
            "trusted by",
            "used by",
        ]
        for claim in forbidden_claims:
            if claim in text:
                err(f"README.md contains unsupported claim: {claim}")

        if "no production usage record exists yet" in text or "no real-use evidence" in text:
            ok("README.md discloses lack of real-use evidence")
        else:
            err("README.md must disclose that no real-use evidence exists yet")

        required_links = [
            "github.com/vassiliylakhonin/agenda-intelligence-md",
            "github.com/vassiliylakhonin/global-think-tank-analyst",
            "github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill",
        ]
        for link in required_links:
            if link.lower() in text:
                ok(f"README.md links companion repo: {link}")
            else:
                err(f"README.md missing companion repo link: {link}")

    if status.exists():
        text = status.read_text(encoding="utf-8").lower()
        if "**bar 2 — not cleared.**" in text:
            ok("STATUS.md states Bar 2 is not cleared")
        else:
            err("STATUS.md must explicitly state: **Bar 2 — not cleared.**")


# ── 7. taxonomy.json: internal consistency and example tags ──────────────────

# Slug form (taxonomy IDs) ↔ prose form (text inside example files).
EVIDENCE_MODE_SLUG_TO_PROSE = {
    "live-source-backed": "live-source-backed",
    "user-provided-sources": "user-provided sources",
    "illustrative-source-packet": "illustrative source packet",
    "reasoning-only": "reasoning-only",
}


def check_taxonomy():
    print("\n[7] taxonomy.json")
    path = ROOT / "taxonomy.json"
    if not path.exists():
        warn("taxonomy.json missing (optional)")
        return

    try:
        tax = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        err(f"taxonomy.json is invalid JSON: {exc}")
        return
    ok("taxonomy.json parses as JSON")

    evidence_ids = {m["id"] for m in tax.get("evidence_modes", [])}
    archetype_ids = {a["id"] for a in tax.get("risk_archetypes", [])}
    source_domain_ids = {s["id"] for s in tax.get("source_domains", [])}

    region_ids = set()
    for bucket in tax.get("regions", {}).values():
        region_ids.update(r["id"] for r in bucket)

    actor_ids = set()
    for bucket in tax.get("actor_categories", {}).values():
        actor_ids.update(a["id"] for a in bucket)

    if not (evidence_ids and archetype_ids and region_ids and actor_ids):
        err("taxonomy.json missing one of: evidence_modes, risk_archetypes, regions, actor_categories")
        return
    ok(f"Taxonomy has {len(region_ids)} regions, {len(actor_ids)} actors, "
       f"{len(archetype_ids)} archetypes, {len(source_domain_ids)} source domains")

    # Every evidence_mode slug must have a known prose form.
    for eid in evidence_ids:
        if eid not in EVIDENCE_MODE_SLUG_TO_PROSE:
            err(f"taxonomy.json evidence_mode id '{eid}' has no prose mapping in validator")

    # example_tags: file exists, IDs are known, evidence_mode matches the file.
    for entry in tax.get("example_tags", []):
        rel = entry.get("file", "")
        f = ROOT / rel
        if not f.exists():
            err(f"taxonomy.json example_tags references missing file: {rel}")
            continue

        em = entry.get("evidence_mode")
        if em not in evidence_ids:
            err(f"{rel}: evidence_mode '{em}' not in taxonomy.evidence_modes")
        else:
            prose = EVIDENCE_MODE_SLUG_TO_PROSE[em]
            file_text = f.read_text(encoding="utf-8").lower()
            if prose not in file_text:
                err(f"{rel}: taxonomy tags evidence_mode '{em}' "
                    f"but file does not contain '{prose}'")

        for r in entry.get("regions", []):
            if r not in region_ids:
                err(f"{rel}: unknown region id '{r}'")
        for a in entry.get("actors", []):
            if a not in actor_ids:
                err(f"{rel}: unknown actor id '{a}'")
        for arch in entry.get("archetypes", []):
            if arch not in archetype_ids:
                err(f"{rel}: unknown archetype id '{arch}'")
        for sd in entry.get("source_domains", []):
            if sd not in source_domain_ids:
                err(f"{rel}: unknown source_domain id '{sd}'")

    # Every non-README example file should be tagged.
    examples_dir = ROOT / "examples"
    tagged_files = {entry.get("file") for entry in tax.get("example_tags", [])}
    for f in sorted(examples_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        rel = f"examples/{f.name}"
        if rel not in tagged_files:
            warn(f"{rel} is not tagged in taxonomy.json example_tags")

    # README must be in sync with the generated taxonomy block.
    import subprocess
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "render-readme.py"), "--check"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        ok("README.md taxonomy block is in sync with taxonomy.json")
    else:
        err("README.md taxonomy block is stale. Run: python3 scripts/render-readme.py")


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
    check_taxonomy()

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
