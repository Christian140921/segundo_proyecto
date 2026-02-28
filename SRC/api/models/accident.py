"""
Accident model for database.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin, IDMixin


class Accident(Base, IDMixin, TimestampMixin):
    """Accident/Incident model."""
    
    __tablename__ = "accidents"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    location = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    severity = Column(String(50), nullable=False)  # low, medium, high, critical
    description = Column(Text, nullable=True)
    status = Column(String(50), default="open")  # open, closed, investigating
    risk_score = Column(Float, nullable=True)

    def __repr__(self) -> str:
        return f"<Accident(id={self.id}, location={self.location}, severity={self.severity})>"
