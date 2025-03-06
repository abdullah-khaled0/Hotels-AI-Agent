from flask import Blueprint, render_template
from src.website.models.database import SessionLocal
from src.website.models.hotel import Hotel

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    db = SessionLocal()
    hotels = db.query(Hotel).all()
    db.close()
    return render_template('index.html', hotels=hotels)