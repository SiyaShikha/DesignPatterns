from decorator.power.number import Number
from decorator.power.decorator import CubeDecorator, SquareDecorator

def test_number_returns_value():
    number = Number(3)
    assert number.get_value() == 3

def test_square_decorator():
    number = Number(2)
    square = SquareDecorator(number)
    assert square.get_value() == 4

    cube = CubeDecorator(square)
    assert cube.get_value() == 64

    square_again = SquareDecorator(cube)
    assert square_again.get_value() == 64 * 64

def test_cube_decorator():
    cube = CubeDecorator(Number(2))
    assert cube.get_value() == 8