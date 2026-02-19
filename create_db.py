from app.db.session import engine
from app.db.models import Base

def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done! Check pgAdmin4.")

if __name__ == "__main__":
    create_tables()