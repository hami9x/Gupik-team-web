from datetime import datetime
import webapp2
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.api import channel
from google.appengine.ext import db

from common import render_template

class ChatMessage(db.Model):
    nickname = db.StringProperty()
    when_created = db.DateTimeProperty(auto_now_add = True)
    content = db.TextProperty()

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

    def post(self):
        content = self.request.get("text")
        now = datetime.utcnow()
        time_str = now.strftime("%Y:%m:%d:%H:%M")
        nickname = self.request.get("nickname")
        obj = ChatMessage(when_created=now, content=content, nickname=nickname)
        obj.put()

        online_list = memcache.get("online_list") # This memcache variable is updated by ConnectHandler
        if online_list == None:
            raise Warning("Something wrong here, online_list isn't updated by ConnectHandler")

        message = {
                "type": "chatMsg",
                "nickname": nickname,
                "time": time_str,
                "content": content,
                }
        for item in online_list:
            channel.send_message(item.user.email(), message)
