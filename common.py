import os
import jinja2

from google.appengine.ext import db

jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

def templateRender(name, values={}):
    return jinjaEnv.get_template(name).render(values)

class MyUser(db.Model):
    id = db.StringProperty()
    email = db.EmailProperty()

    """Create a MyUser object from database, with either email or id"""
    @staticmethod
    def create(email=None, id=None):
        construct_warning = Warning("that user doesn't exist in MyUser database")
        if email != None:
            q = db.GqlQuery("SELECT id FROM MyUser WHERE email = :1", email).get();
            if not q:
                raise construct_warning
            else:
                return MyUser(id=q.id, email=email)
        elif id != None:
            q = db.GqlQuery("SELECT email FROM MyUser WHERE id = :1", id).get();
            if not q:
                raise construct_warning
            else:
                return MyUser(id=id, email=q.email)
