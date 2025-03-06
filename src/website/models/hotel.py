from website.models.database import db

class Hotel(db.Model):
    __tablename__ = 'hotels'

    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    star_rating = db.Column(db.Integer, nullable=False)

    rooms = db.relationship('Room', back_populates='hotel', cascade="all, delete")

    def __repr__(self):
        return f"<Hotel(id={self.hotel_id}, name={self.name})>"
