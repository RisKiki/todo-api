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

            return sendSuccess({
                'todo_list_id': list_id,
                'todos' : todo_list.asJson()['todo_list']
            })
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
                created_on=datetime.today()
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

    def get(self, list_id: str, todo_id: str):
        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        if len(todo_id) != 24:
            return sendErrorNotFound({"message" : "todo_id id not found"})
        try:
            todo = Todo.objects(id=todo_id).first()

            if todo is None:
                return sendErrorNotFound({"message" : "todo id not found"})

            todo_list = TodoList.objects(id=list_id).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            return sendSuccess({
                'todo' : todo.asJson(),
                'todo_list_id' : todo_list.asJson()['id'],
            })
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

    def delete(self, list_id: str, todo_id: str):
        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        if len(todo_id) != 24:
            return sendErrorNotFound({"message" : "todo_id id not found"})
        try:
            todo = Todo.objects(id=todo_id).first()

            if todo is None:
                return sendErrorNotFound({"message" : "todo id not found"})

            todo_list = TodoList.objects(id=list_id).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            todo.delete()

            todo_list.update(
                pull__todo_list=todo.id
            )

            return sendSuccess({
                'todo_id' : todo_id,
                "list_id" : list_id
            })
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

    def patch(self, list_id: str, todo_id: str):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
        body_parser.add_argument('description', type=str, required=True, help="Missing the description of the list")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        if len(todo_id) != 24:
            return sendErrorNotFound({"message" : "todo_id id not found"})
        try:
            todo = Todo.objects(id=todo_id).first()

            if todo is None:
                return sendErrorNotFound({"message" : "todo id not found"})

            todo_list = TodoList.objects(id=list_id).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})
                
            todo.update(
                name=args['name'],
                description=args['description'],
            )
            
            todo = Todo.objects(id=todo_id).first()

            return sendSuccess({'todo' : todo.asJson()})
        except Exception as err:
            return sendJson(400,str(err),args)


    # Question lucas : 1. les jwt_required | 2. récupere touts les todo d'un liste n'est pas différents de récupère toute la liste ? 