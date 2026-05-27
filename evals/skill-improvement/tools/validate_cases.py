#!/usr/bin/env python3
"""Validate skill-improvement eval case files."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_KEYS = {
    "id",
    "split",
    "domain",
    "prompt",
    "expected_behaviors",
    "failure_modes",
}

VALID_SPLITS = {"train", "validation", "test"}


def validate_case(obj: object, path: Path, line_no: int, seen_ids: set[str]) -> list[str]:
    errors: list[str] = []
    location = f"{path}:{line_no}"

    if not isinstance(obj, dict):
        return [f"{location}: case must be a JSON object"]

    missing = sorted(REQUIRED_KEYS - obj.keys())
    if missing:
        errors.append(f"{location}: missing keys: {', '.join(missing)}")

    extra = sorted(set(obj.keys()) - REQUIRED_KEYS)
    if extra:
        errors.append(f"{location}: unexpected keys: {', '.join(extra)}")

    case_id = obj.get("id")
    if not isinstance(case_id, str) or not case_id:
        errors.append(f"{location}: id must be a non-empty string")
    elif case_id in seen_ids:
        errors.append(f"{location}: duplicate id: {case_id}")
    else:
        seen_ids.add(case_id)

    split = obj.get("split")
    if split not in VALID_SPLITS:
        errors.append(f"{location}: split must be one of {sorted(VALID_SPLITS)}")

    for key in ("domain", "prompt"):
        if not isinstance(obj.get(key), str) or not obj.get(key, "").strip():
            errors.append(f"{location}: {key} must be a non-empty string")

    for key in ("expected_behaviors", "failure_modes"):
        value = obj.get(key)
        if not isinstance(value, list) or not value:
            errors.append(f"{location}: {key} must be a non-empty list")
            continue
        if not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{location}: {key} entries must be non-empty strings")

    return errors


def validate_path(path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()

    if not path.exists():
        return [f"{path}: file does not exist"]

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc}")
            continue
        errors.extend(validate_case(obj, path, line_no, seen_ids))

    if not seen_ids:
        errors.append(f"{path}: no cases found")

    return errors


def main(argv: list[str]) -> int:
    paths = [Path(arg) for arg in argv[1:]]
    if not paths:
        paths = [Path("evals/skill-improvement/cases/gulf-middle-east.jsonl")]

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_path(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(paths)} case file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
