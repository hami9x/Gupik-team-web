import webapp2

from mainpage import MainPage
from connecthandler import DisconnectHandler, ConnectHandler

app = webapp2.WSGIApplication([ ("/", MainPage),
                                ("/_ah/channel/disconnected/", DisconnectHandler),
                                ("/_ah/channel/connected/", ConnectHandler),
                            ], debug=True)
