from iterator.with_generator import BookCollection

def test_collections_adds_elements():
    collection = BookCollection()
    collection.add_book("Harry Potter")
    collection.add_book("python")
    
    iterator = iter(collection)
    assert next(iterator) == "Harry Potter"
    assert next(iterator) == "python"