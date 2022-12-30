import sys
from flask import jsonify,request, Flask,session
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
    print("testtest")
    sys.stdout.flush()
    return jsonify(users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify(users)


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=="POST":
       #print(request.form, flush=True)
       user=request.get_json()
      
       print("user:"+user['username'])
       sys.stdout.flush()
       print("password:"+user['password'])
       sys.stdout.flush()
       #return{"data":"ok","redirect":"/login"},200;
       print("registertest")
       return jsonify("submitted!")
    


app.run()