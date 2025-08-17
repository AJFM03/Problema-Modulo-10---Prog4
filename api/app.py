from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# Simulación de base de datos en memoria
books_db = {}

# -----------------------
# Funciones de manejo de libros
# -----------------------
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

# -----------------------
# Endpoints de la API
# -----------------------
@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(get_books()), 200

@app.route("/books/<book_id>", methods=["GET"])
def retrieve_book(book_id):
    book = get_book(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "author", "genre", "status")):
        return jsonify({"error": "Invalid data"}), 400
    book = add_book(data)
    return jsonify(book), 201

@app.route("/books/<book_id>", methods=["PUT"])
def edit_book(book_id):
    data = request.get_json()
    book = update_book(book_id, data)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<book_id>", methods=["DELETE"])
def remove_book(book_id):
    book = delete_book(book_id)
    if book:
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404

# -----------------------
# Inicio de la app
# -----------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
