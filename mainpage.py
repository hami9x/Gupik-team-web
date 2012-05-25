import webapp2
from google.appengine.api import users

import common

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        values = {
                    "user": user,
                    "login_url": users.create_login_url("/"),
                }
        self.response.out.write(common.templateRender("main.html", values))
