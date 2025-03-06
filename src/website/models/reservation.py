from website.models.database import db

class Reservation(db.Model):
    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.guest_id', ondelete='CASCADE'))  # ✅ Fixed ForeignKey
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.room_id', ondelete='CASCADE'))
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), default='Pending')

    guest = db.relationship('Guest', back_populates='reservations')  # ✅ Added relationship
    room = db.relationship('Room', back_populates='reservations')

    def __repr__(self):
        return f"<Reservation(id={self.reservation_id}, guest_id={self.guest_id}, room={self.room_id})>"
