"""
Model loader for loading trained ML models.
"""
import pickle
from pathlib import Path
from typing import Optional, Any

from src.api.core.logging import get_logger
from src.api.core.settings import settings

logger = get_logger(__name__)


class ModelLoader:
    """Load and cache machine learning models."""
    
    _risk_model = None
    _trend_model = None
    _scaler = None

    @classmethod
    def load_risk_model(cls) -> Optional[Any]:
        """Load or return cached risk model."""
        if cls._risk_model is not None:
            return cls._risk_model
        
        try:
            model_path = Path(settings.MODEL_PATH) / "risk_model.pkl"
            if not model_path.exists():
                logger.warning(f"Risk model not found at {model_path}")
                return None
            
            with open(model_path, "rb") as f:
                cls._risk_model = pickle.load(f)
            
            logger.info("Risk model loaded successfully")
            return cls._risk_model
        except Exception as e:
            logger.error(f"Error loading risk model: {str(e)}")
            return None

    @classmethod
    def load_trend_model(cls) -> Optional[Any]:
        """Load or return cached trend model."""
        if cls._trend_model is not None:
            return cls._trend_model
        
        try:
            model_path = Path(settings.MODEL_PATH) / "trend_model.pkl"
            if not model_path.exists():
                logger.warning(f"Trend model not found at {model_path}")
                return None
            
            with open(model_path, "rb") as f:
                cls._trend_model = pickle.load(f)
            
            logger.info("Trend model loaded successfully")
            return cls._trend_model
        except Exception as e:
            logger.error(f"Error loading trend model: {str(e)}")
            return None

    @classmethod
    def load_scaler(cls) -> Optional[Any]:
        """Load or return cached feature scaler."""
        if cls._scaler is not None:
            return cls._scaler
        
        try:
            scaler_path = Path(settings.MODEL_PATH) / "scaler.pkl"
            if not scaler_path.exists():
                logger.warning(f"Scaler not found at {scaler_path}")
                return None
            
            with open(scaler_path, "rb") as f:
                cls._scaler = pickle.load(f)
            
            logger.info("Scaler loaded successfully")
            return cls._scaler
        except Exception as e:
            logger.error(f"Error loading scaler: {str(e)}")
            return None

    @classmethod
    def clear_cache(cls):
        """Clear cached models."""
        cls._risk_model = None
        cls._trend_model = None
        cls._scaler = None
        logger.info("Model cache cleared")
