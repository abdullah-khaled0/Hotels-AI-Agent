from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.hotel_id', ondelete='CASCADE'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hire_date = Column(Date, nullable=False)