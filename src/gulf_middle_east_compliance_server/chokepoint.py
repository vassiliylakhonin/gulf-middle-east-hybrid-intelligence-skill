"""Deterministic chokepoint route comparison over caller-supplied figures.

This module owns no data. It holds no tariffs, no war-risk premiums, no fuel
prices, no distances and no vessel speeds. Every number enters with a
caller-stated source, and the tool only combines low/high inputs into low/high
days and cost ranges per route and, when a baseline is named, the difference
against it. It does not judge whether a chokepoint is open, whether a premium
is current, whether cover is available, or which route to take. A result is
arithmetic on the caller's assumptions, not a finding about Hormuz, Bab
el-Mandeb, the Red Sea or any other route.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

HOURS_PER_DAY = 24

ESTIMATE = "estimate"
INVALID_INPUT = "invalid_input"

ARITHMETIC_ASSUMPTIONS = [
    "Sea days are distance_nm / (speed_knots * 24). Waiting or detour days "
    "(waiting_days) are added to elapsed days. Both are caller-supplied with "
    "their sources; this tool holds no distance, speed or queue data.",
    "The low estimate pairs every figure's low with the opposing figure's "
    "favourable end (low distance, high speed, low waiting days, low rates); "
    "the high estimate pairs them in reverse. The range is input-driven, not "
    "a confidence interval, and expresses no likelihood.",
    "Fuel tonnes are sea days times fuel_tonnes_per_sea_day, plus waiting "
    "days times idle_fuel_tonnes_per_day when that figure is supplied. If it "
    "is not supplied, waiting days burn no fuel in this arithmetic.",
    "War-risk cost is premium_percent_of_insured_value / 100 * insured_value "
    "* transits, with transits stated by the caller. The tool holds no "
    "premium data and does not check whether cover exists at any price.",
    "Charter hire, when supplied, is hire_per_day times elapsed days. Other "
    "cost lines are flat per voyage and are added as supplied.",
    "All money figures must use the one currency named in the scenario; the "
    "tool does not convert currencies or fuel units and does not discount "
    "cargo time value, delay penalties or cargo insurance unless the caller "
    "enters them as other cost lines.",
    "Deltas against the baseline pair the route's low with the baseline's "
    "high (and the reverse), so they show the widest difference the inputs "
    "allow. Overlapping ranges mean the inputs do not separate the routes.",
    "The tool does not rank routes, recommend one, or say a route is "
    "available, safe, lawful or sanctions-compliant.",
]


class Figure(BaseModel):
    """One caller-supplied quantity as a low/high range with its source."""

    low: float
    high: float
    source: str = Field(min_length=1)
    unit: str = ""

    @field_validator("source")
    @classmethod
    def _source_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("every figure requires a non-empty source")
        return value.strip()

    @model_validator(mode="after")
    def _range_is_ordered_and_non_negative(self) -> "Figure":
        if self.low < 0:
            raise ValueError("figure low must be non-negative")
        if self.high < self.low:
            raise ValueError("figure high must be greater than or equal to low")
        return self

    def echo(self) -> dict[str, Any]:
        return {"low": self.low, "high": self.high, "unit": self.unit, "source": self.source}


class WarRisk(BaseModel):
    """Caller-supplied war-risk premium, insured value and transit count."""

    premium_percent_of_insured_value: Figure
    insured_value: Figure
    transits: int = Field(ge=0)

    @model_validator(mode="after")
    def _percent_is_a_percentage(self) -> "WarRisk":
        if self.premium_percent_of_insured_value.high > 100:
            raise ValueError("premium_percent_of_insured_value must not exceed 100")
        return self


class CostLine(BaseModel):
    """A flat per-voyage cost the caller wants included, with its source."""

    name: str = Field(min_length=1)
    amount: Figure


class Route(BaseModel):
    """One route option with the caller's distance, speed, fuel and cost figures."""

    name: str = Field(min_length=1)
    distance_nm: Figure
    speed_knots: Figure
    fuel_tonnes_per_sea_day: Figure
    fuel_price_per_tonne: Figure
    waiting_days: Figure | None = None
    idle_fuel_tonnes_per_day: Figure | None = None
    hire_per_day: Figure | None = None
    war_risk: WarRisk | None = None
    other_costs: list[CostLine] = Field(default_factory=list)

    @model_validator(mode="after")
    def _speed_is_positive(self) -> "Route":
        if self.speed_knots.low <= 0:
            raise ValueError(f"{self.name}: speed_knots low must be positive")
        return self


class ChokepointScenario(BaseModel):
    """The caller's route comparison: a currency, routes and an optional baseline."""

    name: str = ""
    currency: str = Field(min_length=1)
    routes: list[Route] = Field(min_length=1)
    baseline_route: str | None = None

    @field_validator("currency")
    @classmethod
    def _currency_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("currency must be stated by the caller")
        return value.strip()

    @model_validator(mode="after")
    def _names_unique_and_baseline_exists(self) -> "ChokepointScenario":
        names = [route.name for route in self.routes]
        if len(set(names)) != len(names):
            raise ValueError("route names must be unique")
        if self.baseline_route is not None and self.baseline_route not in names:
            raise ValueError("baseline_route must name one of the routes")
        return self


def _round(value: float) -> float:
    return round(value, 1)


def _range(low: float, high: float) -> dict[str, float]:
    return {"low": _round(low), "high": _round(high)}


