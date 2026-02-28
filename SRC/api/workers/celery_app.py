"""
Celery application configuration for async tasks.
"""
from celery import Celery

from src.api.core.settings import settings
from src.api.core.logging import get_logger

logger = get_logger(__name__)

# Initialize Celery app
celery_app = Celery(
    "nodalcms",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

# Configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    worker_prefetch_multiplier=1,
    broker_connection_retry_on_startup=True,
)

logger.info("Celery app initialized")
