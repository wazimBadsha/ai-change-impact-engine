from aici.model import RiskModel

def test_model_probability():
    m = RiskModel()
    p = m.predict({"change_density":1.0,"dependency_centrality":1.0})
    assert 0 < p < 1

def test_model_can_learn_signal():
    m = RiskModel()
    rows = []
    for _ in range(30):
        rows.append(({"change_density":0.0}, 0))
        rows.append(({"change_density":1.0}, 1))
    m.fit([x for x,_ in rows], [y for _,y in rows], epochs=200)
    assert m.predict({"change_density":1.0}) > m.predict({"change_density":0.0})
