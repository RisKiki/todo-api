import os

env = "DEVELOPMENT"
PRODUCTION_SERVER= "172.17.4.154" # Un exemple
API_NAME = "Flask API TODO"
APP_VERSION = "1.0"
SECRET_KEY = "ad241ds546Zz65d*sQs)$s!qzQSds$qsd"

class BaseConfig(object):
    DEBUG = True
    #MONGO Configuration
    MONGODB_HOST = os.environ['MONGO_URI']


class DevelopmentConfig(BaseConfig):
    # SWAGGER Configuration
    SWAGGER_URL = '/api/docs'
    DATA_SWAGGER = 'http://localhost:5000/swagger'

class ProductionConfig(BaseConfig):
    DEBUG = False
    # SWAGGER Configuration
    SWAGGER_URL = '/api/docs'
    DATA_SWAGGER = 'http://' + PRODUCTION_SERVER + ':5000/swagger'
