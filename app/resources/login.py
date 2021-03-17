from flask import request
from flask_restful import Resource, reqparse, abort
from app.models import User
from app.db import db
from app.utils.utils import sendJson, sendSuccess, sendErrorNotFound, log_unautorized

from app import config
from flask_cors import cross_origin


import jwt
import json
from bson import ObjectId, json_util

class LoginResource(Resource):

    @log_unautorized
    def post(self):
        body_parser = reqparse.RequestParser(bundle_errors=True)
        body_parser.add_argument('username', type=str, required=True, help="Missing the login of the user")
        body_parser.add_argument('password', type=str, required=True, help="Missing the password associated to the user login")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception

        try:
            user = User.objects(
                username=args['username']
            ).first()

            if user is None :
                return sendJson(404,"Le mot de passe ou le nom d'utilisateur n'est pas correct (a)", {'username' : args['username']})

            if not User.verify_hash(args['password'], user.password):
                return sendJson(404,"Le mot de passe ou le nom d'utilisateur n'est pas correct", {'username' : args['username']})

            else:
                token = user.encode_auth_token(user.id)

                return sendSuccess({
                    'user' : user.asJson(),
                    'token' : token
                })
        except Exception as err:
            return sendJson(400,str(err),args)
