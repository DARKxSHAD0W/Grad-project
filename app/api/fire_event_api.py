from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.fire_event_service import FireEventService
from app.dtos.fire_event_dto import FireEventCreateDTO, FireEventResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/fire-events", tags=["6. Fire Detection Logs"])

@router.get("/", response_model=List[FireEventResponseDTO])
def list_fire_events(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all fire events - Admin Only"""
    return FireEventService(db).get_all_events()

@router.get("/{fire_event_id}", response_model=FireEventResponseDTO)
def get_fire_event(fire_event_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get fire event by ID - Admin Only"""
    return FireEventService(db).get_event_by_id(fire_event_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FireEventResponseDTO)
def log_fire(dto: FireEventCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Log a new fire detection - Admin Only"""
    return FireEventService(db).log_detection(dto)

@router.put("/{fire_event_id}", response_model=FireEventResponseDTO)
def update_fire_event(fire_event_id: int, dto: FireEventCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update fire event logs - Admin Only"""
    return FireEventService(db).update_event(fire_event_id, dto)

@router.delete("/{fire_event_id}")
def delete_fire_event(fire_event_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete fire event log - Admin Only"""
    return FireEventService(db).delete_event(fire_event_id)