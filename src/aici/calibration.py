from __future__ import annotations
from dataclasses import dataclass

@dataclass
class CalibrationBin:
    lower: float
    upper: float
    mean_prediction: float
    observed_rate: float
    count: int

def reliability_bins(predictions: list[float], labels: list[int], bins: int = 5) -> list[CalibrationBin]:
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have equal length")
    if not predictions:
        return []
    result = []
    for i in range(bins):
        lo, hi = i / bins, (i + 1) / bins
        pairs = [(p, y) for p, y in zip(predictions, labels) if lo <= p < hi or (i == bins - 1 and p == hi)]
        if pairs:
            result.append(CalibrationBin(lo, hi, sum(p for p,_ in pairs)/len(pairs), sum(y for _,y in pairs)/len(pairs), len(pairs)))
    return result
