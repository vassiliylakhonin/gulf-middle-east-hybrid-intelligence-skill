"""Arithmetic and refusal tests for the chokepoint route comparison."""

import json
import unittest

from gulf_middle_east_compliance_server.chokepoint import estimate_bypass_json


def fig(low, high, source="test source"):
    return {"low": low, "high": high, "source": source}


def route(name="direct", **overrides):
    base = {
        "name": name,
        "distance_nm": fig(1000, 1200),
        "speed_knots": fig(10, 12),
        "fuel_tonnes_per_sea_day": fig(30, 40),
        "fuel_price_per_tonne": fig(500, 600),
    }
    base.update(overrides)
    return base


def run(scenario):
    return json.loads(estimate_bypass_json(scenario))


class ArithmeticTests(unittest.TestCase):
    def test_days_fuel_and_cost_pair_low_with_favourable_inputs(self):
        out = run({"currency": "USD", "routes": [route()]})
        r = out["routes"][0]
        # low: 1000 / (12*24) = 3.4722 days; high: 1200 / (10*24) = 5.0 days
        self.assertEqual(r["sea_days"], {"low": 3.5, "high": 5.0})
        # fuel low 3.4722*30 = 104.17; high 5*40 = 200
        self.assertEqual(r["fuel_tonnes"], {"low": 104.2, "high": 200.0})
        # cost low 104.1667*500 = 52083.3; high 200*600 = 120000
        self.assertEqual(r["cost"]["fuel"], {"low": 52083.3, "high": 120000.0})
        self.assertEqual(r["cost"]["total"], r["cost"]["fuel"])
        self.assertEqual(out["status"], "estimate")
        self.assertTrue(out["result_is_not_a_finding"])
        self.assertIsNone(out["comparison_to_baseline"])

    def test_waiting_hire_war_risk_and_other_costs(self):
        r = run(
            {
                "currency": "USD",
                "routes": [
                    route(
                        distance_nm=fig(240, 240),
                        speed_knots=fig(10, 10),
                        fuel_tonnes_per_sea_day=fig(10, 10),
                        fuel_price_per_tonne=fig(100, 100),
                        waiting_days=fig(1, 3),
                        idle_fuel_tonnes_per_day=fig(2, 2),
                        hire_per_day=fig(1000, 1000),
                        war_risk={
                            "premium_percent_of_insured_value": fig(0.5, 1.0),
                            "insured_value": fig(1_000_000, 1_000_000),
                            "transits": 2,
                        },
                        other_costs=[{"name": "agent fee", "amount": fig(500, 700)}],
                    )
                ],
            }
        )["routes"][0]
        self.assertEqual(r["sea_days"], {"low": 1.0, "high": 1.0})
        self.assertEqual(r["elapsed_days"], {"low": 2.0, "high": 4.0})
        self.assertEqual(r["fuel_tonnes"], {"low": 12.0, "high": 16.0})
        self.assertEqual(r["cost"]["fuel"], {"low": 1200.0, "high": 1600.0})
        self.assertEqual(r["cost"]["charter_hire"], {"low": 2000.0, "high": 4000.0})
        self.assertEqual(r["cost"]["war_risk"], {"low": 10000.0, "high": 20000.0})
        self.assertEqual(r["cost"]["other"], {"low": 500.0, "high": 700.0})
        self.assertEqual(r["cost"]["total"], {"low": 13700.0, "high": 26300.0})

    def test_zero_transits_means_zero_war_risk(self):
        r = run(
            {
                "currency": "USD",
                "routes": [
                    route(
                        war_risk={
                            "premium_percent_of_insured_value": fig(1, 1),
                            "insured_value": fig(100, 100),
                            "transits": 0,
                        }
                    )
                ],
            }
        )["routes"][0]
        self.assertEqual(r["cost"]["war_risk"], {"low": 0.0, "high": 0.0})

    def test_baseline_deltas_use_widest_pairing_and_flag_overlap(self):
        a = route("hormuz", distance_nm=fig(500, 500), speed_knots=fig(10, 10))
        b = route("bypass", distance_nm=fig(900, 1000), speed_knots=fig(10, 10))
        out = run({"currency": "USD", "routes": [a, b], "baseline_route": "hormuz"})
        cmp = out["comparison_to_baseline"]
        self.assertEqual(cmp["baseline_route"], "hormuz")
        self.assertEqual([r["name"] for r in cmp["routes"]], ["bypass"])
        days = cmp["routes"][0]["elapsed_days_delta"]
        # bypass 3.75..4.1667 vs base 2.0833..2.0833 -> 1.7 .. 2.1
        self.assertEqual(days["low"], 1.7)
        self.assertEqual(days["high"], 2.1)
        self.assertFalse(days["ranges_overlap"])

        same = run({"currency": "USD", "routes": [a, dict(a, name="copy")], "baseline_route": "hormuz"})
        self.assertTrue(same["comparison_to_baseline"]["routes"][0]["total_cost_delta"]["ranges_overlap"])

    def test_output_never_ranks_or_recommends(self):
        out = run({"currency": "USD", "routes": [route("a"), route("b")], "baseline_route": "a"})
        text = json.dumps(out).lower()
        for word in ("recommend_", "cheapest", "best_route", "\"rank\"", "preferred"):
            self.assertNotIn(word, text)
        self.assertTrue(out["human_review_required"])


class RefusalTests(unittest.TestCase):
    def assert_invalid(self, scenario):
        out = run(scenario)
        self.assertEqual(out["status"], "invalid_input")
        self.assertTrue(out["result_is_not_a_finding"])
        self.assertTrue(out["human_review_required"])
        self.assertNotIn("routes", out)

    def test_missing_or_blank_source_is_rejected(self):
        self.assert_invalid({"currency": "USD", "routes": [route(distance_nm={"low": 1, "high": 2})]})
        self.assert_invalid({"currency": "USD", "routes": [route(distance_nm=fig(1, 2, "   "))]})

    def test_inverted_negative_and_zero_speed_are_rejected(self):
        self.assert_invalid({"currency": "USD", "routes": [route(distance_nm=fig(5, 1))]})
        self.assert_invalid({"currency": "USD", "routes": [route(fuel_price_per_tonne=fig(-1, 1))]})
        self.assert_invalid({"currency": "USD", "routes": [route(speed_knots=fig(0, 10))]})

    def test_currency_is_required_not_defaulted(self):
        self.assert_invalid({"routes": [route()]})
        self.assert_invalid({"currency": "  ", "routes": [route()]})

    def test_missing_war_risk_transits_is_rejected(self):
        self.assert_invalid(
            {
                "currency": "USD",
                "routes": [
                    route(
                        war_risk={
                            "premium_percent_of_insured_value": fig(1, 1),
                            "insured_value": fig(100, 100),
                        }
                    )
                ],
            }
        )

    def test_premium_over_100_percent_is_rejected(self):
        self.assert_invalid(
            {
                "currency": "USD",
                "routes": [
                    route(
                        war_risk={
                            "premium_percent_of_insured_value": fig(1, 101),
                            "insured_value": fig(100, 100),
                            "transits": 1,
                        }
                    )
                ],
            }
        )

    def test_duplicate_route_names_and_unknown_baseline_are_rejected(self):
        self.assert_invalid({"currency": "USD", "routes": [route("a"), route("a")]})
        self.assert_invalid({"currency": "USD", "routes": [route("a")], "baseline_route": "z"})

    def test_empty_routes_rejected(self):
        self.assert_invalid({"currency": "USD", "routes": []})


if __name__ == "__main__":
    unittest.main()
