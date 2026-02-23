import logging
from app.db.session import engine, Base
# Import the models module to ensure all classes are registered
from app.db import models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db():
    try:
        logger.info("Connecting to Database...")

        # This explicitly tells Python to load these specific classes
        # This fixes the issue where they 'disappeared' after refactoring
        required_models = [models.Employee, models.FireEvent, models.Building, models.Camera]

        # Diagnostic: Show exactly what SQLAlchemy is about to build
        tables = list(Base.metadata.tables.keys())
        logger.info(f"Registered tables: {tables}")

        if "employee" not in tables or "fire_event" not in tables:
            logger.error("CRITICAL: Employee or FireEvent missing from metadata!")

        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise e