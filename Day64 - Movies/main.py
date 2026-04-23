from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
import dotenv 

dotenv.load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "movies_collections.db")
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
Bootstrap5(app)

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# CREATE DB
class Movie(db.Model):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

from flask_wtf import FlaskForm
from wtforms import FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class EditForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Update Movie")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

db.init_app(app)

# CREATE TABLE


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    return render_template("index.html", movies=movies)

@app.route("/addMovie", methods=["GET", "POST"])
def addMovie():
    return render_template("add.html")

@app.route("/editMovie/<int:movie_id>", methods=["GET", "POST"])
def editMovie(movie_id):
    movie = db.session.get(Movie, movie_id)
    form = EditForm(obj=movie)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/delete", methods=["POST"])
def delete_movie():
    movie_id = request.form["movie_id"]
    movie = db.session.get(Movie, movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        result = db.session.execute(db.select(Movie).limit(1)).first()

        if result:
            print("Table has data")
        else:
            new_movie = Movie(
                title="Phone Booth",
                year=2002,
                description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
                rating=7.3,
                ranking=10,
                review="My favourite character was the caller.",
                img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
            )

            db.session.add(new_movie)
            db.session.commit()
        db.create_all()
    app.run(debug=True)
