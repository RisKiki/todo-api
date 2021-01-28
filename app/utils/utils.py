from bson import json_util
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