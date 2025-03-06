# src/website/routes/main_routes.py
from flask import Blueprint, jsonify, request
from website.models.database import SessionLocal
from website.models.hotel import Hotel
from ai_agent.crew import AiAgent


main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/hotels')
def get_hotels():
    db = SessionLocal()
    hotels = db.query(Hotel).all()
    db.close()
    return jsonify([{
        "hotel_id": hotel.hotel_id,
        "name": hotel.name,
        "city": hotel.city,
        "country": hotel.country
    } for hotel in hotels])

# @main_routes.route('/run-ai')
# def run_ai():
#     agent = AiAgent()
#     result = agent.run()
#     return jsonify({"result": result})