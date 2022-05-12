# writing SQL code
# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # create a db
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, "
# #     "rating FLOAT NOT NULL)")
#
# # install SQLitebrowser to open the .db file
#
# # commit data to db
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# using SQLAlchemy
# from quickstart blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to silence the deprecation warning
db = SQLAlchemy(app)

# create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float(), unique=True, nullable=False)

    # optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# create record
book = Book(title="Harry Potter", author="J.K. Rowling", rating=5.5)
db.session.add(book)
db.session.commit()



# --------------------- CRUD example --------------------- #
# Create a new record
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)  # id is optional
db.session.add(new_book)
db.session.commit()

# Read all records
all_books = Book.query.all()
# Read A Particular Record By Query
book = Book.query.filter_by(title="Harry Potter").first()

# Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
# Update A Record By PRIMARY KEY
book_id = 1
# get data from form:
# new_title = request.form.get('new_title')  # '...' from Form class in py
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"  # new_title
db.session.commit()

# Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()