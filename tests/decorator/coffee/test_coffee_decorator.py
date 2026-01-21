from decorator.coffee.coffee import PlainCoffee
from decorator.coffee.decorators import MilkDecorator, SugarDecorator


def test_milk_decorator():
    plain_coffee = PlainCoffee()
    milk_added_coffee = MilkDecorator(plain_coffee)
    assert milk_added_coffee.get_cost() == 2.5

def test_sugar_decorator():
    plain_coffee = PlainCoffee()
    sugar_added_coffee = SugarDecorator(plain_coffee)
    assert sugar_added_coffee.get_cost() == 2.2

def test_milk_sugar_combo_decorators():
    plain_coffee = PlainCoffee()
    milk_added_coffee = MilkDecorator(plain_coffee)
    sugar_milk_coffee = SugarDecorator(milk_added_coffee)
    assert sugar_milk_coffee.get_cost() == 2.7
    

