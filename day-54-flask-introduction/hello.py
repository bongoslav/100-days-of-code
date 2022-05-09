# install flask from terminal
# cd to file's parent folder
# set flask env: $env:FLASK_APP = "hello" and run it (flask run)

from flask import Flask
app = Flask(__name__)


@app.route('/')  # trigger the function only if the user tries to access the homepage url
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return "Bye"

if __name__ == "__main__":
    # run the code from withing current file
    app.run()