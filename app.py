import json
import os

from flask import Flask, request
from apis.gift import gift_blueprint, SWAGGER_URL as gift_url
from apis.mobile_app import mobile_blueprint, SWAGGER_URL as mobile_url
from apis.web_app import web_blueprint, SWAGGER_URL as web_url
from apis.server import server_blueprint, SWAGGER_URL as server_url
from swagger_content_operator import process_request, generate_new_swagger_file

app = Flask(__name__)
app.debug = True
app.register_blueprint(gift_blueprint, url_prefix=gift_url)
app.register_blueprint(mobile_blueprint, url_prefix=mobile_url)
app.register_blueprint(web_blueprint, url_prefix=web_url)
app.register_blueprint(server_blueprint, url_prefix=server_url)


@app.route('/allevents', methods=['POST'])
def parse_request():
    data = request.get_json()
    process_request(data)
    return "request processed"


@app.before_first_request
def initialize_files():
    for platform in os.listdir(f'./platforms_branches'):
        print(platform)
        new_content = generate_new_swagger_file({"jsonData": {}, "branch": '', "platform": platform})
        with open(f'./static/{platform}.json', 'w') as file:
            json.dump(new_content, file)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
