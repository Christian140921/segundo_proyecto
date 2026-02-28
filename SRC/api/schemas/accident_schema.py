"""
Pydantic schemas for Accident models.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AccidentBase(BaseModel):
    """Base Accident schema."""
    
    location: str = Field(..., min_length=1)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    severity: str = Field(..., pattern="^(low|medium|high|critical)$")
    description: Optional[str] = None


class AccidentCreate(AccidentBase):
    """Schema for creating an accident."""
    
    pass


class AccidentUpdate(BaseModel):
    """Schema for updating an accident."""
    
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    severity: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    risk_score: Optional[float] = None


class AccidentResponse(AccidentBase):
    """Schema for accident response."""
    
    id: int
    user_id: Optional[int] = None
    status: str
    risk_score: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
