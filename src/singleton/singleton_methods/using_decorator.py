class Singleton:
    class_instances = {}
    def __init__(self, cls):
        self.curren_cls = cls

    def __call__(self, *args, **kwargs):
        # if an instance of cls exists, return instance, else create, store and return
        instance = self.class_instances.get(self.curren_cls)
        if instance is None:
            instance = self.curren_cls(*args, **kwargs)
            self.class_instances[self.curren_cls] = instance
        return instance

@Singleton
class Car:
    def __init__(self):
        self.color = "red"

@Singleton
class Animal:
    def __init__(self):
        self.name = "cat"