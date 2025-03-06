from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.hotel_id', ondelete='CASCADE'))
    room_number = Column(String(10), nullable=False)
    room_type = Column(String(50), nullable=False)
    price_per_night = Column(Numeric(10, 2), nullable=False)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)

    hotel = relationship('Hotel', back_populates='rooms')
    reservations = relationship('Reservation', back_populates='room')