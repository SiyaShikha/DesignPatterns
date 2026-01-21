from decorator.power.number import Number

def test_power_decorator_returns_square():
    num = Number(12)
    assert num.calculations() == 144