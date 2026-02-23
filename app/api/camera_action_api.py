from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.camera_action_service import CameraActionService
from app.dtos.camera_action_dto import CameraActionCreateDTO, CameraActionResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/camera-actions", tags=["7. System Audit Trail"])

@router.get("/", response_model=List[CameraActionResponseDTO])
def list_actions(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all audit logs - Admin Only"""
    return CameraActionService(db).get_all()

@router.get("/{action_id}", response_model=CameraActionResponseDTO)
def get_action(action_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get specific log by ID - Admin Only"""
    return CameraActionService(db).get_by_id(action_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CameraActionResponseDTO)
def log_action(dto: CameraActionCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Create a new log entry - Admin Only"""
    return CameraActionService(db).create(dto)

@router.put("/{action_id}", response_model=CameraActionResponseDTO)
def update_action(action_id: int, dto: CameraActionCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update a log entry - Admin Only"""
    return CameraActionService(db).update(action_id, dto)

@router.delete("/{action_id}")
def delete_action(action_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete a log entry - Admin Only"""
    return CameraActionService(db).delete(action_id)