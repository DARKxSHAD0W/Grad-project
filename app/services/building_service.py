from sqlalchemy.orm import Session
from app.repositories.building_repo import BuildingRepository
from app.schemas.building_schema import BuildingCreate

class BuildingService:
    def __init__(self, db: Session):
        self.repo = BuildingRepository(db)

    def add_building(self, data: BuildingCreate):
        # Convert DTO to dictionary for the Repository
        building_dict = data.model_dump()
        return self.repo.create(building_dict)