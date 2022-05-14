from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route("/")
def home():
    return render_template("index.html")


# Explanation:
# initially we create class Cafe and inherited with class db.Model and in that class there is attribute name table
# in that table all data is contained and when we call random_cafe.to_dict() it will take any random row from database
# table and call it using column and data by getattr() function
def to_dict(self):
    dictionary = {}
    # loop through each column in the data record
    for column in self.__table__.columns:
        # create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary


@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    # this time, because our server is now acting as an API, we want to return a JSON containing the necessary data
    # to do this we have to turn our random_cafe SQLAlchemy Object into a JSON. The process is called serialization.
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[to_dict(cafe) for cafe in cafes])


@app.route("/search")
def search_cafe():
    loc = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=loc).first()
    if cafe:
        return jsonify(cafe=to_dict(cafe))
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# testing in postman
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# PATCH request
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    else:
        return jsonify(error={"Not Found": "No cafe with such id was found."})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def close_cafe(cafe_id):
    api_key = request.args.get("api-key")
    cafe = Cafe.query.get(cafe_id)
    if api_key == "TopSecretAPIKey" and cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Successfully deleted the cafe.")
    elif api_key != "TopSecretAPIKey":
        return jsonify(error="Make sure you got the correct API key.")
    else:
        return jsonify(error={"Not Found": "No cafe with such id was found."})


# Published Documentation: https://documenter.getpostman.com/view/20976551/UyxjEkja

if __name__ == '__main__':
    app.run(debug=True)
