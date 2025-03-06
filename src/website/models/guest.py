from website.models.database import db

class Guest(db.Model):
    __tablename__ = 'guests'

    guest_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    reservations = db.relationship('Reservation', back_populates='guest', cascade="all, delete")  # ✅ Fixed

    def __repr__(self):
        return f"<Guest(id={self.guest_id}, name={self.first_name} {self.last_name})>"