def _route_result(route: Route) -> dict[str, Any]:
    sea_low = route.distance_nm.low / (route.speed_knots.high * HOURS_PER_DAY)
    sea_high = route.distance_nm.high / (route.speed_knots.low * HOURS_PER_DAY)
    wait_low = route.waiting_days.low if route.waiting_days else 0.0
    wait_high = route.waiting_days.high if route.waiting_days else 0.0
    days_low = sea_low + wait_low
    days_high = sea_high + wait_high

    idle_low = route.idle_fuel_tonnes_per_day.low if route.idle_fuel_tonnes_per_day else 0.0
    idle_high = route.idle_fuel_tonnes_per_day.high if route.idle_fuel_tonnes_per_day else 0.0
    fuel_low = sea_low * route.fuel_tonnes_per_sea_day.low + wait_low * idle_low
    fuel_high = sea_high * route.fuel_tonnes_per_sea_day.high + wait_high * idle_high
    fuel_cost_low = fuel_low * route.fuel_price_per_tonne.low
    fuel_cost_high = fuel_high * route.fuel_price_per_tonne.high

    hire_low = days_low * route.hire_per_day.low if route.hire_per_day else 0.0
    hire_high = days_high * route.hire_per_day.high if route.hire_per_day else 0.0

    war_low = war_high = 0.0
    if route.war_risk:
        war = route.war_risk
        war_low = (
            war.premium_percent_of_insured_value.low / 100 * war.insured_value.low * war.transits
        )
        war_high = (
            war.premium_percent_of_insured_value.high / 100 * war.insured_value.high * war.transits
        )

    other_low = sum(line.amount.low for line in route.other_costs)
    other_high = sum(line.amount.high for line in route.other_costs)
    total_low = fuel_cost_low + hire_low + war_low + other_low
    total_high = fuel_cost_high + hire_high + war_high + other_high

    inputs: dict[str, Any] = {
        "distance_nm": route.distance_nm.echo(),
        "speed_knots": route.speed_knots.echo(),
        "fuel_tonnes_per_sea_day": route.fuel_tonnes_per_sea_day.echo(),
        "fuel_price_per_tonne": route.fuel_price_per_tonne.echo(),
    }
    for key in ("waiting_days", "idle_fuel_tonnes_per_day", "hire_per_day"):
        figure = getattr(route, key)
        if figure is not None:
            inputs[key] = figure.echo()
    if route.war_risk is not None:
        inputs["war_risk"] = {
            "premium_percent_of_insured_value": route.war_risk.premium_percent_of_insured_value.echo(),
            "insured_value": route.war_risk.insured_value.echo(),
            "transits": route.war_risk.transits,
        }
    if route.other_costs:
        inputs["other_costs"] = [
            {"name": line.name, **line.amount.echo()} for line in route.other_costs
        ]

    return {
        "name": route.name,
        "inputs": inputs,
        "sea_days": _range(sea_low, sea_high),
        "elapsed_days": _range(days_low, days_high),
        "fuel_tonnes": _range(fuel_low, fuel_high),
        "cost": {
            "fuel": _range(fuel_cost_low, fuel_cost_high),
            "charter_hire": _range(hire_low, hire_high),
            "war_risk": _range(war_low, war_high),
            "other": _range(other_low, other_high),
            "total": _range(total_low, total_high),
        },
    }


def _delta(route: dict[str, Any], base: dict[str, Any], path: tuple[str, ...]) -> dict[str, Any]:
    def pick(item: dict[str, Any]) -> dict[str, float]:
        for key in path:
            item = item[key]
        return item  # type: ignore[return-value]

    mine, theirs = pick(route), pick(base)
    low = mine["low"] - theirs["high"]
    high = mine["high"] - theirs["low"]
    return {
        "low": _round(low),
        "high": _round(high),
        "ranges_overlap": mine["low"] <= theirs["high"] and theirs["low"] <= mine["high"],
    }


def estimate_bypass(scenario: ChokepointScenario) -> dict[str, Any]:
    """Combine caller-supplied figures into per-route ranges. Adds nothing."""
    results = [_route_result(route) for route in scenario.routes]
    comparison = None
    if scenario.baseline_route is not None:
        base = next(item for item in results if item["name"] == scenario.baseline_route)
        comparison = {
            "baseline_route": scenario.baseline_route,
            "routes": [
                {
                    "name": item["name"],
                    "elapsed_days_delta": _delta(item, base, ("elapsed_days",)),
                    "fuel_tonnes_delta": _delta(item, base, ("fuel_tonnes",)),
                    "total_cost_delta": _delta(item, base, ("cost", "total")),
                }
                for item in results
                if item["name"] != scenario.baseline_route
            ],
        }
    return {
        "status": ESTIMATE,
        "tool": "estimate_chokepoint_bypass",
        "result_is_not_a_finding": True,
        "human_review_required": True,
        "scenario": {"name": scenario.name, "currency": scenario.currency},
        "routes": results,
        "comparison_to_baseline": comparison,
        "arithmetic_assumptions": ARITHMETIC_ASSUMPTIONS,
        "detail": (
            "Deterministic arithmetic over caller-supplied figures only. Every "
            "input number carries the source the caller stated; the tool adds "
            "no data and does not check whether inputs are current. It does "
            "not rank or recommend routes and is not a finding about any "
            "chokepoint, route or premium."
        ),
    }


def estimate_bypass_json(arguments: dict[str, Any]) -> str:
    """Tool entry point: validate, estimate, and serialize. Never raises."""
    try:
        scenario = ChokepointScenario.model_validate(arguments)
    except ValueError as exc:
        return json.dumps(
            {
                "status": INVALID_INPUT,
                "tool": "estimate_chokepoint_bypass",
                "detail": f"Invalid scenario: {exc}. No defaults were substituted; "
                "supply every figure with its source.",
                "result_is_not_a_finding": True,
                "human_review_required": True,
            }
        )
    return json.dumps(estimate_bypass(scenario))
