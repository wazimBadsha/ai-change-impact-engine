from collections import defaultdict
from .models import Change, Outcome

def build_dependency_graph(changes: list[Change], outcomes: list[Outcome]) -> dict[str, set[str]]:
    g: dict[str, set[str]] = defaultdict(set)
    for c in changes:
        node = f"{c.kind}:{c.name}"
        g[node].add(f"version:{c.new}")
        g[node].add(f"baseline:{c.old}")
    for o in outcomes:
        cohort = f"cohort:{o.cohort}"
        g[cohort].add(f"release:{o.release_id}")
        for c in changes:
            g[f"{c.kind}:{c.name}"].add(cohort)
    return g

def centrality(graph: dict[str, set[str]]) -> dict[str, float]:
    counts = {n: len(edges) for n, edges in graph.items()}
    m = max(counts.values(), default=1)
    return {n: v / m for n, v in counts.items()}
