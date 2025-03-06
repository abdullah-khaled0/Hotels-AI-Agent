from flask import Flask
from src.website.routes.main_routes import main_routes
from src.website.routes.api_routes import api_routes
from src.website.routes.admin_routes import admin_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_routes)
app.register_blueprint(api_routes)
app.register_blueprint(admin_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)