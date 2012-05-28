import webapp2

from mainpage import MainPage
from chatbox import Chatbox
from connecthandler import DisconnectHandler, ConnectHandler

app = webapp2.WSGIApplication([ ("/", MainPage),
                                ("/chatbox", Chatbox),
                                ("/_ah/channel/disconnected/", DisconnectHandler),
                                ("/_ah/channel/connected/", ConnectHandler),
                            ], debug=True)
