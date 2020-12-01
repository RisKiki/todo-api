from flask import request
from flask_restful import Resource, reqparse, abort

class TodoResource(Resource):

    def get(self, list_id: int):
        return 'get - /lists/todos/list_id'


class TodoByIdResource(Resource):

    def get(self, list_id: int, todo_id: int):
        return 'get - /lists/todos/list_id/todo_id'

    def put(self, list_id: int, todo_id: int):
        return 'put - /lists/todos/list_id/todo_id'

    def delete(self, list_id: int, todo_id: int):
        return 'delete - /lists/todos/list_id/todo_id'

    def patch(self, list_id: int, todo_id: int):
        return 'patch - /lists/todos/list_id/todo_id'