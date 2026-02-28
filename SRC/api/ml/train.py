"""
Model training script.
"""
import pickle
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.api.core.logging import get_logger

logger = get_logger(__name__)


class ModelTrainer:
    """Train machine learning models."""

    def __init__(self, model_path: str = "models/"):
        self.model_path = Path(model_path)
        self.model_path.mkdir(exist_ok=True)

    def train_risk_model(self, X_train, y_train):
        """Train the risk prediction model."""
        logger.info("Starting risk model training")
        
        try:
            # Initialize and train model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Save model
            model_file = self.model_path / "risk_model.pkl"
            with open(model_file, "wb") as f:
                pickle.dump(model, f)
            
            logger.info(f"Risk model trained and saved to {model_file}")
            return model
        except Exception as e:
            logger.error(f"Error training risk model: {str(e)}")
            raise

    def train_trend_model(self, X_train, y_train):
        """Train the trend prediction model."""
        logger.info("Starting trend model training")
        
        try:
            # Initialize and train model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Save model
            model_file = self.model_path / "trend_model.pkl"
            with open(model_file, "wb") as f:
                pickle.dump(model, f)
            
            logger.info(f"Trend model trained and saved to {model_file}")
            return model
        except Exception as e:
            logger.error(f"Error training trend model: {str(e)}")
            raise

    def evaluate_model(self, model, X_test, y_test):
        """Evaluate model performance."""
        score = model.score(X_test, y_test)
        logger.info(f"Model accuracy: {score:.4f}")
        return score
