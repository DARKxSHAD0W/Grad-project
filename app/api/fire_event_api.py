from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.fire_event_service import FireEventService
from app.dtos.fire_event_dto import FireEventCreateDTO, FireEventUpdateDTO, FireEventResponseDTO
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/api/fire-events", tags=["6. Fire Events"])

@router.get("/", response_model=List[FireEventResponseDTO])
def list_fire_events(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """List all fire events - Accessible by any logged-in user"""
    return FireEventService(db).get_all()

@router.get("/{event_id}", response_model=FireEventResponseDTO)
def get_fire_event(event_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Get specific fire event - Accessible by any logged-in user"""
    return FireEventService(db).get_by_id(event_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FireEventResponseDTO)
def report_fire_event(dto: FireEventCreateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Report a new fire event - Accessible by any logged-in user (including Employees)"""
    return FireEventService(db).create(dto)

@router.put("/{event_id}", response_model=FireEventResponseDTO)
def update_fire_event(event_id: int, dto: FireEventUpdateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Update fire event details - Accessible by any logged-in user (including Employees)"""
    return FireEventService(db).update(event_id, dto)

@router.delete("/{event_id}")
def delete_fire_event(event_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Delete fire event record - Accessible by any logged-in user (including Employees)"""
    return FireEventService(db).delete(event_id)