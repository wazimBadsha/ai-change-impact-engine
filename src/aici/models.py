from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class Change:
    kind: str
    name: str
    old: str
    new: str

@dataclass
class Cohort:
    name: str
    traffic: float

@dataclass
class ReleaseChange:
    release_id: str
    baseline: str
    changes: list[Change]
    cohorts: list[Cohort]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ReleaseChange":
        return cls(
            release_id=data["release_id"],
            baseline=data["baseline"],
            changes=[Change(c["kind"], c["name"], c.get("from", ""), c.get("to", "")) for c in data.get("changes", [])],
            cohorts=[Cohort(c["name"], float(c.get("traffic", 0))) for c in data.get("cohorts", [])],
        )

@dataclass
class Outcome:
    release_id: str
    cohort: str
    traffic: float
    regression_rate: float
    latency_delta: float
    cost_delta: float
    incident: float
    successful: float = 1.0

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Outcome":
        return cls(d["release_id"], d["cohort"], float(d.get("traffic", 0)), float(d.get("regression_rate", 0)), float(d.get("latency_delta", 0)), float(d.get("cost_delta", 0)), float(d.get("incident", 0)), float(d.get("successful", 1)))

@dataclass
class Forecast:
    release_id: str
    risk: float
    affected_traffic: float
    decision: str
    features: dict[str, float]
    contributions: dict[str, float]
    high_risk_cohorts: list[str]
    evidence: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
