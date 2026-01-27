class Mammals(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

class Bird(metaclass=Mammals):
    def __init__(self):
        self.name = "parrot"

class Animal(metaclass=Mammals):
    def __init__(self):
        self.name = "cat"