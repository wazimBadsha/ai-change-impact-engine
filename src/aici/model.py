from __future__ import annotations
import math

FEATURES = ["change_density", "dependency_centrality", "cohort_exposure", "historical_regression", "latency_delta", "cost_delta", "incident_rate", "change_kind_diversity"]

class RiskModel:
    """Small dependency-free logistic learner for release-risk forecasting."""
    def __init__(self, weights=None, bias=-1.2):
        self.weights = dict(weights or {
            "change_density": 0.9, "dependency_centrality": 1.2,
            "cohort_exposure": 0.5, "historical_regression": 2.0,
            "latency_delta": 0.8, "cost_delta": 0.5,
            "incident_rate": 1.8, "change_kind_diversity": 0.7,
        })
        self.bias = bias

    @staticmethod
    def _sigmoid(z):
        z = max(min(z, 30), -30)
        return 1.0 / (1.0 + math.exp(-z))

    def predict(self, features):
        return self._sigmoid(self.bias + sum(self.weights.get(k, 0.0) * features.get(k, 0.0) for k in FEATURES))

    def fit(self, rows, labels, epochs=120, lr=0.18):
        if not rows:
            return
        for _ in range(epochs):
            grad = {f: 0.0 for f in FEATURES}
            gb = 0.0
            for x, y in zip(rows, labels):
                err = self.predict(x) - y
                gb += err
                for f in FEATURES:
                    grad[f] += err * x.get(f, 0.0)
            n = len(rows)
            self.bias -= lr * gb / n
            for f in FEATURES:
                self.weights[f] -= lr * grad[f] / n
