from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/events/mobile'
API_URL = '/static/mobile.json'

mobile_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'mobile'})
mobile_blueprint.name = 'name_mobile'
api = Api(mobile_blueprint)
