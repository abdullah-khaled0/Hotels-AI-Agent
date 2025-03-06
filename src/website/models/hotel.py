from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Hotel(Base):
    __tablename__ = 'hotels'
    hotel_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    star_rating = Column(Integer, nullable=False)

    rooms = relationship('Room', back_populates='hotel')