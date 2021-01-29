from app.db import db

class Todo(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    created_on = db.DateTimeField(required=True)

    def asJson(self):
        return {
            "id":str(self.id),
            "name":self.name,
            "created_on":self.created_on.strftime("%d/%m/%Y %H:%M:%S.%f"),
        }

class TodoList(db.Document):
    name = db.StringField(required=True)
    todo_list = db.ListField(db.ReferenceField('Todo'))
    created_on = db.DateTimeField(required=True)

    def asJson(self):
        return {
            "id":str(self.id),
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