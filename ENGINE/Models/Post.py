class Post():
    id=None
    title = None
    description = None
    likes = None
    dislikes = None
    user_id = None
    

     #konsutrktor sa poljima
    def __init__(self,id, title, description, likes, dislikes, user_id,):
        self.id=id
        self.title = title
        self.description = description
        self.likes = likes
        self.dislikes = dislikes
        self.user_id = user_id
       


def ListToDictPost(list,username):
    dict={
        "id":list[0],
        "title":list[1],
        "description":list[2],
        "likes":list[3],
        "dislikes":list[4],
        "user_id":list[5],
        "user":username,
        
    }
    return dict