from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create the engine using the DATABASE_URL from your core/config.py
engine = create_engine(settings.DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the "get_db" function your API was looking for
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()