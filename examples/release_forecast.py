from aici.io import load_change, load_history
from aici.forecast import forecast
from aici.report import markdown_report

if __name__ == "__main__":
    f = forecast(load_change("examples/change.json"), load_history("examples/history.json"))
    print(markdown_report(f))
