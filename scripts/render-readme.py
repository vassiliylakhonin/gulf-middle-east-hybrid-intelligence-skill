#!/usr/bin/env python3
"""
Regenerate the "Examples by archetype" block in README.md from taxonomy.json.

The block is delimited by markers:
    <!-- TAXONOMY:START -->
    <!-- TAXONOMY:END -->

Run with `--check` to verify README is in sync without writing.
Exit 1 if out of sync (used by validate.py).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
TAXONOMY = ROOT / "taxonomy.json"

START = "<!-- TAXONOMY:START -->"
END = "<!-- TAXONOMY:END -->"


def render_block(tax: dict) -> str:
    archetypes = tax["risk_archetypes"]
    tags = tax["example_tags"]
    by_arch: dict[str, list[dict]] = {a["id"]: [] for a in archetypes}
    for entry in tags:
        for aid in entry.get("archetypes", []):
            if aid in by_arch:
                by_arch[aid].append(entry)

    lines = [
        START,
        "",
        "### Examples by archetype",
        "",
        "_Generated from `taxonomy.json`. To update, edit `taxonomy.json` and run `python3 scripts/render-readme.py`._",
        "",
    ]
    for a in archetypes:
        entries = by_arch[a["id"]]
        lines.append(f"**{a['label']}**")
        if not entries:
            lines.append("- _no examples tagged yet_")
        else:
            for e in sorted(entries, key=lambda x: x["file"]):
                lines.append(f"- [`{e['file']}`]({e['file']}) — `{e['evidence_mode']}`")
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def splice(text: str, block: str) -> str:
    if START not in text or END not in text:
        raise SystemExit(
            f"README.md missing taxonomy markers ({START} / {END}). "
            "Insert them once where the block should live."
        )
    before, _, rest = text.partition(START)
    _, _, after = rest.partition(END)
    return before + block + after


def main() -> int:
    check = "--check" in sys.argv
    tax = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    block = render_block(tax)
    current = README.read_text(encoding="utf-8")
    updated = splice(current, block)

    if check:
        if current != updated:
            print("README.md is out of sync with taxonomy.json. "
                  "Run: python3 scripts/render-readme.py", file=sys.stderr)
            return 1
        print("README.md is in sync with taxonomy.json.")
        return 0

    if current == updated:
        print("README.md already in sync. No change.")
    else:
        README.write_text(updated, encoding="utf-8")
        print("README.md regenerated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
