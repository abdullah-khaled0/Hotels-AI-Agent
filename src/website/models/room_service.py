from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class RoomService(Base):
    __tablename__ = 'room_services'
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='CASCADE'), primary_key=True)
    service_id = Column(Integer, ForeignKey('services.service_id', ondelete='CASCADE'), primary_key=True)