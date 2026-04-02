#!/usr/bin/env python3
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "manuscript" / "figures"


GREEN = "#2D6A4F"
GREEN_FILL = "#DDEFE6"
AMBER = "#B7791F"
AMBER_FILL = "#F9E5BF"
RED = "#B42318"
RED_FILL = "#F8D6D2"
BLUE_FILL = "#DCEBFA"
GRAY = "#667085"
LIGHT = "#F5F7FA"
LINE = "#344054"


def setup(ax, xlim=(0, 14), ylim=(0, 10)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")


def box(ax, x, y, w, h, title, body_lines, edge=LINE, face="white", title_size=12, body_size=9):
    ax.add_patch(Rectangle((x, y), w, h, linewidth=2, edgecolor=edge, facecolor=face))
    ax.text(x + 0.2, y + h - 0.35, title, ha="left", va="top", fontsize=title_size, weight="bold", color=edge)
    ax.text(x + 0.2, y + h - 0.95, "\n".join(body_lines), ha="left", va="top", fontsize=body_size, color="#101828")


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=18, linewidth=2, color=LINE)
    )


def make_claim_progression():
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=200)
    setup(ax)

    ax.text(
        0.3,
        9.6,
        "Figure 1. Supported Claim Surfaces and Explicit Boundaries",
        fontsize=18,
        weight="bold",
        ha="left",
        va="top",
        color="#101828",
    )
    ax.text(
        0.3,
        9.1,
        "Main figure: one supported claim, one downstream-acceptance boundary, one side-topic supporting surface, and one later-horizon boundary, with family boundaries kept explicit.",
        fontsize=10.5,
        ha="left",
        va="top",
        color=GRAY,
    )

    # Family bands
    ax.add_patch(Rectangle((0.3, 0.8), 7.2, 7.5, linewidth=1.5, linestyle="--", edgecolor="#7A5AF8", facecolor=BLUE_FILL, alpha=0.35))
    ax.add_patch(Rectangle((7.9, 0.8), 2.8, 7.5, linewidth=1.5, linestyle="--", edgecolor="#0BA5EC", facecolor="#D9F3FF", alpha=0.45))
    ax.add_patch(Rectangle((11.0, 0.8), 2.7, 7.5, linewidth=1.5, linestyle="--", edgecolor=RED, facecolor=RED_FILL, alpha=0.25))

    ax.text(0.55, 8.0, "Family A: priority-resolution", fontsize=11, weight="bold", color="#6941C6")
    ax.text(8.15, 8.0, "Family B: side-topic/quarantine", fontsize=11, weight="bold", color="#026AA2")
    ax.text(11.2, 8.0, "Boundary-only read", fontsize=11, weight="bold", color=RED)

    # Timeline labels
    timeline_y = 7.2
    for xpos, label in [
        (1.1, "Early decision\nboundary"),
        (4.8, "First accepted-direction\nboundary"),
        (8.5, "First side-topic\nworkstart"),
        (11.4, "Later checkpoints\n(turn9+)"),
    ]:
        ax.text(xpos, timeline_y, label, fontsize=9.5, ha="center", va="center", color=LINE)
    arrow(ax, 1.8, 6.9, 4.0, 6.9)
    arrow(ax, 5.7, 6.9, 7.7, 6.9)
    arrow(ax, 9.3, 6.9, 10.8, 6.9)

    # Claim boxes
    box(
        ax,
        0.6,
        3.7,
        3.0,
        2.8,
        "Claim 1: supported",
        [
            "Early ambiguity-turn",
            "appropriate: 0/24 -> 24/24",
            "both providers",
            "Policy: defer_with_resolution",
            "Dynamics: Stable Resolution",
        ],
        edge=GREEN,
        face=GREEN_FILL,
    )
    box(
        ax,
        4.0,
        3.45,
        3.2,
        3.05,
        "Boundary: downstream acceptance",
        [
            "Downstream acceptance boundary",
            "mainline: baseline vs Energy policy",
            "burden removal: 0/24 -> 24/24",
            "Gemini followthrough residual",
            "auxiliary: NRR vs Ablation mixed",
            "Anthropic Baseline > NRR",
            "Policy: commit_to_accepted_direction",
            "do not collapse to uniform hold",
        ],
        edge=AMBER,
        face=AMBER_FILL,
    )
    box(
        ax,
        8.1,
        3.6,
        2.4,
        2.9,
        "Supporting surface",
        [
            "First-step side-topic",
            "Anthropic: 9/12 -> 12/12",
            "Gemini: 8/12 -> 12/12",
            "template-bounded",
            "local repaired comparison",
            "Dynamics: Clean Quarantine Hold",
        ],
        edge="#155EEF",
        face="#E5F0FF",
    )
    box(
        ax,
        11.2,
        3.6,
        2.1,
        2.9,
        "Not a supported claim",
        [
            "Later-horizon failure boundary",
            "shared failure: C_incident_response",
            "turn9 relation collapse",
            "Premature Relation Collapse",
        ],
        edge=RED,
        face=RED_FILL,
    )

    # Bottom interpretation strip
    ax.text(0.45, 2.75, "Interpretation layer", fontsize=10.5, weight="bold", color=GRAY)
    box(ax, 0.6, 1.0, 3.0, 1.35, "Policy / dynamics read", ["defer_with_resolution", "Stable Resolution"], edge=GREEN, face="white", title_size=10, body_size=9)
    box(ax, 4.0, 1.0, 3.2, 1.35, "Policy / dynamics boundary", ["commit_to_accepted_direction", "burden removal support + Gemini residual", "auxiliary NRR-vs-Ablation stays mixed"], edge=AMBER, face="white", title_size=10, body_size=7.8)
    box(ax, 8.1, 1.0, 2.4, 1.35, "Policy / dynamics support", ["accepted_direction -> active_objective", "quarantine -> Clean Quarantine Hold"], edge="#155EEF", face="white", title_size=10, body_size=8.2)
    box(ax, 11.2, 1.0, 2.1, 1.35, "Boundary read", ["Relation-Preservation Hold weakens", "-> Premature Relation Collapse"], edge=RED, face="white", title_size=10, body_size=8.2)

    ax.text(0.35, 0.25, "Supported regions are separated from the red failure-boundary region; the downstream-acceptance surface stays on the mainline baseline-vs-Energy-policy contract for bounded burden-removal support, while the side-topic surface remains supporting evidence on a local repaired comparison and the repaired NRR-vs-Ablation read remains auxiliary boundary evidence with Anthropic Baseline still stronger than NRR.", fontsize=8.5, color=GRAY)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_supported_claim_progression_v1.png", bbox_inches="tight")
    plt.close(fig)


