from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/blog/')
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def blog_read(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, post_num=num)


if __name__ == "__main__":
    app.run(debug=True)
