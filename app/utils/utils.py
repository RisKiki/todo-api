def returnJson(status : int, message : str, data : any):
    return {
        'status': status,
        'message': message,
        'data' : data
    }