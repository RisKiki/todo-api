from flask import request
from flask_restful import Resource, reqparse, abort

from app.services.todoService import TODOS
from app.models import Todo

from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound

class TodoListResource(Resource):

    def get(self):
        return sendSuccess(list(map(lambda todo: todo.asJson(), Todo.objects())))


class TodoListByIdResource(Resource):

    def get(self, list_id: int):
        res = next((todo for todo in TODOS if todo['id'] == list_id), None)
        return sendSuccess(res) if res else sendErrorNotFound({'list_id': list_id})

    def put(self,list_id: int):
        return 'put - /lists/list_id'

    def delete(self, list_id: int):
        return 'delete - /lists/list_id'

    def patch(self, list_id: int):
        return 'patch - /lists/list_id'