def make_architecture():
    fig, ax = plt.subplots(figsize=(14, 5.8), dpi=200)
    setup(ax, xlim=(0, 14), ylim=(0, 6))

    ax.text(0.3, 5.75, "Figure 2. Manuscript-Facing Spine and Supporting Layers", fontsize=18, weight="bold", ha="left", va="top", color="#101828")
    ax.text(0.3, 5.25, "The manuscript-facing spine is paper7 -> Energy -> Guarantee; Policy, Dynamics, and Policy-Verification are imported supporting layers rather than serial spine steps.", fontsize=10.2, ha="left", va="top", color=GRAY)
    ax.text(0.3, 4.75, "Core-to-Guarantee objective framing belongs here only as support: close bounded commit/defer utility under explicit conditions.", fontsize=9.8, ha="left", va="top", color=GRAY)

    # group boundaries
    ax.add_patch(Rectangle((2.3, 0.6), 6.4, 2.4, linewidth=1.5, linestyle="--", edgecolor="#98A2B3", facecolor=LIGHT))
    ax.text(5.5, 2.75, "Imported supporting layers", fontsize=11, weight="bold", ha="center", color="#475467")
    ax.add_patch(Rectangle((10.0, 0.6), 2.8, 3.6, linewidth=1.5, linestyle="--", edgecolor=GREEN, facecolor="#EDF7F0"))
    ax.text(11.4, 4.0, "Claim-owning layer", fontsize=11, weight="bold", ha="center", color=GREEN)

    box(ax, 0.4, 3.1, 2.2, 1.15, "paper7", ["comparison / boundary honesty", "fixed upstream mainline"], edge="#155EEF", face="#E5F0FF", title_size=12, body_size=8.6)
    box(ax, 3.3, 3.1, 2.2, 1.15, "Energy", ["calibration / control handoff", "current upstream authority"], edge="#155EEF", face="#E5F0FF", title_size=12, body_size=8.4)
    box(ax, 2.6, 1.2, 1.8, 1.2, "Policy", ["state/action spec"], edge="#7A5AF8", face="#EEE7FF", title_size=11.5, body_size=8.8)
    box(ax, 4.7, 1.65, 2.0, 1.0, "Dynamics", ["hold / degrade / break"], edge="#0BA5EC", face="#D9F3FF", title_size=11, body_size=8.4)
    box(ax, 4.7, 0.75, 2.0, 1.0, "Policy-Verification", ["matched-condition", "validation surface"], edge="#F79009", face="#FEF0C7", title_size=10.6, body_size=8.1)
    box(ax, 10.3, 1.35, 2.2, 1.95, "Guarantee", ["bounded claim", "this paper"], edge=GREEN, face=GREEN_FILL, title_size=13, body_size=10)

    arrow(ax, 2.6, 3.68, 3.3, 3.68)
    arrow(ax, 5.5, 3.68, 10.3, 2.55)
    arrow(ax, 4.4, 1.8, 10.3, 2.15)
    arrow(ax, 6.7, 2.15, 10.3, 2.45)
    arrow(ax, 6.7, 1.25, 10.3, 1.95)

    ax.text(7.4, 4.05, "Manuscript-facing spine", ha="center", va="bottom", fontsize=10.0, color="#155EEF")
    ax.text(11.4, 0.7, "Guarantee exists to own the claim under explicit provider,\nfamily, horizon, and observability bounds.", ha="center", va="bottom", fontsize=9.2, color=GREEN)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig2_guarantee_centered_architecture_v1.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    make_claim_progression()
    make_architecture()
