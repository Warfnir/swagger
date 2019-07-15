from flask import Flask
from apis.gift import gift_blueprint, SWAGGER_URL as gift_url
from apis.mobile_app import mobile_blueprint, SWAGGER_URL as mobile_url
from apis.web_app import web_blueprint, SWAGGER_URL as web_url
from apis.server import server_blueprint, SWAGGER_URL as server_ur;


app = Flask(__name__)
app.register_blueprint(gift_blueprint, url_prefix=gift_url)
app.register_blueprint(mobile_blueprint, url_prefix=mobile_url)
app.register_blueprint(web_blueprint, url_prefix=web_url)
app.register_blueprint(server_blueprint,url_prefix=server_ur)

app.run(debug=True)