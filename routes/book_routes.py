from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.book import Book

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books", methods=["POST"])
def create_book():
    data = request.json
    book_id = Book.add_book(data)
    return jsonify({"message": "Book added successfully", "id": book_id}), 201

@book_routes.route("/books", methods=["GET"])
def get_books():
    books = Book.get_books()
    return jsonify(books), 200

@book_routes.route("/books/<id>", methods=["GET"])
def get_book_by_id(id):
    book = Book.get_book_by_id(ObjectId(id))
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

@book_routes.route("/books/<id>", methods=["PUT"])
def update_book(id):
    data = request.json
    updated = Book.update_book(ObjectId(id), data)
    if not updated:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book updated successfully"}), 200

@book_routes.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    deleted = Book.delete_book(ObjectId(id))
    if not deleted:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book deleted successfully"}), 200