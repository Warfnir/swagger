from flask import Blueprint
from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

from .namespace1 import api as ns1
from .namepsace2 import api as ns2

SWAGGER_URL = '/events/gift'
API_URL = '/static/gift.json'

gift_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_URL, cofig={'app_name': 'web'})
api = Api(gift_blueprint)

# api1.add_namespace(ns1, path='/prefix/of/ns1')
# api1.add_namespace(ns2)
