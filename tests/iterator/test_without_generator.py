from DesignPatterns.src.iterator.without_generator import BookCollection


def test_collections_adds_elements():
    collection = BookCollection()
    collection.add_book("Harry Potter")
    collection.add_book("python")
    
    iterator = collection.create_iterator()
    
    assert next(iterator) == "Harry Potter"
    assert next(iterator) == "python"