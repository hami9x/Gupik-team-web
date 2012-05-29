import json
from datetime import datetime
import webapp2
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.api import channel
from google.appengine.ext import db

import common
from useronline import UserOnline

class ChatMessage(db.Model):
    nickname = db.StringProperty()
    when_created = db.DateTimeProperty(auto_now_add = True)
    content = db.TextProperty()

class Chatbox(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        config = {
                 "height": 500,
                 "nmessage": 30, #The number of chat messages in history displayed to the client at first
            }


        values = {
                    "user": user,
                    "online_list": UserOnline.get_online_list(),
                    "config": config,
                }

        values2 = {}
        if user:
            common.user_bootstrap(user)
            token = channel.create_channel(user.email())
            messages = db.GqlQuery("SELECT * FROM ChatMessage ORDER BY when_created DESC LIMIT %s" % config["nmessage"])
            values2 = {
                    "token": token,
                    "logout_url": users.create_logout_url("/chatbox"),
                    "messages": messages,
                    "f_simple_time_str": self.simple_time_str,
                    "online_list": UserOnline.get_online_list(),
                }
        else:
            values2 = {
                    "login_url": users.create_login_url("/chatbox"),
                }
        values.update(values2)
        self.response.out.write(common.render_template("chatbox.html", values))

    @staticmethod
    def simple_time_str(time):
        return time.strftime("%Y:%m:%d:%H:%M")

    def post(self):
        content = self.request.get("text")
        now = datetime.utcnow()
        time_str = self.simple_time_str(now)
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
            channel.send_message(item.user.email(), json.dumps(message))
