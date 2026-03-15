from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    destination = Column(String, index=True)
    style = Column(String)
    days = Column(Integer)
    content = Column(JSON)  # Stores the actual generated itinerary structure
    created_at = Column(DateTime(timezone=True), server_default=func.now())
