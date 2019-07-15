from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/events/server'
API_URL = '/static/server.json'

server_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_URL, config={'app_name': 'server'})
server_blueprint.name='name_server'
api = Api(server_blueprint)