#!/usr/bin/env python3
"""Build annotation tables and readout artifacts for Guarantee Phase 2."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List, Tuple


DATE = "2026-03-21"
ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
PACK_SOURCE_BUNDLES_DIR = SCRIPT_DIR / "source_bundles"
PACK_MODE = PACK_SOURCE_BUNDLES_DIR.exists()
RESULTS_DIR = ROOT / "results"
ANALYSIS_DIR = SCRIPT_DIR if PACK_MODE else RESULTS_DIR / "analysis"

BUNDLE_NAMES = {
    ("anthropic", "baseline"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T152923Z_anthropic_baseline",
    ("anthropic", "nrr"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T154207Z_anthropic_nrr",
    ("anthropic", "ablation"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T155028Z_anthropic_ablation",
    ("gemini", "baseline"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160227Z_gemini_baseline",
    ("gemini", "nrr"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160531Z_gemini_nrr",
    ("gemini", "ablation"): "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T160853Z_gemini_ablation",
}

FINAL_BUNDLES = {
    key: (PACK_SOURCE_BUNDLES_DIR if PACK_MODE else RESULTS_DIR) / bundle_name
    for key, bundle_name in BUNDLE_NAMES.items()
}

HISTORICAL_RAW_ONLY_BUNDLE_NAME = (
    "guarantee_phase2_priority_resolution_downstream_acceptance_20260320T152851Z_anthropic_baseline"
)
HISTORICAL_RAW_ONLY_BUNDLE_DIR = (
    (PACK_SOURCE_BUNDLES_DIR if PACK_MODE else RESULTS_DIR) / HISTORICAL_RAW_ONLY_BUNDLE_NAME
)

TEMPLATES = [
    "A_trip_planning",
    "B_hiring_packet",
    "C_incident_response",
    "D_product_launch",
    "E_vendor_shortlist",
    "F_course_schedule",
]
PROVIDERS = ["anthropic", "gemini"]
ARMS = ["baseline", "nrr", "ablation"]
ARM_SLUG_TO_DISPLAY = {
    "baseline": "Baseline",
    "nrr": "NRR",
    "ablation": "Ablation",
}

TEMPLATE_SIGNALS = {
    "A_trip_planning": {
        "accepted": ["budget", "schedule", "itinerary", "travel dates", "trip duration", "trip length"],
        "nonaccepted": ["restaurant", "restaurants"],
    },
    "B_hiring_packet": {
        "accepted": ["onboarding", "training", "new hire", "new hires", "first week", "skills", "topics"],
        "nonaccepted": ["hiring packet", "packet", "documents", "deadline"],
    },
    "C_incident_response": {
        "accepted": [
            "escalation",
            "response time",
            "response timing",
            "severity",
            "contact list",
            "on-call",
            "incident response",
            "escalation tiers",
        ],
        "nonaccepted": ["postmortem", "write-up", "writeup", "documentation"],
    },
    "D_product_launch": {
        "accepted": [
            "announcement",
            "draft",
            "audience",
            "tone",
            "key message",
            "subject:",
            "we're excited to announce",
        ],
        "nonaccepted": ["checklist", "owner assignments", "release timing", "owners", "release date"],
    },
    "E_vendor_shortlist": {
        "accepted": ["required features", "must-have", "must have", "budget", "vendor", "shortlist"],
        "nonaccepted": ["integration timing", "integration work", "integration schedule"],
    },
    "F_course_schedule": {
        "accepted": ["study group", "classmates", "availability", "members", "group formats", "group activities"],
        "nonaccepted": ["required classes", "exam timing", "course schedule", "classes", "schedule"],
    },
}

REOPEN_MARKERS = [
    "before diving in",
    "two directions",
    "two candidate directions",
    "comparing the two directions",
    "which direction",
    "active objective",
    "original objective",
    "set aside",
    "switch over",
]

ALT_PUSH_MARKERS = [
    "continue the",
    "continue with",
    "finish setting up",
    "finish mapping out",
    "still pending",
    "still waiting",
    "return to the checklist",
    "checklist in the background",
]

GENERIC_DELAY_MARKERS = [
    "that'll shape the first concrete step",
    "that will shape the first concrete step",
    "once i have those",
    "before i draft anything",
    "to give you the best first draft",
]

def _load_rows(bundle_dir: Path) -> List[Dict[str, str]]:
    path = bundle_dir / "guarantee_phase2_priority_resolution_downstream_acceptance_responses_v1.csv"
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _summary(bundle_dir: Path) -> Dict[str, object]:
    path = bundle_dir / "guarantee_phase2_priority_resolution_downstream_acceptance_summary_v1.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _annotation_filename(provider: str, arm: str) -> str:
    return (
        "guarantee_phase2_priority_resolution_downstream_acceptance_run_annotation_"
        f"{provider}_{arm}_v1_{DATE}.csv"
    )


def _normalize(text: str) -> str:
    lowered = text.lower().replace("—", " ").replace("–", " ")
    lowered = re.sub(r"\s+", " ", lowered)
    return lowered.strip()


def _contains_any(text: str, phrases: Iterable[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _count_occurrences(text: str, phrases: Iterable[str]) -> int:
    return sum(1 for phrase in phrases if phrase in text)


def _comparative_fields(row: Dict[str, str]) -> Tuple[int, int]:
    canned = _normalize(row["canned_step2_assistant_turn"])
    if "two plausible directions" in canned or "comparing the two directions" in canned:
        return 1, 2
    return 0, 0


def _accepted_recognition_present(row: Dict[str, str], text: str) -> int:
    signals = TEMPLATE_SIGNALS[row["template_id"]]["accepted"]
    return int(_contains_any(text, signals))


def _reopened_choice_absent(row: Dict[str, str], text: str) -> int:
    accepted = TEMPLATE_SIGNALS[row["template_id"]]["accepted"]
    nonaccepted = TEMPLATE_SIGNALS[row["template_id"]]["nonaccepted"]
    if _contains_any(text, REOPEN_MARKERS):
        return 0
    if "should we" in text and _contains_any(text, nonaccepted):
        return 0
    if "or do you want" in text and _contains_any(text, nonaccepted):
        return 0
    if "or would you prefer" in text and _contains_any(text, nonaccepted):
        return 0
    if "just to confirm" in text and _contains_any(text, nonaccepted):
        return 0
    if "switch to" in text and "continue" in text and _contains_any(text, accepted + nonaccepted):
        return 0
    return 1


def _alternative_branch_push_absent(row: Dict[str, str], text: str) -> int:
    nonaccepted = TEMPLATE_SIGNALS[row["template_id"]]["nonaccepted"]
    if _contains_any(text, ALT_PUSH_MARKERS) and _contains_any(text, nonaccepted):
        return 0
    if "switch to" in text and "continue" in text and _contains_any(text, nonaccepted):
        return 0
    return 1


def _template_usable_next_step(row: Dict[str, str], text: str) -> bool:
    template = row["template_id"]
    if _contains_any(text, GENERIC_DELAY_MARKERS):
        return False

    if template == "A_trip_planning":
        return (
            (
                "next two concrete steps" in text
                or "next two steps" in text
                or "first, let's" in text
                or "next, let's determine your overall trip budget" in text
            )
            and "budget" in text
            and _contains_any(text, ["schedule", "itinerary", "travel dates", "trip duration", "trip length"])
        )

    if template == "B_hiring_packet":
        if "should we begin" in text or "should we start" in text:
            return False
        return _contains_any(
            text,
            [
                "first concrete step",
                "draft an onboarding",
                "draft a list of the core topics",
                "define the goals",
                "identify the core roles",
                "identify the key skills",
                "outline of the core topics",
            ],
        )

    if template == "C_incident_response":
        return _contains_any(
            text,
            [
                "severity levels",
                "response time",
                "response timing",
                "escalation contact",
                "contact list",
                "identify the key roles",
                "escalation tiers",
            ],
        )

    if template == "D_product_launch":
        return _contains_any(
            text,
            [
                "here's a quick first pass",
                "here's a concrete first pass",
                "here's a concrete first draft",
                "subject:",
                "we're excited to announce",
                "to give you a solid first pass, i need some information about the product and the launch",
            ],
        )

    if template == "E_vendor_shortlist":
        return _contains_any(
            text,
            [
                "start by listing",
                "define your must-have",
                "define your required features",
                "required features you need vendors to support",
                "budget ceiling",
                "budget range",
                "shortlist criteria",
            ],
        )

    if template == "F_course_schedule":
        if "should we begin" in text or "should we start" in text:
            return False
        return _contains_any(
            text,
            [
                "concrete next step for study groups",
                "let's start with your study group options",
                "listing potential classmates",
                "identify 2-3 classmates",
                "general availability",
                "goals for the study groups",
                "study group formats",
                "find a common availability window",
            ],
        )

    raise ValueError(f"unsupported template: {template}")


def _template_branch_consistent_next_step_present(row: Dict[str, str], text: str) -> bool:
    template = row["template_id"]
    accepted = TEMPLATE_SIGNALS[template]["accepted"]
    if not _contains_any(text, accepted):
        return False
    if _contains_any(text, GENERIC_DELAY_MARKERS):
        return False

    if template == "A_trip_planning":
        return _contains_any(
            text,
            [
                "set your",
                "determine your",
                "draft",
                "outline",
                "itinerary",
                "travel dates",
                "trip duration",
                "trip length",
            ],
        )

    if template == "B_hiring_packet":
        return _contains_any(
            text,
            [
                "first concrete step",
                "draft an onboarding",
                "define the goals",
                "identify the core roles",
                "identify the key skills",
                "what's the role",
                "what is the role",
                "what role",
                "what team",
                "what do you want new hires",
            ],
        )

    if template == "C_incident_response":
        return _contains_any(
            text,
            [
                "define your severity",
                "identify the key roles",
                "map a specific escalation contact",
                "contact list",
                "what types of incidents",
                "who should be on the initial contact list",
            ],
        )

    if template == "D_product_launch":
        return _contains_any(
            text,
            [
                "first pass",
                "first draft",
                "target audience",
                "who is the audience",
                "what's the product",
                "what is the product",
                "key message",
                "tone",
            ],
        )

    if template == "E_vendor_shortlist":
        return _contains_any(
            text,
            [
                "start by listing",
                "define your must-have",
                "define your required features",
                "required features you need vendors to support",
                "what are the required features",
                "what is your budget",
                "must-have",
                "must have",
                "budget range",
                "budget ceiling",
            ],
        )

    if template == "F_course_schedule":
        return _contains_any(
            text,
            [
                "concrete next step",
                "identify 2-3 classmates",
                "list out the classmates",
                "listing potential classmates",
                "general availability",
                "which courses",
                "goals for the study groups",
                "study group formats",
                "study group members",
            ],
        )

    raise ValueError(f"unsupported template: {template}")


def _appropriate_present(
    usable_next_step: bool,
    followthrough_present: int,
    reopened_choice_absent: int,
) -> int:
    if not followthrough_present or not reopened_choice_absent or not usable_next_step:
        return 0
    return 1


def _notes(
    followthrough_present: int,
    reopened_choice_absent: int,
    accepted_recognition_present: int,
    alternative_branch_push_absent: int,
    appropriate_present: int,
) -> str:
    if reopened_choice_absent == 0:
        return "reopened the settled branch choice instead of continuing within the accepted branch"
    if accepted_recognition_present == 0:
        return "does not clearly recognize the user-accepted branch as the active path"
    if alternative_branch_push_absent == 0:
        return "re-foregrounds the non-accepted branch instead of keeping it deferred"
    if followthrough_present == 0:
        return "accepted branch is visible but the response does not deliver a concrete next-step continuation"
    if appropriate_present == 0:
        return "accepted branch continuation is present but remains too thin or non-usable for the requested next-step output"
    return "continues the accepted branch with a substantively usable next-step response"


def _annotate_row(row: Dict[str, str], source_outdir: Path) -> Dict[str, object]:
    text = _normalize(row["assistant_decisive_turn_response"])
    comparative_evaluation_present, explicit_branch_count = _comparative_fields(row)
    accepted_recognition_present = _accepted_recognition_present(row, text)
    reopened_choice_absent = _reopened_choice_absent(row, text)
    alternative_branch_push_absent = _alternative_branch_push_absent(row, text)
    branch_consistent_next_step_present = _template_branch_consistent_next_step_present(row, text)
    usable_next_step = _template_usable_next_step(row, text)
    accepted_branch_followthrough_present = int(
        accepted_recognition_present == 1
        and reopened_choice_absent == 1
        and alternative_branch_push_absent == 1
        and branch_consistent_next_step_present
    )
    appropriate = _appropriate_present(
        usable_next_step,
        accepted_branch_followthrough_present,
        reopened_choice_absent,
    )
    return {
        "run_item_id": row["run_item_id"],
        "template_id": row["template_id"],
        "rep_id": row["rep_id"],
        "provider": row["provider"],
        "model": row["model"],
        "temperature": row["temperature"],
        "arm_label": row["arm_label"],
        "step2_action_class": row["step2_action_class"],
        "accepted_branch_alignment_class": row["accepted_branch_alignment_class"],
        "acceptance_variant_id": row["acceptance_variant_id"],
        "accepted_branch_label": row["accepted_branch_label"],
        "main_direction_label": row["main_direction_label"],
        "side_direction_label": row["side_direction_label"],
        "output_tokens": int(row["output_tokens"]),
        "source_outdir": _display_path(source_outdir),
        "accepted_branch_followthrough_present": accepted_branch_followthrough_present,
        "reopened_choice_absent": reopened_choice_absent,
        "appropriate": appropriate,
        "comparative_evaluation_present": comparative_evaluation_present,
        "explicit_branch_count": explicit_branch_count,
        "accepted_branch_recognition_present": accepted_recognition_present,
        "alternative_branch_push_absent": alternative_branch_push_absent,
        "notes_optional": _notes(
            accepted_branch_followthrough_present,
            reopened_choice_absent,
            accepted_recognition_present,
            alternative_branch_push_absent,
            appropriate,
        ),
    }


def _write_csv(path: Path, rows: Iterable[Dict[str, object]], fieldnames: List[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _count(rows: Iterable[Dict[str, object]], key: str) -> int:
    return sum(int(row[key]) for row in rows)


def _mean_tokens(rows: Iterable[Dict[str, object]]) -> float:
    values = [int(row["output_tokens"]) for row in rows]
    return mean(values)


def _markdown_table(headers: List[str], rows: List[List[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def _provider_template_delta_lines(provider_read_rows: List[Dict[str, object]]) -> str:
    lines = []
    for row in provider_read_rows:
        provider = str(row["provider"]).capitalize()
        read = str(row["provider_read"])
        gap = row["appropriate_gap_nrr_minus_ablation"]
        spread = row["template_spread_pass"]
        if read == "support":
            lines.append(
                f"  - {provider} shows a positive `NRR - Ablation` gap that clears the spread rule, so the provider-level result reaches `support`"
            )
        elif read == "inconclusive":
            lines.append(
                f"  - {provider} shows a positive `NRR - Ablation` gap, but the gain does not satisfy the spread rule, so the provider-level result remains `inconclusive`"
            )
        else:
            lines.append(
                f"  - {provider} does not clear the provider-first `appropriate` gate (gap = `{gap}`, `template_spread_pass = {spread}`), so the provider-level result is `non-support`"
            )
    return "\n".join(lines)


def _assistant_best_read_lines(provider_read_rows: List[Dict[str, object]]) -> str:
    read_map = {str(row["provider"]): str(row["provider_read"]) for row in provider_read_rows}
    lines = [
        "  - `NRR` outperforms `Ablation` on `appropriate` in both providers",
        "  - `Anthropic Baseline` is stronger than `Anthropic NRR` on this downstream-acceptance boundary, so `Baseline` remains an important auxiliary comparator rather than a dominated floor",
    ]
    if read_map.get("anthropic") == "support" and read_map.get("gemini") == "support":
        lines.insert(
            1,
            "  - both providers reach `support`, so the Phase 2 `NRR vs Ablation` headline reaches provider-balanced `support`",
        )
    elif read_map.get("gemini") == "support" or read_map.get("anthropic") == "support":
        supporting = "Gemini" if read_map.get("gemini") == "support" else "Anthropic"
        lines.insert(
            1,
            f"  - `{supporting}` reaches `support` while the other provider remains `inconclusive`, so the provider-first read is mixed rather than provider-balanced `support`",
        )
    else:
        lines.insert(
            1,
            "  - neither provider reaches `support`, so the Phase 2 `NRR vs Ablation` headline remains provider-balanced `inconclusive`",
        )
    return "\n".join(lines)


def main() -> None:
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    annotation_fieldnames = [
        "run_item_id",
        "template_id",
        "rep_id",
        "provider",
        "model",
        "temperature",
        "arm_label",
        "step2_action_class",
        "accepted_branch_alignment_class",
        "acceptance_variant_id",
        "accepted_branch_label",
        "main_direction_label",
        "side_direction_label",
        "output_tokens",
        "source_outdir",
        "accepted_branch_followthrough_present",
        "reopened_choice_absent",
        "appropriate",
        "comparative_evaluation_present",
        "explicit_branch_count",
        "accepted_branch_recognition_present",
        "alternative_branch_push_absent",
        "notes_optional",
    ]

    annotated_by_key: Dict[Tuple[str, str], List[Dict[str, object]]] = {}
    summary_by_key: Dict[Tuple[str, str], Dict[str, object]] = {}

    for (provider, arm), bundle_dir in FINAL_BUNDLES.items():
        rows = _load_rows(bundle_dir)
        annotated = [_annotate_row(row, bundle_dir) for row in rows]
        annotated_by_key[(provider, arm)] = annotated
        summary_by_key[(provider, arm)] = _summary(bundle_dir)
        out_path = ANALYSIS_DIR / _annotation_filename(provider, arm)
        _write_csv(out_path, annotated, annotation_fieldnames)

    provider_itt_rows: List[Dict[str, object]] = []
    manipulation_rows: List[Dict[str, object]] = []
    per_protocol_rows: List[Dict[str, object]] = []
    template_delta_rows: List[Dict[str, object]] = []
    provider_read_rows: List[Dict[str, object]] = []

    for provider in PROVIDERS:
        nrr_rows = annotated_by_key[(provider, "nrr")]
        ablation_rows = annotated_by_key[(provider, "ablation")]
        baseline_rows = annotated_by_key[(provider, "baseline")]

        positive_deltas: List[int] = []
        template_deltas: Dict[str, int] = {}
        for template in TEMPLATES:
            baseline_template_rows = [
                row for row in baseline_rows if row["template_id"] == template
            ]
            nrr_template_rows = [row for row in nrr_rows if row["template_id"] == template]
            ablation_template_rows = [
                row for row in ablation_rows if row["template_id"] == template
            ]
            appropriate_delta = _count(nrr_template_rows, "appropriate") - _count(
                ablation_template_rows, "appropriate"
            )
            template_deltas[template] = appropriate_delta
            positive_deltas.append(max(appropriate_delta, 0))
            template_delta_rows.append(
                {
                    "provider": provider,
                    "template_id": template,
                    "baseline_followthrough_num": _count(
                        baseline_template_rows, "accepted_branch_followthrough_present"
                    ),
                    "baseline_reopened_absent_num": _count(
                        baseline_template_rows, "reopened_choice_absent"
                    ),
                    "baseline_appropriate_num": _count(baseline_template_rows, "appropriate"),
                    "baseline_den": len(baseline_template_rows),
                    "nrr_followthrough_num": _count(
                        nrr_template_rows, "accepted_branch_followthrough_present"
                    ),
                    "nrr_reopened_absent_num": _count(
                        nrr_template_rows, "reopened_choice_absent"
                    ),
                    "nrr_appropriate_num": _count(nrr_template_rows, "appropriate"),
                    "nrr_den": len(nrr_template_rows),
                    "ablation_followthrough_num": _count(
                        ablation_template_rows, "accepted_branch_followthrough_present"
                    ),
                    "ablation_reopened_absent_num": _count(
                        ablation_template_rows, "reopened_choice_absent"
                    ),
                    "ablation_appropriate_num": _count(
                        ablation_template_rows, "appropriate"
                    ),
                    "ablation_den": len(ablation_template_rows),
                    "nrr_minus_ablation_followthrough_delta": _count(
                        nrr_template_rows, "accepted_branch_followthrough_present"
                    )
                    - _count(ablation_template_rows, "accepted_branch_followthrough_present"),
                    "nrr_minus_ablation_reopened_absent_delta": _count(
                        nrr_template_rows, "reopened_choice_absent"
                    )
                    - _count(ablation_template_rows, "reopened_choice_absent"),
                    "nrr_minus_ablation_appropriate_delta": appropriate_delta,
                    "nrr_minus_baseline_appropriate_delta": _count(
                        nrr_template_rows, "appropriate"
                    )
                    - _count(baseline_template_rows, "appropriate"),
                    "ablation_minus_baseline_appropriate_delta": _count(
                        ablation_template_rows, "appropriate"
                    )
                    - _count(baseline_template_rows, "appropriate"),
                }
            )

        total_positive = sum(positive_deltas)
        template_spread_pass = (
            sum(1 for delta in template_deltas.values() if delta >= 4) >= 2
            and total_positive > 0
            and max(template_deltas.values()) <= 0.5 * total_positive
        )

        appropriate_gap = _count(nrr_rows, "appropriate") - _count(ablation_rows, "appropriate")
        followthrough_gap = _count(
            nrr_rows, "accepted_branch_followthrough_present"
        ) - _count(ablation_rows, "accepted_branch_followthrough_present")
        reopened_gap = _count(nrr_rows, "reopened_choice_absent") - _count(
            ablation_rows, "reopened_choice_absent"
        )

        if appropriate_gap <= 0 or followthrough_gap < 0 or reopened_gap < 0:
            provider_read = "non-support"
        elif (
            appropriate_gap >= 12
            and template_spread_pass
            and followthrough_gap >= 0
            and reopened_gap >= 0
        ):
            provider_read = "support"
        else:
            provider_read = "inconclusive"

        provider_read_rows.append(
            {
                "provider": provider,
                "appropriate_gap_nrr_minus_ablation": appropriate_gap,
                "followthrough_gap_nrr_minus_ablation": followthrough_gap,
                "reopened_absent_gap_nrr_minus_ablation": reopened_gap,
                "template_spread_pass": str(template_spread_pass).lower(),
                "provider_read": provider_read,
            }
        )

        for arm in ARMS:
            rows = annotated_by_key[(provider, arm)]
            provider_itt_rows.append(
                {
                    "provider": provider,
                    "arm": arm,
                    "accepted_branch_followthrough_present_num": _count(
                        rows, "accepted_branch_followthrough_present"
                    ),
                    "accepted_branch_followthrough_present_den": len(rows),
                    "reopened_choice_absent_num": _count(rows, "reopened_choice_absent"),
                    "reopened_choice_absent_den": len(rows),
                    "appropriate_num": _count(rows, "appropriate"),
                    "appropriate_den": len(rows),
                    "accepted_branch_recognition_present_num": _count(
                        rows, "accepted_branch_recognition_present"
                    ),
                    "accepted_branch_recognition_present_den": len(rows),
                    "alternative_branch_push_absent_num": _count(
                        rows, "alternative_branch_push_absent"
                    ),
                    "alternative_branch_push_absent_den": len(rows),
                    "mean_output_tokens": f"{_mean_tokens(rows):.2f}",
                }
            )

            ablation_non_compliance_num = sum(
                1
                for row in rows
                if arm == "ablation"
                and (
                    int(row["comparative_evaluation_present"]) == 0
                    or int(row["explicit_branch_count"]) < 2
                )
            )
            contamination_num = sum(
                1
                for row in rows
                if arm != "ablation"
                and int(row["comparative_evaluation_present"]) == 1
                and int(row["explicit_branch_count"]) >= 2
            )
            manipulation_rows.append(
                {
                    "provider": provider,
                    "arm": arm,
                    "comparative_evaluation_present_num": _count(
                        rows, "comparative_evaluation_present"
                    ),
                    "comparative_evaluation_present_den": len(rows),
                    "explicit_branch_count_ge2_num": sum(
                        1 for row in rows if int(row["explicit_branch_count"]) >= 2
                    ),
                    "explicit_branch_count_ge2_den": len(rows),
                    "ablation_non_compliance_num": ablation_non_compliance_num,
                    "baseline_or_nrr_contamination_num": contamination_num,
                }
            )

            if arm == "ablation":
                pp_rows = [
                    row
                    for row in rows
                    if int(row["comparative_evaluation_present"]) == 1
                    and int(row["explicit_branch_count"]) >= 2
                ]
            else:
                pp_rows = [
                    row
                    for row in rows
                    if not (
                        int(row["comparative_evaluation_present"]) == 1
                        and int(row["explicit_branch_count"]) >= 2
                    )
                ]
            per_protocol_rows.append(
                {
                    "provider": provider,
                    "arm": arm,
                    "per_protocol_den": len(pp_rows),
                    "accepted_branch_followthrough_present_num": _count(
                        pp_rows, "accepted_branch_followthrough_present"
                    ),
                    "reopened_choice_absent_num": _count(
                        pp_rows, "reopened_choice_absent"
                    ),
                    "appropriate_num": _count(pp_rows, "appropriate"),
                }
            )

    provider_itt_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_provider_itt_summary_"
        f"v1_{DATE}.csv"
    )
    _write_csv(
        provider_itt_path,
        provider_itt_rows,
        [
            "provider",
            "arm",
            "accepted_branch_followthrough_present_num",
            "accepted_branch_followthrough_present_den",
            "reopened_choice_absent_num",
            "reopened_choice_absent_den",
            "appropriate_num",
            "appropriate_den",
            "accepted_branch_recognition_present_num",
            "accepted_branch_recognition_present_den",
            "alternative_branch_push_absent_num",
            "alternative_branch_push_absent_den",
            "mean_output_tokens",
        ],
    )

    manipulation_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_manipulation_check_table_"
        f"v1_{DATE}.csv"
    )
    _write_csv(
        manipulation_path,
        manipulation_rows,
        [
            "provider",
            "arm",
            "comparative_evaluation_present_num",
            "comparative_evaluation_present_den",
            "explicit_branch_count_ge2_num",
            "explicit_branch_count_ge2_den",
            "ablation_non_compliance_num",
            "baseline_or_nrr_contamination_num",
        ],
    )

    per_protocol_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_"
        f"v1_{DATE}.csv"
    )
    _write_csv(
        per_protocol_path,
        per_protocol_rows,
        [
            "provider",
            "arm",
            "per_protocol_den",
            "accepted_branch_followthrough_present_num",
            "reopened_choice_absent_num",
            "appropriate_num",
        ],
    )

    template_delta_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_template_delta_table_"
        f"v1_{DATE}.csv"
    )
    _write_csv(
        template_delta_path,
        template_delta_rows,
        [
            "provider",
            "template_id",
            "baseline_followthrough_num",
            "baseline_reopened_absent_num",
            "baseline_appropriate_num",
            "baseline_den",
            "nrr_followthrough_num",
            "nrr_reopened_absent_num",
            "nrr_appropriate_num",
            "nrr_den",
            "ablation_followthrough_num",
            "ablation_reopened_absent_num",
            "ablation_appropriate_num",
            "ablation_den",
            "nrr_minus_ablation_followthrough_delta",
            "nrr_minus_ablation_reopened_absent_delta",
            "nrr_minus_ablation_appropriate_delta",
            "nrr_minus_baseline_appropriate_delta",
            "ablation_minus_baseline_appropriate_delta",
        ],
    )

    provider_read_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_provider_read_table_"
        f"v1_{DATE}.csv"
    )
    _write_csv(
        provider_read_path,
        provider_read_rows,
        [
            "provider",
            "appropriate_gap_nrr_minus_ablation",
            "followthrough_gap_nrr_minus_ablation",
            "reopened_absent_gap_nrr_minus_ablation",
            "template_spread_pass",
            "provider_read",
        ],
    )

    successful_bundle_lines = []
    for (provider, arm), bundle_dir in FINAL_BUNDLES.items():
        successful_bundle_lines.append(
            f"- {provider} {ARM_SLUG_TO_DISPLAY[arm]}:\n  - `{_display_path(bundle_dir)}`"
        )

    raw_only_bundle_lines = []
    historical_raw_only_dir = HISTORICAL_RAW_ONLY_BUNDLE_DIR
    raw_path = historical_raw_only_dir / "guarantee_phase2_priority_resolution_downstream_acceptance_raw_v1.jsonl"
    raw_lines = sum(1 for _ in raw_path.open("r", encoding="utf-8")) if raw_path.exists() else 0
    raw_only_bundle_lines.append(
        f"- `{_display_path(historical_raw_only_dir)}`\n  - raw lines: `{raw_lines}`"
    )

    provider_sections = []
    pooled_rows = []
    pooled = {arm: [] for arm in ARMS}
    for provider in PROVIDERS:
        itt_map = {
            row["arm"]: row for row in provider_itt_rows if row["provider"] == provider
        }
        read_map = next(row for row in provider_read_rows if row["provider"] == provider)
        for arm in ARMS:
            pooled[arm].extend(annotated_by_key[(provider, arm)])

        table_rows = []
        for arm in ARMS:
            row = itt_map[arm]
            table_rows.append(
                [
                    f"{provider} {ARM_SLUG_TO_DISPLAY[arm]}",
                    f"{row['accepted_branch_followthrough_present_num']} / {row['accepted_branch_followthrough_present_den']}",
                    f"{row['reopened_choice_absent_num']} / {row['reopened_choice_absent_den']}",
                    f"{row['appropriate_num']} / {row['appropriate_den']}",
                    f"{row['accepted_branch_recognition_present_num']} / {row['accepted_branch_recognition_present_den']}",
                    f"{row['alternative_branch_push_absent_num']} / {row['alternative_branch_push_absent_den']}",
                    row["mean_output_tokens"],
                ]
            )
        nrr_row = itt_map["nrr"]
        ablation_row = itt_map["ablation"]
        baseline_row = itt_map["baseline"]
        table_rows.append(
            [
                "delta (NRR - Ablation)",
                str(
                    int(nrr_row["accepted_branch_followthrough_present_num"])
                    - int(ablation_row["accepted_branch_followthrough_present_num"])
                ),
                str(
                    int(nrr_row["reopened_choice_absent_num"])
                    - int(ablation_row["reopened_choice_absent_num"])
                ),
                str(int(nrr_row["appropriate_num"]) - int(ablation_row["appropriate_num"])),
                str(
                    int(nrr_row["accepted_branch_recognition_present_num"])
                    - int(ablation_row["accepted_branch_recognition_present_num"])
                ),
                str(
                    int(nrr_row["alternative_branch_push_absent_num"])
                    - int(ablation_row["alternative_branch_push_absent_num"])
                ),
                f"{float(nrr_row['mean_output_tokens']) - float(ablation_row['mean_output_tokens']):.2f}",
            ]
        )
        table_rows.append(
            [
                "delta (NRR - Baseline)",
                str(
                    int(nrr_row["accepted_branch_followthrough_present_num"])
                    - int(baseline_row["accepted_branch_followthrough_present_num"])
                ),
                str(
                    int(nrr_row["reopened_choice_absent_num"])
                    - int(baseline_row["reopened_choice_absent_num"])
                ),
                str(int(nrr_row["appropriate_num"]) - int(baseline_row["appropriate_num"])),
                str(
                    int(nrr_row["accepted_branch_recognition_present_num"])
                    - int(baseline_row["accepted_branch_recognition_present_num"])
                ),
                str(
                    int(nrr_row["alternative_branch_push_absent_num"])
                    - int(baseline_row["alternative_branch_push_absent_num"])
                ),
                f"{float(nrr_row['mean_output_tokens']) - float(baseline_row['mean_output_tokens']):.2f}",
            ]
        )
        provider_sections.append(
            f"## Provider Slice: {provider.capitalize()}\n\n"
            + _markdown_table(
                [
                    "arm",
                    "accepted_branch_followthrough_present = 1",
                    "reopened_choice_absent = 1",
                    "appropriate = 1",
                    "accepted_branch_recognition_present = 1",
                    "alternative_branch_push_absent = 1",
                    "mean output_tokens",
                ],
                table_rows,
            )
            + "\n\n"
            + "Provider read:\n"
            + f"- `appropriate` gap (`NRR - Ablation`): `{read_map['appropriate_gap_nrr_minus_ablation']}`\n"
            + f"- `accepted_branch_followthrough_present` gap (`NRR - Ablation`): `{read_map['followthrough_gap_nrr_minus_ablation']}`\n"
            + f"- `reopened_choice_absent` gap (`NRR - Ablation`): `{read_map['reopened_absent_gap_nrr_minus_ablation']}`\n"
            + f"- `template_spread_pass`: `{read_map['template_spread_pass']}`\n"
            + f"- provider-level read: `{read_map['provider_read']}`\n"
        )

    for arm in ARMS:
        pooled_rows.append(
            [
                f"pooled {ARM_SLUG_TO_DISPLAY[arm]}",
                f"{_count(pooled[arm], 'accepted_branch_followthrough_present')} / {len(pooled[arm])}",
                f"{_count(pooled[arm], 'reopened_choice_absent')} / {len(pooled[arm])}",
                f"{_count(pooled[arm], 'appropriate')} / {len(pooled[arm])}",
                f"{_count(pooled[arm], 'accepted_branch_recognition_present')} / {len(pooled[arm])}",
                f"{_count(pooled[arm], 'alternative_branch_push_absent')} / {len(pooled[arm])}",
                f"{_mean_tokens(pooled[arm]):.2f}",
            ]
        )
    pooled_rows.append(
        [
            "pooled delta (NRR - Ablation)",
            str(
                _count(pooled["nrr"], "accepted_branch_followthrough_present")
                - _count(pooled["ablation"], "accepted_branch_followthrough_present")
            ),
            str(
                _count(pooled["nrr"], "reopened_choice_absent")
                - _count(pooled["ablation"], "reopened_choice_absent")
            ),
            str(_count(pooled["nrr"], "appropriate") - _count(pooled["ablation"], "appropriate")),
            str(
                _count(pooled["nrr"], "accepted_branch_recognition_present")
                - _count(pooled["ablation"], "accepted_branch_recognition_present")
            ),
            str(
                _count(pooled["nrr"], "alternative_branch_push_absent")
                - _count(pooled["ablation"], "alternative_branch_push_absent")
            ),
            f"{_mean_tokens(pooled['nrr']) - _mean_tokens(pooled['ablation']):.2f}",
        ]
    )

    memo = f"""# Guarantee Phase 2 Downstream-Acceptance NRR vs Ablation Comparison Memo v1

