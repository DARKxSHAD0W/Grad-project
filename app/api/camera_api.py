from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.camera_schema import CameraCreate, CameraResponse
from app.services.camera_service import CameraService

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cameras", response_model=CameraResponse)
def create_camera(camera_in: CameraCreate, db: Session = Depends(get_db)):
    """
    Presenter Layer:
    Receives CameraCreate DTO -> Passes to Service -> Returns CameraResponse DTO
    """
    service = CameraService(db)
    return service.add_new_camera(camera_in)