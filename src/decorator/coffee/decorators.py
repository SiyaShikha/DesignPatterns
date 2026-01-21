from decorator.coffee.coffee import Coffee


class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_description(self):
        return self.decorated_coffee.get_description()

    def get_cost(self):
        return self.decorated_coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Milk"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.2
