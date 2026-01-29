class Car:
    _engine = None
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        return self._engine.start()


class Sedan(Car):
    def start(self):
        return super().start()
    
class Swift(Car):
    def start(self):
        return super().start()

