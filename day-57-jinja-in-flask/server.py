from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)  # adding kwargs to the html file


@app.route('/guess/<guessed_name>')
def guess(guessed_name):
    params_gender = {"name": f"{guessed_name}"}
    params_age = {"name": f"{guessed_name}"}

    response_gender = requests.get("https://api.genderize.io", params=params_gender)
    response_age = requests.get("https://api.agify.io", params=params_age)

    gender = response_gender.json()["gender"]
    age = response_age.json()["age"]

    return render_template("guess.html", name=guessed_name, gender=gender, age=age)
    

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
