from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media1.giphy.com/media/IsfrRWvbUdRny/giphy.gif?cid=ecf05e473dtwn8gng7t3w4e9bll1lw100lt7m6hqmm428zrj&rid=giphy.gif&ct=g'>"

random_num = random.randint(0, 9)

@app.route('/<int:number>')
def entered_nubmer(number):
    if number < random_num:
        return f"<h1 style='color: red'> Number {number} is too low.</h1>"
    elif number > random_num:
        return f"<h1 style='color: blue'> Number {number} is too high.</h1>"
    else:
        return f"<h1 style='color: green'> Number {number} is the correct number!</h1>"

if __name__ == "__main__":
    app.run(debug=True)