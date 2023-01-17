import os
import sys
import time
from flask import jsonify,request, Flask,session,current_app
from create_database import create_connection
from flask_cors import CORS
from Models.User import User,ListToDict
from Models.Post import Post,ListToDictPost
from flask_session import Session
import json
import sqlite3
import sqlalchemy
import jwt
import security


app = Flask(__name__)

app.config['DEBUG'] = True
app.config["SESSION_TYPE"]='filesystem'
app.config["SESSION_PERMANENT"]=True
app.config["PERMANENT_SESSION_LIFETIME"]=1000
app.config["SECRET_KEY"]="SECRET_KEY"



CORS(app)
##"C:\\git\\DRS_PROJEKAT\\ENGINE\\forum.db"                                           --Cvijetin
##"D:\\Fakultet\\CETVRTA GODINA\\DRS\\PROJEKAT\\DRS_PROJEKAT\\ENGINE\\forum.db"       --Emilija
##"C:\\Users\\Pantex\\Documents\\GitHub\\DRS_PROJEKAT\\ENGINE\\forum.db"              --Miloš
##
database = create_connection("C:\\git\\DRS_PROJEKAT\\ENGINE\\forum.db")
users = [ { 'username': 'milos', 'password':'milos'}]
app.secret_key="hhhhhh"
cursor=database.cursor()
##cursor.execute("""INSERT OR REPLACE INTO  user (id,firstName,lastName,address,country,username,password,phoneNumber,email) VALUES (4,'Emilija','Balaz','Kikinda','Srbija','emily','nestonamadjarskom','brojtelefona','emiliabalazs.ki@gmail.com')""")
##cursor.execute("""DROP TABLE user""")


@app.route('/home', methods=['get'])
def home():
    cursor.execute("select * from topic")
    database.commit()
    postsRAW=cursor.fetchall()
    allPosts=[]
 
    for post in postsRAW:
      cursor.execute("select username from user WHERE id=?",(post[5],))
      database.commit()
      id=cursor.fetchone()
      allPosts.append(ListToDictPost(post,id[0]))


    

    return jsonify(allPosts)

@app.route('/profile', methods=['get','post'])
def profile():
   user=security.token_required(database,app.config["SECRET_KEY"])
   
   return jsonify(user) 


@app.route('/like', methods=['get','post'])
def like():
   user=security.token_required(database,app.config["SECRET_KEY"])
   
   id=request.get_json()
   cursor.execute("""UPDATE topic SET likes=likes+1 where id=?""",(int(id),))
   database.commit()

   liked_topic=[]
   cursor.execute("""SELECT likedTopic from user where id=?""",(user["id"],))
   database.commit()
   liked_topic_JSON=cursor.fetchone()
   
   liked_topic=json.loads(liked_topic_JSON[0])
   liked_topic.append(id)

   cursor.execute("""UPDATE user SET likedTopic=? WHERE id=?""",(json.dumps(liked_topic),user["id"],))
   database.commit()

   return jsonify(user) 


@app.route('/unlike', methods=['get','post'])
def unlike():
   user=security.token_required(database,app.config["SECRET_KEY"])
   
   id=request.get_json()
   cursor.execute("""UPDATE topic SET likes=likes-1 where id=?""",(int(id),))
   database.commit()
  

   liked_topic=[]
   cursor.execute("""SELECT likedTopic from user where id=?""",(user["id"],))
   database.commit()
   liked_topic_JSON=cursor.fetchone()

   liked_topic=json.loads(liked_topic_JSON[0])
   liked_topic.remove(id)

   cursor.execute("""UPDATE user SET likedTopic=? WHERE id=?""",(json.dumps(liked_topic),user["id"],))
   database.commit()
  

   return jsonify(user) 




@app.route('/dislike', methods=['get','post'])
def dislike():
   user=security.token_required(database,app.config["SECRET_KEY"])
   
   id=request.get_json()
   cursor.execute("""UPDATE topic SET dislikes=dislikes+1 where id=?""",(int(id),))
   database.commit()


   disliked_topic=[]
   cursor.execute("""SELECT unlikedTopic from user where id=?""",(user["id"],))
   database.commit()
   disliked_topic_JSON=cursor.fetchone()


   disliked_topic=json.loads(disliked_topic_JSON[0])
   disliked_topic.append(id)

   cursor.execute("""UPDATE user SET unlikedTopic=? WHERE id=?""",(json.dumps(disliked_topic),user["id"],))
   database.commit()

   return jsonify(user)


