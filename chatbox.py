import webapp2
from google.appengine.api import users
from common import render_template

class Chatbox(webapp2.RequestHandler):
    def get(self):
        values = {
                "user": users.get_current_user(),
                "login_url": users.create_login_url("/chatbox"),
                "logout_url": users.create_logout_url("/chatbox"),
                "config": {
                    "height": 500,
                    },
                }
        self.response.out.write(render_template("chatbox.html", values))
