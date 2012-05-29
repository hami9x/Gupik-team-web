import webapp2
from google.appengine.api import users
from google.appengine.api import channel

import common
from useronline import UserOnline

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            common.user_bootstrap(user)
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
        self.response.out.write(common.render_template("mainpage.html", values))
