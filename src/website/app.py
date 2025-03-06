import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from website.models.database import db
from website.models.guest import Guest
from website.models.hotel import Hotel
from website.models.room import Room
from website.models.reservation import Reservation

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-key")


db.init_app(app)


@app.route('/')
def index():
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

@app.route('/hotel/<int:hotel_id>')
def hotel_details(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    rooms = Room.query.filter_by(hotel_id=hotel_id, is_available=True).all()
    return render_template('hotel_details.html', hotel=hotel, rooms=rooms)

@app.route('/room/<int:room_id>', methods=['GET', 'POST'])
def room_details(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        guest_email = request.form.get('guest_email')  # Get guest email from form

        # Find guest by email or create a new one
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

        from datetime import datetime
        check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_date, "%Y-%m-%d")

        total_price = room.price_per_night * max((check_out - check_in).days, 1)

        reservation = Reservation(
            guest_id=guest.guest_id,  # ✅ Store guest_id instead of guest_name
            room_id=room.room_id,
            check_in_date=check_in,
            check_out_date=check_out,
            total_price=total_price,
            status='Confirmed'
        )
        db.session.add(reservation)
        db.session.commit()

        flash(f"Reservation confirmed for {room.room_type} from {check_in_date} to {check_out_date}!", "success")
        return redirect(url_for('index'))
    
    return render_template('room_details.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
