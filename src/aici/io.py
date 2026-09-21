import json
from pathlib import Path
from .models import ReleaseChange, Outcome

def load_change(path):
    return ReleaseChange.from_dict(json.loads(Path(path).read_text()))

def load_history(path):
    data = json.loads(Path(path).read_text())
    return [Outcome.from_dict(x) for x in data]
