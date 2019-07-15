from flask import Blueprint
from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

from .namespace1 import api as ns1
from .namepsace2 import api as ns2

blueprint1 = Blueprint('blueprint1', __name__)
get_swaggerui_blueprint()
api1 = Api(blueprint1)
api1.add_namespace(ns1, path='/prefix/of/ns1')
api1.add_namespace(ns2)
