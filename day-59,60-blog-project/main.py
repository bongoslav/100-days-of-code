from flask import Flask, render_template, request
import requests
from datetime import date
import smtplib
import os

OWN_EMAIL = os.environ["GMAIL"]
OWN_PASSWORD = os.environ["GMAIL_PASSWORD"]

today = date.today()

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()
date = today.strftime("%B %d, %Y")


@app.route("/")
def home():
    return render_template("index.html", posts=posts, date=date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", posts=posts, num=num, date=date)

@app.route("/contact", methods=['GET', 'POST'])
def receive_data():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
