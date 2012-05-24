import webapp2

from mainpage import MainPage

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
