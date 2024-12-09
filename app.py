from flask import Flask, request, jsonify
import database
from auth import token_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System!"})


@app.route('/books', methods=['GET'])
@token_required
def get_books():
    books = database.get_all_books()
    return jsonify(books)

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.get_json()
    new_book = database.add_book(data)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.get_json()
    updated_book = database.update_book(book_id, data)
    if updated_book:
        return jsonify(updated_book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    success = database.delete_book(book_id)
    if success:
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"message": "Book not found"}), 404

# Search Books by author
@app.route('/books/search', methods=['GET'])
@token_required
def search_books():
    query = request.args.get('q', '').lower()
    results = database.search_books(query)
    return jsonify(results)

if __name__ == '__main__':
    database.initialize_database()
    app.run(debug=True)