from collections import defaultdict
from .models import ReleaseChange, Outcome
from .graph import build_dependency_graph, centrality

def extract_features(change: ReleaseChange, history: list[Outcome]) -> tuple[dict[str, float], dict[str, str]]:
    graph = build_dependency_graph(change.changes, history)
    cent = centrality(graph)
    relevant = [o for o in history if o.cohort in {c.name for c in change.cohorts}]
    traffic = sum(c.traffic for c in change.cohorts)
    denom = max(sum(o.traffic for o in relevant), 1e-9)
    regression = sum(o.regression_rate * o.traffic for o in relevant) / denom
    latency = sum(abs(o.latency_delta) * o.traffic for o in relevant) / denom
    cost = sum(abs(o.cost_delta) * o.traffic for o in relevant) / denom
    incidents = sum(o.incident * o.traffic for o in relevant) / denom
    changed_kinds = len({c.kind for c in change.changes})
    changed_nodes = [f"{c.kind}:{c.name}" for c in change.changes]
    graph_centrality = sum(cent.get(n, 0) for n in changed_nodes) / max(len(changed_nodes), 1)
    features = {
        "change_density": min(len(change.changes) / 5.0, 1.0),
        "dependency_centrality": graph_centrality,
        "cohort_exposure": min(traffic, 1.0),
        "historical_regression": min(regression, 1.0),
        "latency_delta": min(latency / 2.0, 1.0),
        "cost_delta": min(cost / 2.0, 1.0),
        "incident_rate": min(incidents, 1.0),
        "change_kind_diversity": min(changed_kinds / 5.0, 1.0),
    }
    meta = {"graph_nodes": str(len(graph)), "historical_samples": str(len(relevant)), "changed_nodes": ",".join(changed_nodes)}
    return features, meta
