from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.camera_service import CameraService
from app.dtos.camera_dto import CameraCreateDTO, CameraUpdateDTO, CameraResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/cameras", tags=["3. Camera Management"])

@router.get("/", response_model=List[CameraResponseDTO])
def list_cameras(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all cameras - Admin Only"""
    return CameraService(db).get_all_cameras()

@router.get("/{camera_id}", response_model=CameraResponseDTO)
def get_camera(camera_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get camera by ID - Admin Only"""
    return CameraService(db).get_camera(camera_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CameraResponseDTO)
def add_camera(dto: CameraCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Add new camera - Admin Only"""
    return CameraService(db).create_camera(dto)

@router.put("/{camera_id}", response_model=CameraResponseDTO)
def update_camera(camera_id: int, dto: CameraUpdateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update camera - Admin Only"""
    return CameraService(db).update_camera(camera_id, dto)

@router.delete("/{camera_id}")
def delete_camera(camera_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete camera - Admin Only"""
    return CameraService(db).delete_camera(camera_id)