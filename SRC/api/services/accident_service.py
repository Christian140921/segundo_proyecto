"""
Accident business logic service.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from src.api.core.logging import get_logger
from src.api.models.accident import Accident
from src.api.schemas.accident_schema import AccidentCreate, AccidentUpdate
from src.api.services.prediction_service import PredictionService

logger = get_logger(__name__)


class AccidentService:
    """Service for accident-related business logic."""

    @staticmethod
    def create_accident(db: Session, accident_data: AccidentCreate, user_id: Optional[int] = None) -> Accident:
        """Create a new accident."""
        logger.info(f"Creating accident at location: {accident_data.location}")
        
        # Calculate risk score using ML prediction
        risk_score = PredictionService.predict_risk(
            location=accident_data.location,
            severity=accident_data.severity
        )
        
        db_accident = Accident(
            user_id=user_id,
            location=accident_data.location,
            latitude=accident_data.latitude,
            longitude=accident_data.longitude,
            severity=accident_data.severity,
            description=accident_data.description,
            risk_score=risk_score,
        )
        db.add(db_accident)
        db.commit()
        db.refresh(db_accident)
        
        logger.info(f"Accident created successfully: {db_accident.id} (Risk Score: {risk_score})")
        return db_accident

    @staticmethod
    def get_accident_by_id(db: Session, accident_id: int) -> Optional[Accident]:
        """Get an accident by ID."""
        return db.query(Accident).filter(Accident.id == accident_id).first()

    @staticmethod
    def get_all_accidents(db: Session, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get all accidents with pagination."""
        return db.query(Accident).offset(skip).limit(limit).all()

    @staticmethod
    def get_accidents_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get accidents by user."""
        return db.query(Accident).filter(Accident.user_id == user_id).offset(skip).limit(limit).all()

    @staticmethod
    def get_accidents_by_severity(db: Session, severity: str, skip: int = 0, limit: int = 100) -> List[Accident]:
        """Get accidents filtered by severity."""
        return db.query(Accident).filter(Accident.severity == severity).offset(skip).limit(limit).all()

    @staticmethod
    def update_accident(db: Session, accident_id: int, accident_data: AccidentUpdate) -> Optional[Accident]:
        """Update an accident."""
        logger.info(f"Updating accident: {accident_id}")
        
        accident = db.query(Accident).filter(Accident.id == accident_id).first()
        if not accident:
            logger.warning(f"Accident not found: {accident_id}")
            return None
        
        update_data = accident_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(accident, key, value)
        
        db.commit()
        db.refresh(accident)
        
        logger.info(f"Accident updated successfully: {accident_id}")
        return accident

    @staticmethod
    def delete_accident(db: Session, accident_id: int) -> bool:
        """Delete an accident."""
        logger.info(f"Deleting accident: {accident_id}")
        
        accident = db.query(Accident).filter(Accident.id == accident_id).first()
        if not accident:
            logger.warning(f"Accident not found: {accident_id}")
            return False
        
        db.delete(accident)
        db.commit()
        
        logger.info(f"Accident deleted successfully: {accident_id}")
        return True
