"""
Feature extraction and engineering for ML models.
"""
from typing import List, Dict, Any

from src.api.core.logging import get_logger

logger = get_logger(__name__)


class FeatureExtractor:
    """Extract and engineer features for ML models."""

    # Feature mappings
    SEVERITY_MAP = {
        "low": 1,
        "medium": 2,
        "high": 3,
        "critical": 4,
    }

    LOCATION_RISK_MAP = {
        "highway": 3,
        "urban": 2,
        "rural": 1,
        "residential": 2,
    }

    @classmethod
    def extract_risk_features(cls, location: str, severity: str) -> List[float]:
        """Extract features for risk prediction."""
        try:
            features = []
            
            # Severity feature
            severity_value = cls.SEVERITY_MAP.get(severity.lower(), 2)
            features.append(float(severity_value))
            
            # Location risk feature
            location_risk = cls.LOCATION_RISK_MAP.get(location.lower(), 2)
            features.append(float(location_risk))
            
            # Time-based features (hour of day, day of week, etc.)
            # These should be added based on actual requirements
            
            logger.debug(f"Extracted risk features: {features}")
            return features
        except Exception as e:
            logger.error(f"Error extracting risk features: {str(e)}")
            return [2.0, 2.0]  # Default features

    @classmethod
    def extract_trend_features(cls, data: Dict[str, Any]) -> List[float]:
        """Extract features for trend prediction."""
        try:
            features = []
            
            # Example features - adjust based on actual requirements
            if "count" in data:
                features.append(float(data["count"]))
            if "average_severity" in data:
                features.append(float(data["average_severity"]))
            if "growth_rate" in data:
                features.append(float(data["growth_rate"]))
            
            logger.debug(f"Extracted trend features: {features}")
            return features
        except Exception as e:
            logger.error(f"Error extracting trend features: {str(e)}")
            return []

    @classmethod
    def normalize_features(cls, features: List[float], mean: float = 0, std: float = 1) -> List[float]:
        """Normalize features to zero mean and unit variance."""
        return [(f - mean) / (std + 1e-8) for f in features]
