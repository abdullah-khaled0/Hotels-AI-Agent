from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, TIMESTAMP
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.reservation_id', ondelete='CASCADE'))
    payment_date = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(20), default='Pending')