from app import app, db, ma
from flask import request, jsonify
from app.models import Book

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'genre', 'summary')

book_schema = BookSchema(strict=True)
books_schema = BookSchema(many=True, strict=True)

# Create a Book
@app.route('/book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    summary = request.json['summary']

    book = Book(title, author, genre, summary)

    db.session.add(book)
    db.session.commit()

    return book_schema.jsonify(book)


# Get single Book
@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    return book_schema.jsonify(book)


# Get all Books
@app.route('/book', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = books_schema.dump(books)
    return jsonify(result.data)


# Update a Book
@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)

    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    summary = request.json['summary']

    book.title = title
    book.author = author
    book.genre = genre
    book.summary = summary

    db.session.commit()

    return book_schema.jsonify(book)

# Delete single Book
@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)
