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