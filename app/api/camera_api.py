from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.dtos.camera_dto import CameraCreateDTO, CameraResponseDTO, CameraUpdateDTO
from app.services.camera_service import CameraService

router = APIRouter()

@router.post("/", response_model=CameraResponseDTO, status_code=status.HTTP_201_CREATED)
def create_camera(dto: CameraCreateDTO, db: Session = Depends(get_db)):
    service = CameraService(db)
    return service.create_camera(dto)

@router.get("/", response_model=List[CameraResponseDTO])
def list_cameras(db: Session = Depends(get_db)):
    service = CameraService(db)
    return service.get_all_cameras()

@router.get("/{camera_id}", response_model=CameraResponseDTO)
def get_camera(camera_id: int, db: Session = Depends(get_db)):
    service = CameraService(db)
    return service.get_camera(camera_id)

@router.put("/{camera_id}", response_model=CameraResponseDTO)
def update_camera(camera_id: int, dto: CameraUpdateDTO, db: Session = Depends(get_db)):
    service = CameraService(db)
    return service.update_camera(camera_id, dto)

@router.delete("/{camera_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_camera(camera_id: int, db: Session = Depends(get_db)):
    service = CameraService(db)
    return service.delete_camera(camera_id)