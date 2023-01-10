from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType
# from sqlalchemy_utils import ScalarListType

app = Flask(__name__)

#'sqlite:///C:\\Users\\Pantex\\Documents\\GitHub\\DRS_PROJEKAT\\ENGINE\\forum.db'         --MILOS

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
    loggedIn=db.Column(db.String(1))
    likedTopic=db.Column(MutableList.as_mutable(PickleType(db.Integer, db.ForeignKey("topic.id"))))
    unlikedTopic=db.Column(MutableList.as_mutable(PickleType(db.Integer, db.ForeignKey("topic.id"))))
    likedComment=db.Column(MutableList.as_mutable(PickleType(db.Integer, db.ForeignKey("comment.id"))))
    unlikedComment=db.Column(MutableList.as_mutable(PickleType(db.Integer, db.ForeignKey("comment.id"))))
    interests=db.Column(MutableList.as_mutable(PickleType(db.Integer, db.ForeignKey("topic.id"))))
    topics = db.relationship('Topic', backref='user')
    commentss = db.relationship('Comment', backref='user')

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likedPosts = db.relationship('User', backref='topic')
    comments = db.relationship('Comment', backref='topic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(50))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    likedComment = db.relationship('User', backref='comment')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

with app.app_context():
    db.create_all()