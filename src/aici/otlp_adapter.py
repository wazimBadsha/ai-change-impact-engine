from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class TelemetryOutcome:
    """Provider-neutral normalized outcome from an observability event."""
    release_id: str
    cohort: str
    regression_rate: float = 0.0
    latency_delta: float = 0.0
    cost_delta: float = 0.0
    incident: float = 0.0
    traffic: float = 0.0

def normalize_event(event: dict[str, Any]) -> TelemetryOutcome:
    attrs = event.get("attributes", event)
    return TelemetryOutcome(
        release_id=str(attrs.get("release.id", attrs.get("release_id", "unknown"))),
        cohort=str(attrs.get("ai.cohort", attrs.get("cohort", "unknown"))),
        regression_rate=float(attrs.get("ai.regression_rate", attrs.get("regression_rate", 0))),
        latency_delta=float(attrs.get("ai.latency_delta", attrs.get("latency_delta", 0))),
        cost_delta=float(attrs.get("ai.cost_delta", attrs.get("cost_delta", 0))),
        incident=float(attrs.get("ai.incident", attrs.get("incident", 0))),
        traffic=float(attrs.get("ai.traffic", attrs.get("traffic", 0))),
    )
