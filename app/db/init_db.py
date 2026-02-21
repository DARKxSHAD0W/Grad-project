import logging
from app.db.session import engine
from app.db.models import Base

# Set up a basic logger to show status in your terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db():
    try:
        logger.info("Initializing the database tables...")

        # This command creates tables only if they do not exist
        # It uses the metadata from your models.py
        Base.metadata.create_all(bind=engine)

        logger.info("Database tables initialized successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
        raise e


# This allows you to run 'python app/db/init_db.py' directly to reset tables
if __name__ == "__main__":
    init_db()