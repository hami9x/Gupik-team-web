import webapp2
from google.appengine.api import users
from mainpage import UserOnline

def changeOnlineNumber(handler, fchange):
    user = users.User(email = handler.request.get("from"))
    q = UserOnline.all().filter("user =", user)
    model = q.get()
    model.online = fchange(model.online)
    model.put()

class DisconnectHandler(webapp2.RequestHandler):
    def post(self):
        changeOnlineNumber(self, (lambda x: 0))

class ConnectHandler(webapp2.RequestHandler):
    def post(self):
        changeOnlineNumber(self, (lambda x: 1))
