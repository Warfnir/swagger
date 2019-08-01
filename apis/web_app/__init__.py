from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/events/web'
API_URL = '/static/web.json'

web_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'web'})
web_blueprint.name = 'name_web'
api = Api(web_blueprint)
