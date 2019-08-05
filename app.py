import json
import os
import traceback

from flask import Flask, request, abort

from platforms_registration import register_blueprints, create_directiories
from swagger_content_modifier import process_request, generate_new_swagger_file
from volume_connector import get_volume_path

app = Flask(__name__)

volume_path = get_volume_path(os.environ.get('VOLUME','swagger-volume'))

@app.route('/allevents', methods=['POST'])
def parse_request():
    try:
        data = request.get_json()
        process_request(data, volume_path)
        return "Request processed"
    except Exception :
        traceback.print_exc()
        abort(500, "Something went wrong.")

@app.before_first_request
def initialize_swagger_files():
    for platform in os.listdir(volume_path+'/platforms_branches'):
        new_content = generate_new_swagger_file(platform, volume_path)
        with open(f'./static/{platform}.json', 'w') as file:
            json.dump(new_content, file)


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    create_directiories(volume_path)
    register_blueprints(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
