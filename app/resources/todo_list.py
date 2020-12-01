from flask import request
from flask_restful import Resource, reqparse, abort

class TodoListResource(Resource):

    def get(self):
        return 'get - /lists'


class TodoListByIdResource(Resource):

    def get(self, list_id: int):
        return 'get - /lists/list_id'

    def put(self,list_id: int):
        return 'put - /lists/list_id'

    def delete(self, list_id: int):
        return 'delete - /lists/list_id'

    def patch(self, list_id: int):
        return 'patch - /lists/list_id'