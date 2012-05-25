import webapp2

from mainpage import MainPage
from disconnecthandler import DisconnectHandler

app = webapp2.WSGIApplication([ ("/", MainPage),
                                ("/_ah/channel/disconnected/", DisconnectHandler)
                            ], debug=True)
