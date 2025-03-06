from sqlalchemy import Column, Integer, String, Numeric, Text
from sqlalchemy.orm import relationship
from src.website.models.database import Base

class Service(Base):
    __tablename__ = 'services'
    service_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)