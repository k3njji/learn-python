from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "books_collections.db")
db.init_app(app)

@app.route('/')
def home():
    # all_books = db.session.query(User).all()
    # another way to get it
    all_books = db.session.execute(db.select(User).order_by(User.title)).scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = User(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.session.get(User, book_id)
    if request.method == 'POST':
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)

@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book = db.session.get(User, book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "books_collections.db")
# print(db_path)

# db = sqlite3.connect(db_path)
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, rating REAL)")
# cursor.execute(
#     "INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
#     ('Harry Potter', 'J. K. Rowling', 9.3)
# )
# db.commit()