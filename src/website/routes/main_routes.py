# src/website/routes/main_routes.py
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from website.models.database import db
from website.models.hotel import Hotel
from website.models.guest import Guest
from website.models.room import Room
from website.models.reservation import Reservation
from ai_agent.crew import run
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from datetime import datetime

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

@main_routes.route('/hotel/<int:hotel_id>')
def hotel_details(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    rooms = Room.query.filter_by(hotel_id=hotel_id, is_available=True).all()
    return render_template('hotel_details.html', hotel=hotel, rooms=rooms)

@main_routes.route('/room/<int:room_id>', methods=['GET', 'POST'])
def room_details(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        guest_email = request.form.get('guest_email')
        
        guest = Guest.query.filter_by(email=guest_email).first()
        if not guest:
            guest = Guest(
                first_name=request.form.get('first_name'),
                last_name=request.form.get('last_name'),
                email=guest_email,
                phone=request.form.get('phone'),
                address=request.form.get('address'),
                city=request.form.get('city'),
                country=request.form.get('country')
            )
            db.session.add(guest)
            db.session.commit()

        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')

        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")

        total_price = room.price_per_night * max((check_out - check_in).days, 1)

        reservation = Reservation(
            guest_id=guest.guest_id,
            room_id=room.room_id,
            check_in_date=check_in,
            check_out_date=check_out,
            total_price=total_price,
            status='Confirmed'
        )
        db.session.add(reservation)
        db.session.commit()

        flash(f"Reservation confirmed for {room.room_type} from {check_in_date} to {check_out_date}!", "success")
        return redirect(url_for('main_routes.index'))
    
    return render_template('room_details.html', room=room)

@main_routes.route('/reservations')
def reservations():
    reservations = (Reservation.query
                    .join(Room)
                    .join(Hotel)
                    .order_by(Reservation.check_in_date)
                    .all())
    return render_template('reservations.html', reservations=reservations)

@main_routes.route('/delete_reservation/<int:reservation_id>', methods=['GET'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    
    try:
        db.session.delete(reservation)
        db.session.commit()
        flash('Reservation deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting reservation: {str(e)}', 'error')
    
    return redirect(url_for('main_routes.reservations'))

@main_routes.context_processor
def inject_reservation_count():
    reservations = Reservation.query.all()
    reservation_count = len(reservations)
    return dict(reservation_count=reservation_count)

@main_routes.route('/query', methods=['POST'])
def query_agent():
    data = request.json
    user_query = data.get("query")
    
    text_source = TextFileKnowledgeSource(file_paths="../knowledge/database_schema.txt")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    
    input = {
        "query": user_query,
        "schema": f"{text_source.content}"
    }

    result = run(input)
    return jsonify({"result": str(result)})