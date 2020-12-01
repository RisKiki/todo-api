from app.db import db

import mongoengine_goodjson as gj

class Todo(gj.Document):
    name = db.StringField(required=True)
    created_on = db.DateTimeField(required=True)

    def asJson(self):
        return {
            "id":str(self.id),
            "name":self.name,
            "created_on":self.created_on
        }

class User(db.Document):
    username = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)

    def asJson(self):
        return {
            "id":str(self.id),
            "username":self.username,
            "password":self.password
        }