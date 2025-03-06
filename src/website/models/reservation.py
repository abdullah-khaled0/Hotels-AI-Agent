from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric, String
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'
    reservation_id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('guests.guest_id', ondelete='CASCADE'))
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='CASCADE'))
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), default='Pending')

    guest = relationship('Guest', back_populates='reservations')
    room = relationship('Room', back_populates='reservations')