from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.building_repository import BuildingRepository
from app.dtos.building_dto import BuildingCreateDTO, BuildingUpdateDTO

class BuildingService:
    def __init__(self, db: Session):
        self.repository = BuildingRepository(db)

    def create_building(self, dto: BuildingCreateDTO):
        return self.repository.create(dto)

    def get_all_buildings(self):
        return self.repository.get_all()

    def get_building(self, building_id: int):
        building = self.repository.get_by_id(building_id)
        if not building:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
        return building

    def update_building(self, building_id: int, dto: BuildingUpdateDTO):
        building = self.repository.update(building_id, dto)
        if not building:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
        return building

    def delete_building(self, building_id: int):
        if not self.repository.delete(building_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
        return {"detail": "Building deleted successfully"}