from __future__ import annotations
import argparse, json
from .io import load_change, load_history
from .forecast import forecast
from .policy import Policy, gate
from .report import markdown_report
from .models import Forecast

def main():
    p = argparse.ArgumentParser(prog="aici", description="AI Change Intelligence")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("forecast")
    f.add_argument("change")
    f.add_argument("history")
    f.add_argument("--json", action="store_true")
    g = sub.add_parser("gate")
    g.add_argument("forecast")
    g.add_argument("--policy", required=True)
    args = p.parse_args()
    if args.cmd == "forecast":
        result = forecast(load_change(args.change), load_history(args.history))
        print(json.dumps(result.to_dict(), indent=2) if args.json else markdown_report(result))
        return 0
    result = Forecast(**json.loads(open(args.forecast).read()))
    decision = gate(result, Policy(**json.loads(open(args.policy).read())))
    print(decision)
    return {"ALLOW": 0, "REVIEW": 10, "BLOCK": 20}[decision]

if __name__ == "__main__":
    raise SystemExit(main())
