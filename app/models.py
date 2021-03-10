from app.db import db
from app import config
import jwt
import datetime

class Todo(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    created_on = db.DateTimeField(required=True)

    def asJson(self):
        return {
            "id":str(super().id),
            "name":self.name,
            "created_on":self.created_on.strftime("%d/%m/%Y %H:%M:%S.%f"),
        }

class TodoList(db.Document):
    name = db.StringField(required=True)
    todo_list = db.ListField(db.ReferenceField('Todo'))
    created_on = db.DateTimeField(required=True)

    def asJson(self):
        return {
            "id":str(super().id),
            "name":self.name,
            "todo_list" :dict(map(lambda todo: todo.asJson(), self.todo_list)),
            "created_on":self.created_on.strftime("%d/%m/%Y %H:%M:%S.%f"),
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
    
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """

        payload = {
            "username" : self.username,
            "password" : self.password
        }

        return jwt.encode(
            payload,
            config.SECRET_KEY,
            algorithm='HS256'
        )


    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY, algorithms=['HS256'])
            return payload['username']
        except jwt.ExpiredSignatureError as e1:
            raise e1
        except jwt.InvalidTokenError as e2:
            raise e2
