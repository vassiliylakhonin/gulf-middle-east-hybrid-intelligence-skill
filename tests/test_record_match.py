"""Overlap and refusal tests for the entity record comparison."""

import json
import unittest

from gulf_middle_east_compliance_server.record_match import compare_records_json


def run(a, b, **extra):
    return json.loads(compare_records_json({"record_a": a, "record_b": b, **extra}))


def rec(label, **fields):
    return {"label": label, "source": f"extract for {label}", **fields}


class OverlapTests(unittest.TestCase):
    def test_exact_matches_after_normalisation(self):
        out = run(
            rec(
                "old",
                names=["Al-Noor Trading LLC"],
                addresses=["Office 12, Tower B, Dubai"],
                phones=["+971 4 123 4567"],
                emails=["Info@Example.com"],
                websites=["https://www.example.com/"],
                directors=["Ali  Hassan"],
            ),
            rec(
                "new",
                names=["AL NOOR TRADING LLC"],
                addresses=["office 12 tower b dubai"],
                phones=["00971-4-123-4567", "+971 50 000 0000"],
                emails=["info@example.com"],
                websites=["example.com"],
                directors=["ali hassan"],
            ),
        )
        self.assertEqual(out["status"], "match_report")
        by_field = {f["field"]: f for f in out["fields"]}
        for field in ("names", "addresses", "emails", "websites", "directors"):
            self.assertEqual(len(by_field[field]["exact_matches"]), 1, field)
        # +971 vs 00971 differ as digit strings: not matched, not guessed
        self.assertEqual(by_field["phones"]["exact_matches"], [])
        self.assertEqual(out["summary"]["exact_match_count"], 5)
        self.assertTrue(out["result_is_not_a_finding"])
        self.assertTrue(out["human_review_required"])

    def test_phone_digits_match_and_short_numbers_are_unusable(self):
        out = run(
            rec("a", phones=["(971) 4-123-4567", "123"]),
            rec("b", phones=["971 4 123 4567"]),
        )
        phones = out["fields"][0]
        self.assertEqual(len(phones["exact_matches"]), 1)
        self.assertEqual(phones["unusable_values"]["a"], ["123"])

    def test_no_match_is_reported_without_conclusion(self):
        out = run(rec("a", names=["Alpha"]), rec("b", names=["Beta"]))
        self.assertEqual(out["summary"]["exact_match_count"], 0)
        self.assertIn("not evidence", out["detail"])

    def test_field_absent_on_both_sides_is_not_compared(self):
        out = run(rec("a", names=["x"]), rec("b", names=["y"]))
        self.assertEqual(out["summary"]["fields_compared"], ["names"])

    def test_cross_field_person_matches_only(self):
        out = run(
            rec("a", directors=["Omar Khalid"], names=["Omar Khalid"]),
            rec("b", registered_agents=["omar khalid"], names=["Zed"]),
        )
        self.assertEqual(len(out["cross_field_matches"]), 1)
        self.assertEqual(out["summary"]["cross_field_match_count"], 1)
        # a name field is not a person field, so the entity name does not cross-match
        self.assertEqual(len(out["cross_field_matches"]), 1)

    def test_near_matches_only_with_caller_threshold(self):
        a = rec("a", addresses=["Office 12 Tower B Dubai"])
        b = rec("b", addresses=["Office 12 Tower B Dubai Marina"])
        without = run(a, b)
        self.assertNotIn("near_matches", without["fields"][0])
        with_t = run(a, b, near_match_token_overlap=0.8)
        near = with_t["fields"][0]["near_matches"]
        self.assertEqual(len(near), 1)
        self.assertEqual(near[0]["token_overlap"], 0.833)
        high = run(a, b, near_match_token_overlap=0.9)
        self.assertEqual(high["fields"][0]["near_matches"], [])

    def test_output_never_states_a_network_conclusion(self):
        out = run(rec("a", addresses=["x y"]), rec("b", addresses=["x y"]))
        text = json.dumps(out).lower()
        for word in ("same network is", "is the same", "reconstituted:", "confirmed", "sanctioned:"):
            self.assertNotIn(word, text)
        self.assertIn("weak", out["fields"][0]["note"])

    def test_non_ascii_values_are_preserved_and_matched(self):
        out = run(rec("a", names=["Шамс Аль-Нур"]), rec("b", names=["шамс аль нур"]))
        self.assertEqual(out["summary"]["exact_match_count"], 1)


class RefusalTests(unittest.TestCase):
    def assert_invalid(self, a, b, **extra):
        out = run(a, b, **extra)
        self.assertEqual(out["status"], "invalid_input")
        self.assertTrue(out["result_is_not_a_finding"])
        self.assertTrue(out["human_review_required"])
        self.assertNotIn("fields", out)

    def test_missing_or_blank_source_is_rejected(self):
        ok = rec("b", names=["x"])
        self.assert_invalid({"label": "a", "names": ["x"]}, ok)
        self.assert_invalid({"label": "a", "source": "  ", "names": ["x"]}, ok)

    def test_empty_record_is_rejected(self):
        self.assert_invalid(rec("a"), rec("b", names=["x"]))
        self.assert_invalid(rec("a", names=[]), rec("b", names=["x"]))

    def test_same_labels_and_unknown_fields_are_rejected(self):
        self.assert_invalid(rec("a", names=["x"]), rec("a", names=["x"]))
        self.assert_invalid(rec("a", names=["x"], risk_score=9), rec("b", names=["x"]))

    def test_bad_threshold_is_rejected(self):
        for value in (0, 1.5, -1):
            self.assert_invalid(rec("a", names=["x"]), rec("b", names=["x"]), near_match_token_overlap=value)


if __name__ == "__main__":
    unittest.main()
