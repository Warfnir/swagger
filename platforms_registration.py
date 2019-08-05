import os
import traceback

from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint


def prepare_blueprints(app):
    platforms = [p for p in os.environ.get('PLATFORMS', "web server mobile gift").split(" ")]
    for platform in platforms:
        try:
            os.mkdir(f'./platforms_branches/{platform}')
        # It might already exists
        except FileExistsError:
            pass

        try:
            SWAGGER_URL = f'/events/{platform}'
            API_URL = f'/static/{platform}.json'
            platform_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
            platform_blueprint.name = platform
            app.register_blueprint(platform_blueprint, url_prefix=SWAGGER_URL)
        except Exception:
            traceback.print_exc()