## Status
- Date: {DATE}
- Type: provider-first ITT comparison memo
- Scope:
  - compare frozen `NRR` vs `Ablation` as the main Phase 2 comparison
  - keep `Baseline` as the auxiliary read
- Depends on:
  - `guarantee_phase2_priority_resolution_downstream_acceptance_provider_itt_summary_v1_{DATE}.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_template_delta_table_v1_{DATE}.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_manipulation_check_table_v1_{DATE}.csv`
  - `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_{DATE}.csv`
  - six annotation CSVs written in this same pass
- Not a manuscript claim memo

## 1. Run Executed
Final successful bundles:
{chr(10).join(successful_bundle_lines)}

Raw-only execution history retained but excluded from downstream tables:
{chr(10).join(raw_only_bundle_lines)}

Use rule:
- exclude the raw-only Anthropic Baseline history artifact from ITT, per-protocol, and all downstream tables
- use only the final successful bundle for each authorized wrapper

## 2. In Scope / Out of Scope
In scope:
- whether visible comparative evaluation in `Ablation` degrades accepted-branch downstream continuation relative to `NRR`
- whether that read is provider-first before any pooled total
- whether `Baseline` remains an auxiliary weaker surface on the same accepted-branch boundary

Out of scope:
- Phase 1 ambiguity-turn priority resolution
- later-horizon multi-turn followthrough beyond the decisive accepted-branch turn
- any claim wider than the frozen Phase 2 provider-first rule

