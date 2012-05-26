import logging
import json
import webapp2
from google.appengine.api import users
from google.appengine.api import channel
from google.appengine.ext import db
from mainpage import UserOnline
from common import MyUser

def reaction(handler, f_status_change):
    user = users.User(email = handler.request.get("from"))
    q = UserOnline.all().filter("user =", user)
    model = q.get()
    model.online = f_status_change(model.online)
    model.put()

    #Now send message to client
    message = {
                "uid": MyUser.create(user.email()).id,
                "on": model.online,
            }
    if model.online:
        message["nickname"] = user.nickname()
    json_msg = json.dumps(message)
    q = db.GqlQuery("SELECT user FROM UserOnline WHERE online = 1 AND user != :1", user)
    for item in q:
        channel.send_message(item.user.email(), json_msg)

class DisconnectHandler(webapp2.RequestHandler):
    def post(self):
        reaction(self, (lambda x: 0))

class ConnectHandler(webapp2.RequestHandler):
    def post(self):
        reaction(self, (lambda x: 1))
