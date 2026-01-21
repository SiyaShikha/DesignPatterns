from decorator.power.number import NumberComponent


class NumberDecorator(NumberComponent):
    def __init__(self, number: NumberComponent):
        self.number = number

    def get_value(self):
        return self.number.get_value()

class SquareDecorator(NumberDecorator):
    def get_value(self):
        value = self.number.get_value()
        return value * value

class CubeDecorator(NumberDecorator):
    def get_value(self):
        value = self.number.get_value()
        return value * value * value
