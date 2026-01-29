from abc import ABC, abstractmethod
class Car(ABC):
    _engine = None
    def __init__(self, engine):
        self._engine = engine

    @abstractmethod
    def start(self):
        pass


class Sedan(Car):
   def start(self):
       return f"Sedan {self._engine.start_engine()}"
   
   def window(self):
       return "top window"
    
class Swift(Car):
    def start(self):
        return f"Swift {self._engine.start_engine()}"
    
    def window(self):
       return "side window"

