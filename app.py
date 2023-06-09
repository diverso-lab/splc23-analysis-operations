from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

# Importing routes
from routes.recommender_routes import recommender_bp

# Creating the app and configuring it
app = Flask(__name__)
app.config['API_BASE_URL'] = '/api/v1'

# Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "FLAMAPY API - V1"
    }
)

# Adding blueprints
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(recommender_bp)

@app.route("/", methods=['GET'])
def home():
    return app.send_static_file('home.html')

if __name__ == '__main__':
    app.run()
