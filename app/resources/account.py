from flask import request
from flask_restful import Resource, reqparse, abort

class AccountResource(Resource):

    def post(self):
        return 'account/post'