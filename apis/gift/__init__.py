from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/events/gift'
API_URL = '/static/gift.json'

gift_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'gift'})
gift_blueprint.name = 'name_gift'
api = Api(gift_blueprint)
