from iterator.with_generator import BookCollection

def test_collections_adds_elements():
    collection = BookCollection()
    collection.add_book("Harry Potter")
    collection.add_book("python")
    
    assert next(collection) == "Harry Potter"
    assert next(collection) == "python"