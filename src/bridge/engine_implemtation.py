from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start():
        pass

class Diseal(Engine):
    def start(self):
        return "starting diseal engine"
    
class Petrol(Engine):
    def start(self):
        return "starting petrol engine"
