from flask import Blueprint, jsonify
from src.website.models.database import SessionLocal
from src.website.models.room import Room

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/rooms/<int:hotel_id>')
def get_rooms(hotel_id):
    db = SessionLocal()
    rooms = db.query(Room).filter(Room.hotel_id == hotel_id, Room.is_available == True).all()
    db.close()
    return jsonify([{
        'room_id': room.room_id,
        'room_number': room.room_number,
        'room_type': room.room_type,
        'price_per_night': float(room.price_per_night),
        'capacity': room.capacity
    } for room in rooms])