import os
import traceback
from flask_swagger_ui import get_swaggerui_blueprint

def create_directiories():
    platforms = [p for p in os.environ.get('PLATFORMS', "web server mobile gift").split(" ")]
    for platform in platforms:
        try:
            os.mkdir(f'./platforms_branches/{platform}')
        # It might already exists
        except FileExistsError:
            pass

def register_blueprints(app):
    platforms = os.listdir('./platforms_branches')
    for platform in platforms:
        try:
            SWAGGER_URL = f'/events/{platform}'
            API_URL = f'/static/{platform}.json'
            platform_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={})
            platform_blueprint.name = platform
            app.register_blueprint(platform_blueprint, url_prefix=SWAGGER_URL)
        except Exception:
            traceback.print_exc()

