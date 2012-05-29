import os
import jinja2

from google.appengine.ext import db
from useronline import UserOnline

jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

def render_template(name, values={}):
    return jinjaEnv.get_template(name).render(values)

def user_bootstrap(user):
    UserOnline.check_user(user)
    MyUser.check_user(user)

class MyUser(db.Model):
    id = db.StringProperty()
    email = db.EmailProperty()

    """Create a MyUser object from database, with either email or id"""
    @staticmethod
    def create(email=None, id=None):
        construct_warning = Warning("that user doesn't exist in MyUser database")
        if email != None:
            q = MyUser.all().filter("email =", email).get()
            if not q:
                raise construct_warning
            else:
                return MyUser(id=q.id, email=email)
        elif id != None:
            q = MyUser.all().filter("id =", id).get()
            if not q:
                raise construct_warning
            else:
                return MyUser(id=id, email=q.email)

    """Check if the user exists in MyUser database, if not, add to"""
    @staticmethod
    def check_user(user):
        q = MyUser.all().filter("id =", user.user_id()).get()
        if not q:
            MyUser(id=user.user_id(), email=user.email()).put()
