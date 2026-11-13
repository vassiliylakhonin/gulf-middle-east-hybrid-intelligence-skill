"""Deterministic field comparison of two caller-supplied entity records.

This module owns no data. It does not screen names against sanctions lists,
look anything up, or infer ownership. The caller supplies two records, each
with a stated source, and the tool lists which normalised field values appear
in both. A shared value is a field match, nothing more: shared addresses,
agents, phone numbers and officers are common among unrelated firms, and a
match here is not a conclusion that two entities are the same network, that
one reconstituted the other, or that either is designated or evades anything.
Absence of a match is not evidence of absence of a link.
"""

from __future__ import annotations

import json
import re
import unicodedata
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

REPORT = "match_report"
INVALID_INPUT = "invalid_input"

MIN_PHONE_DIGITS = 7

TEXT_FIELDS = (
    "names",
    "addresses",
    "directors",
    "shareholders",
    "signatories",
    "registered_agents",
    "registration_numbers",
)
PHONE_FIELDS = ("phones",)
EMAIL_FIELDS = ("emails",)
WEB_FIELDS = ("websites",)
ALL_FIELDS = TEXT_FIELDS + PHONE_FIELDS + EMAIL_FIELDS + WEB_FIELDS
PERSON_FIELDS = ("directors", "shareholders", "signatories", "registered_agents")

FIELD_NOTES = {
    "names": "Entity names are compared after case and punctuation normalisation only; no transliteration or alias handling.",
    "addresses": "Shared addresses are common (virtual offices, free-zone and registered-agent addresses); a match is weak on its own.",
    "phones": "Compared as digits only after removing punctuation; shared switchboards and agent numbers occur.",
    "emails": "Compared case-insensitively; shared agent or generic mailboxes occur.",
    "websites": "Compared without scheme, www and trailing slash; shared hosting or parent-brand sites occur.",
    "directors": "Common personal names produce coincidental matches; name-only matching does not identify a person.",
    "shareholders": "Nominee and corporate shareholders are shared across many unrelated entities.",
    "signatories": "Professional signatories act for many entities.",
    "registered_agents": "Registered agents serve many unrelated clients; a match is weak on its own.",
    "registration_numbers": "Compared as normalised text; identical numbers in different registries are not the same registration.",
}

ASSUMPTIONS = [
    "Values are normalised (Unicode NFKD, case-folded, punctuation turned into spaces, whitespace collapsed; phones reduced to digits; websites stripped of scheme, www and trailing slash) and then compared for exact equality.",
    "No transliteration, spelling-variant, abbreviation or fuzzy matching is applied unless the caller supplies near_match_token_overlap, in which case values that are not exact matches but share at least that fraction of their tokens (Jaccard) are listed separately as near matches.",
    "Cross-field matches (for example a director of one record who is the registered agent of the other) are compared only among directors, shareholders, signatories and registered agents.",
    "A field with no values on either side is not compared; absence of data is not absence of a link.",
    "The tool does not check whether either record is accurate or current, whether either entity appears on any sanctions list, or who controls either entity.",
]


def _clean_text(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value).casefold()
    folded = "".join(ch for ch in folded if not unicodedata.combining(ch))
    folded = re.sub(r"[^\w]+", " ", folded, flags=re.UNICODE).replace("_", " ")
    return re.sub(r"\s+", " ", folded).strip()


def _clean_phone(value: str) -> str:
    return re.sub(r"\D", "", value)


def _clean_web(value: str) -> str:
    text = value.strip().casefold()
    text = re.sub(r"^[a-z][a-z0-9+.-]*://", "", text)
    text = re.sub(r"^www\.", "", text)
    return text.rstrip("/")


def _normalise(field: str, value: str) -> str:
    if field in PHONE_FIELDS:
        digits = _clean_phone(value)
        return digits if len(digits) >= MIN_PHONE_DIGITS else ""
    if field in EMAIL_FIELDS:
        return value.strip().casefold()
    if field in WEB_FIELDS:
        return _clean_web(value)
    return _clean_text(value)


class EntityRecord(BaseModel):
    """One caller-supplied record. Every record requires a label and a source."""

    model_config = ConfigDict(extra="forbid")

    label: str = Field(min_length=1)
    source: str = Field(min_length=1)
    as_of: str = ""
    names: list[str] = Field(default_factory=list)
    addresses: list[str] = Field(default_factory=list)
    phones: list[str] = Field(default_factory=list)
    emails: list[str] = Field(default_factory=list)
    websites: list[str] = Field(default_factory=list)
    directors: list[str] = Field(default_factory=list)
    shareholders: list[str] = Field(default_factory=list)
    signatories: list[str] = Field(default_factory=list)
    registered_agents: list[str] = Field(default_factory=list)
    registration_numbers: list[str] = Field(default_factory=list)

    @field_validator("label", "source")
    @classmethod
    def _not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("label and source must be non-empty")
        return value.strip()

    @model_validator(mode="after")
    def _has_at_least_one_value(self) -> "EntityRecord":
        if not any(getattr(self, field) for field in ALL_FIELDS):
            raise ValueError(f"{self.label}: record has no field values to compare")
        return self


