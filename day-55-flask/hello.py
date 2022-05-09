from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media2.giphy.com/media/K1tgb1IUeBOgw/giphy.gif?cid=ecf05e47zdphots2ude1c041u6w0w4h27hoeinneufveuq91&rid=giphy.gif&ct=g" width=200px>' \


# adding multiple decorators
@app.route('/bye')
@make_emphasis
@make_underlined
@make_bold
def say_bye():
    return "Bye"

# extracting parts from url
# <path:variable> -> gets whatever string we specify as path and it can be used
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there, {name}, you are {number} years old!"



# Playground:
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:  # only if the variable is True execute the function
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Mario")
create_blog_post(new_user)



if __name__ == "__main__":
    # run the code from withing current file
    app.run(debug=True)
