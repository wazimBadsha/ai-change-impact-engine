from dataclasses import dataclass
from .models import Forecast

@dataclass
class Policy:
    review_at: float = 0.50
    block_at: float = 0.75
    max_affected_traffic: float = 0.90

def gate(forecast: Forecast, policy: Policy) -> str:
    if forecast.risk >= policy.block_at or forecast.affected_traffic > policy.max_affected_traffic:
        return "BLOCK"
    if forecast.risk >= policy.review_at:
        return "REVIEW"
    return "ALLOW"
