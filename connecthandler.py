import logging
import json
import webapp2
from google.appengine.api import users
from google.appengine.api import channel
from google.appengine.api import memcache

from useronline import UserOnline
from common import MyUser

def reaction(handler, f_status_change):
    user = users.User(email = handler.request.get("from"))
    q = UserOnline.all().filter("user =", user)
    model = q.get()
    model.online = f_status_change(model.online)
    model.put()

    #Now send message to client
    message = {
                "type": "onlineStatus",
                "uid": MyUser.create(user.email()).id,
                "on": model.online,
            }
    if model.online:
        message["nickname"] = user.nickname()
    json_msg = json.dumps(message)

    q = UserOnline.get_online_list()

    #Update the list of online user in memcache for others to use
    online_list = q.fetch(20)
    if memcache.get("online_list") == None:
        if not memcache.add("online_list", online_list):
            raise Warning("memcache add doens't work")
    else:
        memcache.set("online_list", online_list)
    for item in q:
        if user.email() != item.user.email():
            logging.info("Send msg to: "+item.user.email()+"; "+json_msg)
            channel.send_message(item.user.email(), json_msg)

class DisconnectHandler(webapp2.RequestHandler):
    def post(self):
        reaction(self, (lambda x: 0))

class ConnectHandler(webapp2.RequestHandler):
    def post(self):
        reaction(self, (lambda x: 1))
