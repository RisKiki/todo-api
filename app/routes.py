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
api.add_resource(TodoListByIdResource, '/lists/<int:list_id>')

# Todo
api.add_resource(TodoResource, '/lists/todos/<int:list_id>/<int:todo_id>')
api.add_resource(TodoByIdResource, '/lists/todos/<int:id_list>')



