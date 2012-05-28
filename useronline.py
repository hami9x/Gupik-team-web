from google.appengine.ext import db

class UserOnline(db.Model):
    user = db.UserProperty()
    online = db.IntegerProperty()

    @staticmethod
    def get_online_list():
        return db.GqlQuery("SELECT user FROM UserOnline WHERE online = 1")

    @staticmethod
    def check_user(user):
        q = UserOnline.all().filter("user =", user).get()
        if not q:
            model = UserOnline(user=user, online=1)
            model.put()
