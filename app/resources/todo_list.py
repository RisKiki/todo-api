from flask import request
from flask_restful import Resource, reqparse, abort

from app.models import TodoList
from datetime import datetime

from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound

class TodoListResource(Resource):

    def get(self):
        return sendSuccess(list(map(lambda todoList: todoList.asJson(), TodoList.objects())))

    def put(self):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

        try:
            if 'todo_list' in args:
                todo_list = TodoList(
                    name=args['name'],
                    todo_list=args['todo_list'],
                    created_on=datetime.today().strftime("%d/%m/%Y %H:%M:%S.%f")
                ).save()
            else :
                todo_list = TodoList(
                    name=args['name'],
                    todo_list=[],
                    created_on=datetime.today().strftime("%d/%m/%Y %H:%M:%S.%f")
                ).save()
            return sendSuccess({'todo_list' : todo_list.asJson()})
        except Exception as err:
            return sendJson(400,str(err),args)


class TodoListByIdResource(Resource):

    def get(self, list_id: int):
        return 'get - /lists/list_id'

    # def put(self,list_id: int):
    #     body_parser = reqparse.RequestParser(bundle_errors=True)
    #     body_parser.add_argument('name', type=str, required=True, help="Missing the name of the list")
    #     args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

    #     try:
    #         if todo_list in args:
    #             todo_list = TodoList(name=args['todo_list'],todo_list=args['todo_list'], create_on=datetime.today()).save()
    #         else :
    #             todo_list = TodoList(name=args['todo_list'],todo_list=[], create_on=datetime.today()).save()
    #         return sendSuccess({'todo_list' : todo_list.asJson()})
    #     except Exception as err:
    #         return sendJson(400,str(err),args)

    def delete(self, list_id: int):
        return 'delete - /lists/list_id'

    def patch(self, list_id: int):
        return 'patch - /lists/list_id'