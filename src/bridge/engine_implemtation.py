from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start_engine():
        pass

class Diseal(Engine):
    def start_engine(self):
        return "starting diseal engine"
    
class Petrol(Engine):
    def start_engine(self):
        return "starting petrol engine"
