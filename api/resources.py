from flask import Flask, jsonify, request
from models import add_book, get_books, get_book, update_book, delete_book

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
