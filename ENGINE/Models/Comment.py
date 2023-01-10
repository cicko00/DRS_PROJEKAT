class Comment():
    id=None
    desc = None
    user_id = None
    topic_id = None

     #konsutrktor sa poljima
    def __init__(self,id, desc, user_id, topic_id):
        self.id=id
        self.desc = desc
        self.user_id = user_id
        self.topic_id = topic_id

    
def ListToDictComment(list,username,topic_name):
    dict={
        "id":list[0],
        "desc":list[1],
        "user_id":list[2],
        "topic_id":list[3],
        "user":username,
        "topic":topic_name
        
    }
    return dict