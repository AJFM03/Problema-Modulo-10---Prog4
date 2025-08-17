import uuid

books_db = {}  # Diccionario simulando la base de datos

def add_book(data):
    book_id = str(uuid.uuid4())
    book = {"id": book_id, **data}
    books_db[book_id] = book
    return book

def get_books():
    return list(books_db.values())

def get_book(book_id):
    return books_db.get(book_id)

def update_book(book_id, data):
    if book_id in books_db:
        books_db[book_id].update(data)
        return books_db[book_id]
    return None

def delete_book(book_id):
    return books_db.pop(book_id, None)
