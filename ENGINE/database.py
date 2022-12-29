from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    password = db.Column(db.String(50))
    phoneNumber = db.Column(db.Number(50))
    email = db.Column(db.String(100), unique=True)

with app.app_context():
    db.create_all()