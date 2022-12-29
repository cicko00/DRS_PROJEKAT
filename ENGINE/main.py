from flask import jsonify,request, Flask
from create_database import create_connection
from flask_cors import CORS
from Models.User import User



app = Flask(__name__)
app.config['DEBUG'] = True

CORS(app)

database = create_connection("forum.db")

users = [ { 'username': 'milos', 'password':'milos'}]

@app.route('/home', methods=['get'])
def home():
    return jsonify(users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify(users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return jsonify(users)

app.run()