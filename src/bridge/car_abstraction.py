from abc import ABC, abstractmethod
class Car(ABC):
    _engine = None
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        return self._engine.start()


class Sedan(Car):
   def window(self):
       return "top window"
    
class Swift(Car):
    def window(self):
       return "side window"

