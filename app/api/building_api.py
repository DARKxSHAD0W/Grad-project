from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db # Assuming you have a session helper
from app.dtos.building_dto import BuildingCreateDTO, BuildingUpdateDTO, BuildingResponseDTO
from app.services.building_service import BuildingService

router = APIRouter()

# CREATE
@router.post("/", response_model=BuildingResponseDTO, status_code=status.HTTP_201_CREATED)
def create_building(dto: BuildingCreateDTO, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.create_building(dto)

# READ ALL
@router.get("/", response_model=List[BuildingResponseDTO])
def get_all_buildings(db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.get_all_buildings()

# READ ONE
@router.get("/{building_id}", response_model=BuildingResponseDTO)
def get_building(building_id: int, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.get_building(building_id)

# UPDATE
@router.put("/{building_id}", response_model=BuildingResponseDTO)
def update_building(building_id: int, dto: BuildingUpdateDTO, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.update_building(building_id, dto)

# DELETE
@router.delete("/{building_id}")
def delete_building(building_id: int, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.delete_building(building_id)