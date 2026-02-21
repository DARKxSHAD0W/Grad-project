from sqlalchemy.orm import Session
from app.db.models import Building

class BuildingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, building_data: dict):
        """
        Saves a building to the database based on the schema [cite: 66-70].
        """
        db_building = Building(**building_data)
        self.db.add(db_building)
        self.db.commit()
        self.db.refresh(db_building)
        return db_building