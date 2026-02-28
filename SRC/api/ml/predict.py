"""
Prediction module for making inferences with trained models.
"""
from typing import List, Any, Optional

from src.api.core.logging import get_logger
from src.api.ml.model_loader import ModelLoader
from src.api.ml.features import FeatureExtractor

logger = get_logger(__name__)


class Predictor:
    """Make predictions using trained models."""

    def __init__(self):
        self.risk_model = ModelLoader.load_risk_model()
        self.trend_model = ModelLoader.load_trend_model()

    def predict_risk(self, features: List[float]) -> Optional[float]:
        """Predict risk score."""
        try:
            if self.risk_model is None:
                logger.warning("Risk model not available")
                return None
            
            prediction = self.risk_model.predict([features])[0]
            return float(prediction)
        except Exception as e:
            logger.error(f"Error during risk prediction: {str(e)}")
            return None

    def predict_risk_proba(self, features: List[float]) -> Optional[List[float]]:
        """Predict risk probabilities."""
        try:
            if self.risk_model is None or not hasattr(self.risk_model, 'predict_proba'):
                logger.warning("Risk model not available or doesn't support probability")
                return None
            
            probabilities = self.risk_model.predict_proba([features])[0]
            return list(probabilities)
        except Exception as e:
            logger.error(f"Error during risk probability prediction: {str(e)}")
            return None

    def predict_trend(self, features: List[float]) -> Optional[float]:
        """Predict trend."""
        try:
            if self.trend_model is None:
                logger.warning("Trend model not available")
                return None
            
            prediction = self.trend_model.predict([features])[0]
            return float(prediction)
        except Exception as e:
            logger.error(f"Error during trend prediction: {str(e)}")
            return None

    def batch_predict(self, features_list: List[List[float]]) -> Optional[List[float]]:
        """Make batch predictions."""
        try:
            if self.risk_model is None:
                logger.warning("Risk model not available")
                return None
            
            predictions = self.risk_model.predict(features_list)
            return list(predictions)
        except Exception as e:
            logger.error(f"Error during batch prediction: {str(e)}")
            return None
