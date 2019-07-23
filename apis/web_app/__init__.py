from flask import Blueprint
from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/events/web'
API_URL = '/static/web.json'

web_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_URL, config={'app_name': 'web'})
web_blueprint.name='name_web'
api = Api(web_blueprint)

#blueprint1 = Blueprint('blueprint1', __name__)
#get_swaggerui_blueprint()
# api1 = Api(blueprint1)
# api1.add_namespace(ns1, path='/prefix/of/ns1')
# api1.add_namespace(ns2)
