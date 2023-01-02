import sys
from flask import jsonify,request, Flask,session
from create_database import create_connection
from flask_cors import CORS
from Models.User import User
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True

CORS(app)

database = create_connection("C:\\git\\DRS_PROJEKAT\\ENGINE\\forum.db")
users = [ { 'username': 'milos', 'password':'milos'}]
cursor=database.cursor()
##cursor.execute("""INSERT OR REPLACE INTO  user (id,firstName,lastName,address,country,username,password,phoneNumber,email) VALUES (4,'Emilija','Balaz','Kikinda','Srbija','emily','nestonamadjarskom','brojtelefona','emiliabalazs.ki@gmail.com')""")
##cursor.execute("""DROP TABLE user""")


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
       
       user=request.get_json()

       cursor.execute("""SELECT * from user""")
       database.commit()
       db_list=cursor.fetchall()
       for i in db_list:
         if(i[6]==user['password']):
            return jsonify("PASSWORD!")
         elif(i[5]==user['username']):
            return jsonify("USERNAME!")
        
       cursor.execute("SELECT COALESCE(MAX(id),0) FROM user")
       database.commit()
       oldid=cursor.fetchall
    

       cursor.execute("""INSERT OR REPLACE INTO  user (id,firstName,lastName,address,country,username,password,phoneNumber,email) VALUES (?,?,?,?,?,?,?,?,?)""",(1,user['firstName'],user['lastName'],user['address'],user['country'],user['username'],user['password'],user['phoneNumber'],user['email']))
       database.commit()



       
      

       
       
       print("user:"+user['username']+"  pasword:"+user['password'])
       sys.stdout.flush()
       
       
       #return{"data":"ok","redirect":"/login"},200;
       print("registertest")
       return jsonify("submitted!")
    


app.run()