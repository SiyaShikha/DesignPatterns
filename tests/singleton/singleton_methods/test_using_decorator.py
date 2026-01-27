from singleton.singleton_methods.using_decorator import Animal, Car


def test_singleton_car_class_objects_are_same():
    obj1 = Car()
    obj2 = Car()
    assert obj1 == obj2

def test_singleton_animal_class_objects_are_same():
    obj1 = Animal()
    obj2 = Animal()
    assert obj1 == obj2

