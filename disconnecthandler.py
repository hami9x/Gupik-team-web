import webapp2
from google.appengine.api import users
from mainpage import UserOnline

class DisconnectHandler(webapp2.RequestHandler):
    def post(self):
        user = users.User(email = self.request.get("from"))
        q = UserOnline.all().filter("user =", user)
        model = q.get();
        model.online -= 1;
        model.put();