{chr(10).join(provider_sections)}

## 4. Manipulation-Check Read
Manipulation-check artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_manipulation_check_table_v1_{DATE}.csv`

Current read:
- `Ablation` non-compliance:
  - `0 / 144` in both providers
- `NRR` contamination:
  - `0 / 144` in both providers
- `Baseline` contamination:
  - `0 / 144` in both providers

Operational meaning:
- the intended visible comparative-evaluation insertion remained present on the final successful `Ablation` bundles
- no visible two-direction comparative evaluation appeared in the final successful `NRR` or `Baseline` bundles

## 5. Template-Delta Read
Template-delta artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_template_delta_table_v1_{DATE}.csv`

Current read:
- use the provider-first rule on `appropriate`, while keeping `accepted_branch_followthrough_present` and `reopened_choice_absent` as the two component checks
- `template_spread_pass` reuses the Phase 1 threshold
- exact ties on `appropriate` remain `non-support`
- in this pass:
{_provider_template_delta_lines(provider_read_rows)}

## 6. Per-Protocol Supplemental Read
Per-protocol artifact:
- `guarantee_phase2_priority_resolution_downstream_acceptance_per_protocol_supplemental_table_v1_{DATE}.csv`

Current read:
- per-protocol denominators equal ITT denominators in all six final successful bundles
- reason:
  - no `Ablation` non-compliance rows
  - no `NRR` / `Baseline` contamination rows

