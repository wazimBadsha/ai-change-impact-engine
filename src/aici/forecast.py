from .features import extract_features
from .model import RiskModel
from .models import Forecast, ReleaseChange, Outcome

def forecast(change: ReleaseChange, history: list[Outcome], model: RiskModel | None = None) -> Forecast:
    features, meta = extract_features(change, history)
    model = model or RiskModel()
    risk = model.predict(features)
    affected = min(sum(c.traffic for c in change.cohorts), 1.0)
    cohort_scores = {}
    for cohort in change.cohorts:
        hist = [o for o in history if o.cohort == cohort.name]
        base = sum(o.regression_rate + o.incident for o in hist) / max(len(hist), 1)
        cohort_scores[cohort.name] = base * cohort.traffic + 0.2 * features["dependency_centrality"] * cohort.traffic
    high = [k for k, v in cohort_scores.items() if v >= 0.20]
    decision = "BLOCK" if risk >= 0.75 else ("REVIEW" if risk >= 0.50 else "ALLOW")
    contributions = {k: round(model.weights.get(k, 0.0) * v, 5) for k, v in features.items()}
    evidence = []
    if features["dependency_centrality"] >= 0.6: evidence.append("changed dependency has high historical graph centrality")
    if features["historical_regression"] >= 0.2: evidence.append("similar historical cohorts show regression")
    if features["incident_rate"] > 0: evidence.append("historical incidents exist in the affected cohort set")
    if features["latency_delta"] >= 0.25: evidence.append("historical latency delta is elevated")
    if features["cost_delta"] >= 0.25: evidence.append("historical cost delta is elevated")
    if not evidence: evidence.append("no strong historical risk signal was observed")
    evidence.append(f"graph contains {meta['graph_nodes']} dependency nodes")
    return Forecast(change.release_id, round(risk, 4), round(affected, 4), decision, {k: round(v, 4) for k, v in features.items()}, contributions, high, evidence)
