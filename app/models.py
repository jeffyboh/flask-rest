from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(40))
    summary = db.Column(db.String(1000))

    def __init__(self, title, author, genre, summary):
        self.title = title
        self.author = author
        self.genre = genre
        self.summary = summary

