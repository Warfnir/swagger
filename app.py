import json
import os
import traceback

from flask import Flask, request, abort

from platforms_registration import register_blueprints, create_directiories
from swagger_content_modifier import process_request, generate_new_swagger_file

app = Flask(__name__)

@app.route('/allevents', methods=['POST'])
def parse_request():
    try:
        data = request.get_json()
        process_request(data)
        return "Request processed"
    except Exception :
        traceback.print_exc()
        abort(500, "Something went wrong.")

@app.before_first_request
def initialize_swagger_files():
    platforms = os.listdir('./platforms_branches')
    try:
        platforms.pop(platforms.index('.gitignore'))
    except Exception:
        pass
    for platform in platforms:
        new_content = generate_new_swagger_file(platform)
        with open(f'./static/{platform}.json', 'w') as file:
            json.dump(new_content, file)


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    create_directiories()
    register_blueprints(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
