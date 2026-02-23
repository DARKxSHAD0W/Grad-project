from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.building_service import BuildingService
from app.dtos.building_dto import BuildingCreateDTO, BuildingUpdateDTO, BuildingResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/buildings", tags=["1. Building Management"])

@router.get("/", response_model=List[BuildingResponseDTO])
def list_buildings(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return BuildingService(db).get_all_buildings()

@router.get("/{building_id}", response_model=BuildingResponseDTO)
def get_building(building_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return BuildingService(db).get_building(building_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BuildingResponseDTO)
def create_building(dto: BuildingCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return BuildingService(db).create_building(dto)

@router.put("/{building_id}", response_model=BuildingResponseDTO)
def update_building(building_id: int, dto: BuildingUpdateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return BuildingService(db).update_building(building_id, dto)

@router.delete("/{building_id}")
def delete_building(building_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return BuildingService(db).delete_building(building_id)