from bridge.engine_implemtation import Diseal, Petrol

def test_diseal_engine_starts():
    engine = Diseal()
    assert engine.start() == "starting diseal engine"

def test_petrol_engine_starts():
    engine = Petrol()
    assert engine.start() == "starting petrol engine"