from flask import request
from flask_restful import Resource, reqparse, abort

from datetime import datetime
from app.models import TodoList, Todo

from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound

class TodoResource(Resource):

    def get(self, list_id: str):
        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        try:
            todo_list = TodoList.objects(id=list_id).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            return sendSuccess({'todos' : todo_list.asJson()['todo_list']})
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

    def put(self, list_id: str):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
        body_parser.add_argument('description', type=str, required=True, help="Missing the description of the list")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})

        try:
            todo_list = TodoList.objects(id=list_id).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            todo = Todo(
                name=args['name'],
                description = args['name'],
                created_on=datetime.today().strftime("%d/%m/%Y %H:%M:%S.%f")
            ).save()

            todo_list.update(
                push__todo_list=todo
            )

            updated_todo_list = TodoList.objects(id=list_id).first()

            return sendSuccess({
                "todo" : todo.asJson(),
                "updated_todo_list" : updated_todo_list.asJson()
            })
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

        


class TodoByIdResource(Resource):

    def get(self, list_id: str, todo_id: int):
        return 'get - /lists/todos/list_id/todo_id'

    def delete(self, list_id: str, todo_id: int):
        return 'delete - /lists/todos/list_id/todo_id'

    def patch(self, list_id: str, todo_id: int):
        return 'patch - /lists/todos/list_id/todo_id'


    # Question lucas : 1. les jwt_required | 2. récupere touts les todo d'un liste n'est pas différents de récupère toute la liste ? 