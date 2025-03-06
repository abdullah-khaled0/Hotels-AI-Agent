from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Guest(Base):
    __tablename__ = 'guests'
    guest_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(255))
    city = Column(String(100))
    country = Column(String(100))

    reservations = relationship('Reservation', back_populates='guest')