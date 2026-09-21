from aici.calibration import reliability_bins

def test_reliability_bins():
    bins = reliability_bins([0.1, 0.2, 0.8, 0.9], [0, 0, 1, 1], bins=2)
    assert len(bins) == 2
    assert bins[0].observed_rate == 0
    assert bins[1].observed_rate == 1