class MatchRequest(BaseModel):
    """Two records and an optional caller-chosen near-match threshold."""

    model_config = ConfigDict(extra="forbid")

    record_a: EntityRecord
    record_b: EntityRecord
    near_match_token_overlap: float | None = Field(default=None, gt=0, le=1)

    @model_validator(mode="after")
    def _labels_differ(self) -> "MatchRequest":
        if self.record_a.label == self.record_b.label:
            raise ValueError("record_a and record_b need different labels")
        return self


def _index(record: EntityRecord, field: str) -> tuple[dict[str, list[str]], list[str]]:
    """Map normalised value -> original values; also list unusable originals."""
    index: dict[str, list[str]] = {}
    unusable: list[str] = []
    for original in getattr(record, field):
        key = _normalise(field, original)
        if not key:
            unusable.append(original)
            continue
        index.setdefault(key, [])
        if original not in index[key]:
            index[key].append(original)
    return index, unusable


def _jaccard(a: str, b: str) -> float:
    ta, tb = set(a.split()), set(b.split())
    return len(ta & tb) / len(ta | tb) if ta and tb else 0.0


def _compare_field(
    field: str, a: EntityRecord, b: EntityRecord, threshold: float | None
) -> dict[str, Any] | None:
    ia, bad_a = _index(a, field)
    ib, bad_b = _index(b, field)
    if not ia and not ib and not bad_a and not bad_b:
        return None
    exact = [
        {"normalised": key, a.label: ia[key], b.label: ib[key]}
        for key in sorted(set(ia) & set(ib))
    ]
    entry: dict[str, Any] = {
        "field": field,
        "values_in_a": len(ia),
        "values_in_b": len(ib),
        "exact_matches": exact,
        "note": FIELD_NOTES[field],
    }
    if bad_a or bad_b:
        entry["unusable_values"] = {a.label: bad_a, b.label: bad_b}
    if threshold is not None and field not in PHONE_FIELDS + EMAIL_FIELDS + WEB_FIELDS:
        near = []
        for ka in sorted(set(ia) - set(ib)):
            for kb in sorted(set(ib) - set(ia)):
                score = _jaccard(ka, kb)
                if score >= threshold:
                    near.append(
                        {
                            "token_overlap": round(score, 3),
                            a.label: ia[ka],
                            b.label: ib[kb],
                        }
                    )
        entry["near_matches"] = near
    return entry


def _cross_field(a: EntityRecord, b: EntityRecord) -> list[dict[str, Any]]:
    found = []
    for fa in PERSON_FIELDS:
        for fb in PERSON_FIELDS:
            if fa == fb:
                continue
            ia, _ = _index(a, fa)
            ib, _ = _index(b, fb)
            for key in sorted(set(ia) & set(ib)):
                found.append(
                    {
                        "normalised": key,
                        f"{a.label}.{fa}": ia[key],
                        f"{b.label}.{fb}": ib[key],
                    }
                )
    return found


def compare_records(request: MatchRequest) -> dict[str, Any]:
    """List shared field values between two records. Draws no conclusion."""
    a, b = request.record_a, request.record_b
    threshold = request.near_match_token_overlap
    fields = [
        entry
        for entry in (_compare_field(f, a, b, threshold) for f in ALL_FIELDS)
        if entry is not None
    ]
    cross = _cross_field(a, b)
    exact_total = sum(len(entry["exact_matches"]) for entry in fields)
    return {
        "status": REPORT,
        "tool": "compare_entity_records",
        "result_is_not_a_finding": True,
        "human_review_required": True,
        "records": {
            a.label: {"source": a.source, "as_of": a.as_of},
            b.label: {"source": b.source, "as_of": b.as_of},
        },
        "fields": fields,
        "cross_field_matches": cross,
        "summary": {
            "fields_compared": [entry["field"] for entry in fields],
            "exact_match_count": exact_total,
            "cross_field_match_count": len(cross),
        },
        "assumptions": ASSUMPTIONS,
        "detail": (
            "Field-level overlap between two caller-supplied records only. A "
            "shared value is not evidence that the entities are the same "
            "network, that one reconstituted the other, or that either is "
            "sanctioned; no list was consulted and no source was checked. "
            "Absence of a match is not evidence of no link."
        ),
    }


def compare_records_json(arguments: dict[str, Any]) -> str:
    """Tool entry point: validate, compare, and serialize. Never raises."""
    try:
        request = MatchRequest.model_validate(arguments)
    except ValueError as exc:
        return json.dumps(
            {
                "status": INVALID_INPUT,
                "tool": "compare_entity_records",
                "detail": f"Invalid records: {exc}. Each record needs a label, "
                "a source and at least one field value.",
                "result_is_not_a_finding": True,
                "human_review_required": True,
            }
        )
    return json.dumps(compare_records(request), ensure_ascii=False)
