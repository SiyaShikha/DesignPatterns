
from singleton.singleton_methods.using_meta_class import Animal, Bird


def test_singleton_car_class_objects_are_same():
    obj1 = Bird()
    obj2 = Bird()
    print(obj1)
    print(obj2)
    assert obj1 == obj2

# def test_singleton_animal_class_objects_are_same():
#     obj1 = Animal()
#     obj2 = Animal()
#     assert obj1 == obj2

