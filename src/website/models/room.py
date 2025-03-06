from website.models.database import db

class Room(db.Model):
    __tablename__ = 'rooms'

    room_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.hotel_id', ondelete='CASCADE'))
    room_number = db.Column(db.String(10), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Numeric(10, 2), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    hotel = db.relationship('Hotel', back_populates='rooms')
    reservations = db.relationship('Reservation', back_populates='room', cascade="all, delete")

    def __repr__(self):
        return f"<Room(id={self.room_id}, number={self.room_number})>"
