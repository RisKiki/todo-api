from flask import request
from flask_restful import Resource, reqparse, abort

from app.models import User

from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound

class AccountResource(Resource):

    def post(self):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('username', type=str, required=True, help="Missing the login of the user")
        body_parser.add_argument('password', type=str, required=True, help="Missing the password associated to the user login")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

        try:
            user = User(username=args['username'],password=args['password']).save()
            return sendSuccess({'user' : user.asJson()})
        except Exception as err:
            return sendJson(400,str(err),args)
        