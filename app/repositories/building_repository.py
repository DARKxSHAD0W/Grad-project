from sqlalchemy.orm import Session
from app.db.models import Building
from app.dtos.building_dto import BuildingCreateDTO, BuildingUpdateDTO

class BuildingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: BuildingCreateDTO) -> Building:
        new_building = Building(
            building_name=dto.building_name,
            phone_number=dto.phone_number,
            status=dto.status
        )
        self.db.add(new_building)
        self.db.commit()
        self.db.refresh(new_building)
        return new_building

    def get_all(self):
        return self.db.query(Building).all()

    def get_by_id(self, building_id: int):
        return self.db.query(Building).filter(Building.building_id == building_id).first()

    def update(self, building_id: int, dto: BuildingUpdateDTO):
        db_building = self.get_by_id(building_id)
        if db_building:
            update_data = dto.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_building, key, value)
            self.db.commit()
            self.db.refresh(db_building)
        return db_building

    def delete(self, building_id: int):
        db_building = self.get_by_id(building_id)
        if db_building:
            self.db.delete(db_building)
            self.db.commit()
            return True
        return False