import json
from .models import Forecast

def markdown_report(f: Forecast) -> str:
    lines = [
        f"# AI Change Intelligence — {f.release_id}", "",
        f"Decision: {f.decision}", f"Risk: {f.risk:.2f}", f"Affected traffic: {f.affected_traffic:.0%}", "",
        "## High-risk cohorts",
        *([f"- {x}" for x in f.high_risk_cohorts] or ["- None identified"]),
        "", "## Evidence", *[f"- {x}" for x in f.evidence], "",
        "## Features", json.dumps(f.features, indent=2), "",
        "## Model contributions", json.dumps(f.contributions, indent=2),
    ]
    return "
".join(lines)
