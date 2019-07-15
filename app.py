from flask import Flask
from apis.gift import gift_blueprint, SWAGGER_URL as gift_url
from apis.mobile_app import blueprint2 as api2
from apis.web_app import blueprint1 as api1


app = Flask(__name__)
app.register_blueprint(gift_blueprint, url_prefix=gift_url)
app.register_blueprint(api1, url_prefix='/api1/1')
app.register_blueprint(api2, url_prefix='/api2/1')

app.run(debug=True)