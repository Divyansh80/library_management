import json
import os

DB_FILE = 'db.json'

def initialize_database():
    """Create the database """
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({"books": []}, f)

def read_db():
    """Read  database"""
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def write_db(data):
    """Write data """
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_all_books():
    return read_db()["books"]

def add_book(book_data):
    db = read_db()
    new_book = {
        "id": len(db["books"]) + 1,
        "title": book_data["title"],
        "author": book_data["author"],
        "year": book_data.get("year", "Unknown")
    }
    db["books"].append(new_book)
    write_db(db)
    return new_book

def update_book(book_id, book_data):
    """Update  existing book"""
    db = read_db()
    for book in db["books"]:
        if book["id"] == book_id:
            book.update(book_data)
            write_db(db)
            return book
    return None

def delete_book(book_id):
    """Delete  book"""
    db = read_db()
    original_len = len(db["books"])
    db["books"] = [book for book in db["books"] if book["id"] != book_id]
    write_db(db)
    return len(db["books"]) < original_len

def search_books(query):
    """Search books by author."""
    db = read_db()
    return [book for book in db["books"] if query in book["title"].lower() or query in book["author"].lower()]
