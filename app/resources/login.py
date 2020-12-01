from flask import request
from flask_restful import Resource, reqparse, abort

class LoginResource(Resource):

    def post(self):
        return 'login/post'