import os
from flask import Flask
from dotenv import load_dotenv
from website.models.database import db
from website.routes.main_routes import main_routes

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-key")

db.init_app(app)

# Register the blueprint
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)