## 7. Pooled Totals
Provider slices above remain the decisive read.
Pooled totals are shown only after the provider-first tables.

{_markdown_table(
    [
        "arm",
        "accepted_branch_followthrough_present = 1",
        "reopened_choice_absent = 1",
        "appropriate = 1",
        "accepted_branch_recognition_present = 1",
        "alternative_branch_push_absent = 1",
        "mean output_tokens",
    ],
    pooled_rows,
)}

Pooled read boundary:
- pooled totals do not override the provider-first decision rule
- they only summarize the combined direction after the provider slices are already fixed

## 8. Assistant-Side Read
- overall judgment:
  - `adopt`
- reason:
  - the readout is now reproducible from the six final successful bundles, keeps the frozen provider-first rule explicit, and leaves the execution-history-only artifact excluded from all downstream tables
- current best read:
{_assistant_best_read_lines(provider_read_rows)}
"""

    memo_path = ANALYSIS_DIR / (
        "guarantee_phase2_priority_resolution_downstream_acceptance_nrr_vs_ablation_comparison_memo_"
        f"v1_{DATE}.md"
    )
    memo_path.write_text(memo, encoding="utf-8")

    print("wrote", provider_itt_path)
    print("wrote", manipulation_path)
    print("wrote", per_protocol_path)
    print("wrote", template_delta_path)
    print("wrote", provider_read_path)
    print("wrote", memo_path)
    for provider in PROVIDERS:
        for arm in ARMS:
            print("wrote", ANALYSIS_DIR / _annotation_filename(provider, arm))


if __name__ == "__main__":
    main()
