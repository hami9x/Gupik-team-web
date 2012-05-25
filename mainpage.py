import webapp2
from google.appengine.api import users
from google.appengine.api import channel
from google.appengine.ext import db

import common

class UserOnline(db.Model):
    user = db.UserProperty()
    online = db.IntegerProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            obj = UserOnline.all().filter("user =", user).get()
            if not obj:
                model = UserOnline(user=user, online=1)
                model.put();

            token = channel.create_channel(user.email())
            online_list = db.GqlQuery("SELECT user FROM UserOnline WHERE online = 1 AND user != :1", user)
            values = {
                        "user": user,
                        "token": token,
                        "online_list": online_list,
                    }
        else:
            values = {
                        "user": user,
                        "login_url": users.create_login_url("/"),
                    }
        self.response.out.write(common.templateRender("main.html", values))