@app.route('/undislike', methods=['get','post'])
def undislike():
   user=security.token_required(database,app.config["SECRET_KEY"])

   id=request.get_json()
   cursor.execute("""UPDATE topic SET dislikes=dislikes-1 where id=?""",(int(id),))
   database.commit()


   disliked_topic=[]
   cursor.execute("""SELECT unlikedTopic from user where id=?""",(user["id"],))
   database.commit()
   disliked_topic_JSON=cursor.fetchone()


   disliked_topic=json.loads(disliked_topic_JSON[0])
   disliked_topic.remove(id)
   
   cursor.execute("""UPDATE user SET unlikedTopic=? WHERE id=?""",(json.dumps(disliked_topic),user["id"],))
   database.commit()

   return jsonify(user) 


@app.route('/change-data', methods=['get','post'])
def changeData():
  user=security.token_required(database,app.config["SECRET_KEY"])
  user_update=request.get_json()

  cursor.execute("""UPDATE user SET firstName=?,lastName=?,username=?,password=?,country=?,address=?,email=?,phoneNumber=?WHERE id=?""",(user_update['firstName'],user_update['lastName'],user_update['username'],user_update['password'],user_update['country'],user_update['address'],user_update['email'],user_update['phoneNumber'],user['id'],))
  database.commit()

  return jsonify("TRUE")


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method=="POST":
        user=request.get_json()
        cursor.execute("""SELECT * from user""")
        database.commit()
        db_list=cursor.fetchall()
        userr={}
        for i in db_list:
            if(i[8]==user['email'] and i[6]==user['password']):
              cursor.execute("""UPDATE user SET loggedIn='Y'WHERE email=?""",(user['email'],))
              database.commit()
              userr["token"] = jwt.encode(
                    {"id": i[0]},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
              return jsonify(userr);

                
                
                
               
                
        return jsonify("FALSE")


@app.route('/register', methods=['POST','GET'])
def register():
    
    if request.method=="POST":
       
       user=request.get_json()

       cursor.execute("""SELECT * from user""")
       database.commit()
       db_list=cursor.fetchall()
       for i in db_list:
         if(i[6]==user['password']):
           return jsonify("Password already exist! Try different one!")
            
         elif(i[5]==user['username']):
            return jsonify("Username already exist! Try different one!")
        
       cursor.execute("SELECT COALESCE(MAX(id),0) FROM user")
       database.commit()
       oldid=cursor.fetchone()   
       newid = oldid[0] + 1
    

       cursor.execute("""INSERT OR REPLACE INTO  user (id,firstName,lastName,address,country,username,password,phoneNumber,email,loggedIn,likedTopic,unlikedTopic,likedComment,unlikedComment,interests) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(newid,user['firstName'],user['lastName'],user['address'],user['country'],user['username'],user['password'],user['phoneNumber'],user['email'],'N',"[]","[]","[]","[]","[]",))
       database.commit()
       print("user:"+user['username']+"  pasword:"+user['password'])
       sys.stdout.flush()
       return jsonify("Succes!")
           
@app.route('/logout', methods=['GET', 'POST'])
def logout(): 
  user=security.token_required(database,app.config["SECRET_KEY"])
  cursor.execute("""UPDATE user SET loggedIn='N'WHERE username=?""",(user['username'],))
  database.commit()
  return jsonify('TRUE')

@app.route('/add-post', methods=['GET', 'POST'])
def addpost(): 
  user=security.token_required(database,app.config["SECRET_KEY"])
  cursor.execute("SELECT COALESCE(MAX(id),0) FROM topic")
  database.commit()
  oldid=cursor.fetchone()   
  newid = oldid[0] + 1
  
  newPost=request.get_json()
  cursor.execute("""INSERT OR REPLACE INTO  topic (id,title,description,likes,dislikes,user_id) VALUES (?,?,?,?,?,?)""",(newid,newPost['title'],newPost['description'],newPost['likes'],newPost['dislikes'],user['id']))
  database.commit()



  return jsonify('TRUE')





app.run()