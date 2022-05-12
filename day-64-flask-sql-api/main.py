from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "3619e7b9c68c95199e62b5f6f066fd35"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to silence the deprecation warning
db = SQLAlchemy(app)


# creating table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


db.create_all()


# creating form
class EditForm(FlaskForm):
    new_rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # orders movies in ascending order (don't use the desc() method -> the movies start from the least rated)
    all_movies = Movie.query.order_by(Movie.ranking).all()
    for i in range(len(all_movies)):
        # new ranking reversed from their order in all_movies -> descending order
        all_movies[i].ranking = len(all_movies) - i
    # commit the order in DB
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    new_rating = request.form.get('new_rating')
    new_review = request.form.get('new_review')
    movie_id = request.args.get("id")
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():  # checks if it's a post request & if it's valid
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_update)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        PARAMETERS = {
            "api_key": API_KEY,
            "language": "en-US",
            "query": request.form.get("movie_title"),
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=PARAMETERS)
        response.raise_for_status()
        data = response.json()
        return render_template("select.html", results=data["results"])
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_api_id}", params={"api_key": API_KEY})
        response.raise_for_status()
        data = response.json()
        # creating a new instance in the table with the available parameters
        new_movie = Movie(
            title=data["title"],
            img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
            year=data["release_date"].split("-")[0],
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
