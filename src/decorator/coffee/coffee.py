from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class PlainCoffee(Coffee):
    def get_description(self):
        return "Plain Coffee"

    def get_cost(self):
        return 2.0
