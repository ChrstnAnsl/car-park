from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, json, glob, shutil
from werkzeug.utils import secure_filename

app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates')
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Init DB
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Data Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phonenumber = db.Column(db.Integer, unique=True)
    firstname = db.Column(db.String(50))
    middlename = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    address = db.Column(db.String(50))
    dateofbirth = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    car = db.Column(db.String(50))
    platenumber = db.Column(db.String(7))

    def __init__(self, username, password, email, phonenumber, firstname, middlename, lastname, address, dateofbirth, gender, car, platenumber):
        self.username = username
        self.password = password
        self.email = email
        self.phonenumber = phonenumber
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.car = car
        self.platenumber = platenumber

# Schema Definition
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'username', 'password', 'email', 'phonenumber', 'firstname', 'middlename', 'lastname', 'address', 'dateofbirth', 'gender', 'car', 'platenumber'
            )
        success = {
            'status': 'successfully added new user'
        }

# Passing schema to function
user_schema = UserSchema()



@app.route('/', methods=['GET'])
def test():

    return render_template('login.html')
    # return {
    #     'message': 'welcome to Online Parking Management',
    #     'author': 'test'
    # }

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register-new-user', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    phonenumber = request.json['phonenumber']
    firstname = request.json['firstname']
    middlename = request.json['middlename']
    lastname = request.json['lastname']
    address = request.json['address']
    dateofbirth = request.json['dateofbirth']
    gender = request.json['gender']
    car = request.json['car']
    platenumber = request.json['platenumber']

    user_data = User(username, password, email, phonenumber, firstname, middlename, lastname, address, dateofbirth, gender, car, platenumber)

    db.session.add(user_data)
    db.session.commit()

    return user_schema.jsonify(user_data)

# unfinished
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    product = User.query.get(id)

    return {'message': 'succesfully logged in'}


if __name__ == '__main__':
    app.run(debug=True)


