from flask import request
from flask_restful import Resource, reqparse, abort

from app.models import TodoList
from datetime import datetime

from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound, jwt_auth, log_autorized


class TodoListResource(Resource):

    @log_autorized
    @jwt_auth
    def get(self, username):
        try:
            liste = list(map(lambda todoList: todoList.asJson(), TodoList.objects(username=username)))
            return sendSuccess(liste)
        except Exception as e:
            raise(e)

    @log_autorized  
    @jwt_auth
    def put(self, username):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
        args = body_parser.parse_args(strict=False) # Accepted only if these two parameters are strictly declared in body else raise exception

        try:
            if 'todo_list' in args:
                todo_list = TodoList(
                    name=args['name'],
                    todo_list=args['todo_list'],
                    username=username, 
                    created_on=datetime.today()
                ).save()
            else :
                todo_list = TodoList(
                    name=args['name'],
                    todo_list=[],
                    username=username,
                    created_on=datetime.today()
                ).save()
            return sendSuccess({'todo_list' : todo_list.asJson()})
        except Exception as err:
            return sendJson(400,str(err),args)


class TodoListByIdResource(Resource):

    @log_autorized
    @jwt_auth
    def get(self, username, list_id: str):
        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        try:
            todo_list = TodoList.objects(id=list_id, username=username).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            return sendSuccess({'todo_list' : todo_list.asJson()})
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

    @log_autorized
    @jwt_auth
    def delete(self, username, list_id: str):
        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        try:
            todo_list = TodoList.objects(id=list_id, username=username).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})

            for todo in todo_list.todo_list:
                todo.delete()

            todo_list.delete()
            return sendSuccess({'todo_list_id' : list_id})
        except Exception as err:
            return sendJson(400,str(err),{"list_id":list_id})

    @log_autorized
    @jwt_auth
    def patch(self, username, list_id: str):

        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
        args = body_parser.parse_args(strict=False) # Accepted only if these two parameters are strictly declared in body else raise exception

        if len(list_id) != 24:
            return sendErrorNotFound({"message" : "todo_list id not found"})
        try:
            todo_list = TodoList.objects(id=list_id, username=username).first()

            if todo_list is None:
                return sendErrorNotFound({"message" : "todo_list id not found"})
                
            if 'todo_list' in args:
                todo_list.update(
                    name=args['name'],
                    todo_list=args['todo_list'],
                )
            else:
                todo_list.update(
                    name=args['name'],
                )
            
            todo_list = TodoList.objects(id=list_id).first()

            return sendSuccess({'todo_list' : todo_list.asJson()})
        except Exception as err:
            return sendJson(400,str(err),args)