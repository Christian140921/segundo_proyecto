"""
Prediction service for ML models.
"""
from typing import Optional

from src.api.core.logging import get_logger
from src.api.ml.model_loader import ModelLoader
from src.api.ml.features import FeatureExtractor

logger = get_logger(__name__)


class PredictionService:
    """Service for making predictions using ML models."""

    @staticmethod
    def predict_risk(location: str, severity: str) -> float:
        """Predict risk score for an accident."""
        logger.info(f"Predicting risk for location: {location}, severity: {severity}")
        
        try:
            # Load the model
            model = ModelLoader.load_risk_model()
            if model is None:
                logger.warning("Risk model not loaded, returning default risk score")
                return 0.5
            
            # Extract features
            features = FeatureExtractor.extract_risk_features(location, severity)
            
            # Make prediction
            risk_score = model.predict([features])[0]
            
            logger.info(f"Risk prediction completed: {risk_score}")
            return float(risk_score)
        except Exception as e:
            logger.error(f"Error during risk prediction: {str(e)}")
            return 0.5

    @staticmethod
    def predict_trend(historical_data: list) -> Optional[dict]:
        """Predict future trends based on historical data."""
        logger.info("Predicting trends from historical data")
        
        try:
            model = ModelLoader.load_trend_model()
            if model is None:
                logger.warning("Trend model not loaded")
                return None
            
            # This would depend on the actual implementation
            return {"trend": "up", "confidence": 0.75}
        except Exception as e:
            logger.error(f"Error during trend prediction: {str(e)}")
            return None
