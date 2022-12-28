from flask import jsonify,request, Flask
from flask_cors import CORS


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

users = [ { 'username': 'milos', 'password':'milos'}]

@app.route('/home', methods=['get'])
def home():
    return jsonify(users)

@app.route('/login', methods=['post'])
def login():
    return jsonify(users)


@app.route('/register', methods=['post'])
def register():
    return jsonify(users)

app.run()