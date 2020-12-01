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
        'status': 200,
        'message': 'success',
        'data' : data
    }
