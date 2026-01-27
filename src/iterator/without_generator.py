class Iterator:
    def __init__(self, collection):
        self._books = collection
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book
    
class BookCollection:
    def __init__(self):
        self._books = []
    def add_book(self, name):
        self._books.append(name)
    def create_iterator(self):
        return Iterator(self._books)  

collection = BookCollection()
collection.add_book("Harry")
collection.add_book("java")

iterator = collection.create_iterator()

for book in iterator:
    print(book)     
    