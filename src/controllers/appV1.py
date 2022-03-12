from flask import Blueprint
from flask_restx import Api


from .deviceController import device_ns
from .userController import user_ns 

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,doc='/doc/',
    title='Medical Platform',
    version='1.0',
    description='A medical plaform for doctor-patient interaction',
    # All API metadatas
)

api.add_namespace(device_ns)
api.add_namespace(user_ns)