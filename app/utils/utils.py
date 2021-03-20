from bson import json_util
from flask import request
from app.models import User

import jwt
import json


def sendJson(status : int, message : str, data : any):
    return {
        'status': status,
        'message': message,
        'data' : data
    }

def sendSuccess(data : any):
    return {
        'status': 200,
        'message': 'success',
        'data' : data
    }

def sendErrorNotFound(data : any):
    return {
        'status': 404,
        'message': 'Not found',
        'data' : data
    }

def sendError(error_id : int, error_message : str, data : any):
    return {
        'status': error_id,
        'message': error_message,
        'data' : data
    }

def parse_json(data):
    return json.loads(json_util.dumps(data))

def jwt_auth(f):
  def wrapper(*args, **kwargs):
    try :
        token = request.headers['Authorization']
        payload = User.decode_auth_token(token)
        username = payload['username']
        password = payload['password']
    except jwt.exceptions.InvalidTokenError:
        return sendJson(403, "Invalid token",{})
    except Exception as e:
        raise(e)
    
    try:
        user = User.objects(
            username=username,
            password=password
        ).first()

        if user is None :
            return sendJson(403, "Invalid token",{})

    # Je veux renvoyer user (ou username) à f
    except Exception as err:
        return sendJson(400,str(err),args)

    return f(*args, username, **kwargs)
  return wrapper

def log_autorized(f):
  def wrapper(*args, **kwargs):
    try :
        token = request.headers['Authorization']
        username = User.decode_auth_token(token)
    except jwt.exceptions.InvalidTokenError:
        return sendJson(403, "Invalid token",token)
    except Exception as e:
        raise(e)

    print(f'''
    route : {request.url_rule}
    username : {username}
    body : {request.data}
    ''')
    return f(*args, **kwargs)
  return wrapper

def log_unautorized(f):
  def wrapper(*args, **kwargs):
    print(f'''
    route : {request.url_rule}
    username : Not logged
    body : {request.data}
    ''')
    return f(*args, **kwargs)
  return wrapper
