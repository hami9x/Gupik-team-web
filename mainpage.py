import webapp2
from google.appengine.api import users
from google.appengine.api import channel

from common import render_template
from common import MyUser
from useronline import UserOnline

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            UserOnline.check_user(user)
            MyUser.check_user(user)
            token = channel.create_channel(user.email())
            values = {
                        "user": user,
                        "token": token,
                        "online_list": UserOnline.get_online_list(),
                    }
        else:
            values = {
                        "user": user,
                        "login_url": users.create_login_url("/"),
                    }
        self.response.out.write(render_template("mainpage.html", values))
