from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Pantex\\Documents\\GitHub\\DRS_PROJEKAT\\ENGINE\\forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    address = db.Column(db.String(50))
    country = db.Column(db.String(50))
    username= db.Column(db.String(50))
    password = db.Column(db.String(50))
    phoneNumber = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    topics = db.relationship('Topic', backref='user')

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

with app.app_context():
    db.create_all()
    