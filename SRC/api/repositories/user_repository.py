"""
User repository for data access operations.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from src.api.core.logging import get_logger
from src.api.models.user import User
from src.api.schemas.user_schema import UserCreate, UserUpdate

logger = get_logger(__name__)


class UserRepository:
    """Repository for user data access operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreate) -> User:
        """Create a new user in the database."""
        db_user = User(**user_data.dict(exclude={"password"}))
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination."""
        return self.db.query(User).offset(skip).limit(limit).all()

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update a user."""
        user = self.get_by_id(user_id)
        if not user:
            return None
        
        update_data = user_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> bool:
        """Delete a user."""
        user = self.get_by_id(user_id)
        if not user:
            return False
        
        self.db.delete(user)
        self.db.commit()
        return True

    def count(self) -> int:
        """Count total users."""
        return self.db.query(User).count()
