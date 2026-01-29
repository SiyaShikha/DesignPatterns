from bridge.car_abstraction import Sedan, Swift
from bridge.engine_implemtation import Diseal, Petrol


def test_sedan_car_starts_the_engine():
    engine = Diseal()
    car = Sedan(engine)
    assert car.start() == "starting diseal engine"

def test_swift_car_starts_the_engine():
    engine = Petrol()
    car = Swift(engine)
    assert car.start() == "starting petrol engine"

