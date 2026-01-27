class BookCollection:
    def __init__(self):
        self._books = []
    def add_book(self, name):
        self._books.append(name)
    def __iter__(self):
        for book in self._books:
            yield book

collection = BookCollection()
collection.add_book("Harry")
collection.add_book("java")

for book in collection:
    print(book) 