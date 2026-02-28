"""
Accident repository for data access operations.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from src.api.core.logging import get_logger
from src.api.models.accident import Accident
from src.api.schemas.accident_schema import AccidentCreate, AccidentUpdate

logger = get_logger(__name__)


class AccidentRepository:
    """Repository for accident data access operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, accident_data: AccidentCreate, user_id: Optional[int] = None) -> Accident:
        """Create a new accident in the database."""
        db_accident = Accident(**accident_data.dict(), user_id=user_id)
        self.db.add(db_accident)
        self.db.commit()
        self.db.refresh(db_accident)
        return db_accident

    def get_by_id(self, accident_id: int) -> Optional[Accident]:
        """Get an accident by ID."""
        return self.db.query(Accident).filter(Accident.id == accident_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get all accidents with pagination."""
        return self.db.query(Accident).offset(skip).limit(limit).all()

    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get accidents by user."""
        return self.db.query(Accident).filter(Accident.user_id == user_id).offset(skip).limit(limit).all()

    def get_by_severity(self, severity: str, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get accidents filtered by severity."""
        return self.db.query(Accident).filter(Accident.severity == severity).offset(skip).limit(limit).all()

    def get_by_status(self, status: str, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get accidents filtered by status."""
        return self.db.query(Accident).filter(Accident.status == status).offset(skip).limit(limit).all()

    def update(self, accident_id: int, accident_data: AccidentUpdate) -> Optional[Accident]:
        """Update an accident."""
        accident = self.get_by_id(accident_id)
        if not accident:
            return None
        
        update_data = accident_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(accident, key, value)
        
        self.db.commit()
        self.db.refresh(accident)
        return accident

    def delete(self, accident_id: int) -> bool:
        """Delete an accident."""
        accident = self.get_by_id(accident_id)
        if not accident:
            return False
        
        self.db.delete(accident)
        self.db.commit()
        return True

    def count(self) -> int:
        """Count total accidents."""
        return self.db.query(Accident).count()

    def count_by_severity(self, severity: str) -> int:
        """Count accidents by severity."""
        return self.db.query(Accident).filter(Accident.severity == severity).count()
