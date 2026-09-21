from pathlib import Path
from aici.io import load_change, load_history
from aici.forecast import forecast
from aici.policy import Policy, gate

ROOT = Path(__file__).parents[1]

def test_forecast_is_explainable():
    f = forecast(load_change(ROOT / "examples/change.json"), load_history(ROOT / "examples/history.json"))
    assert 0 <= f.risk <= 1
    assert f.decision in {"ALLOW", "REVIEW", "BLOCK"}
    assert f.evidence
    assert "billing" in f.high_risk_cohorts

def test_policy_exit_decision():
    f = forecast(load_change(ROOT / "examples/change.json"), load_history(ROOT / "examples/history.json"))
    assert gate(f, Policy()) in {"ALLOW", "REVIEW", "BLOCK"}
