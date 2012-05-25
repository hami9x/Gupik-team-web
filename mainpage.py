import webapp2
from google.appengine.api import users
from google.appengine.api import channel
from google.appengine.ext import db

import common

class UserOnline(db.Model):
    user = db.UserProperty()
    online = db.BooleanProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        online = UserOnline.all().filter("user =", user).get()
        if not online:
            model = UserOnline(user=user, online=True)
            model.put();
        else:
            online.online = True
            online.put()
        token = channel.create_channel(user.user_id())
        online_list = db.GqlQuery("SELECT user FROM UserOnline WHERE online = TRUE")
        values = {
                    "user": user,
                    "login_url": users.create_login_url("/"),
                    "token": token,
                    "online_list": online_list,
                }
        self.response.out.write(common.templateRender("main.html", values))
