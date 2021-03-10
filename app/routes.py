from app import api

from app.resources.login import LoginResource
from app.resources.account import AccountResource
from app.resources.todo_list import TodoListResource, TodoListByIdResource
from app.resources.todo import TodoResource, TodoByIdResource

# Account
api.add_resource(AccountResource, '/account')

# Login
api.add_resource(LoginResource, '/login')

# Todo lists
api.add_resource(TodoListResource, '/lists')
api.add_resource(TodoListByIdResource, '/lists/<string:list_id>')

# Todo
api.add_resource(TodoResource, '/lists/todos/<string:list_id>')
api.add_resource(TodoByIdResource, '/lists/todos/<string:list_id>/<string:todo_id>')



