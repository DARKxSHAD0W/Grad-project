from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.building_schema import BuildingCreate, BuildingResponse
from app.services.building_service import BuildingService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/buildings", response_model=BuildingResponse)
def create_building(building_in: BuildingCreate, db: Session = Depends(get_db)):
    service = BuildingService(db)
    return service.add_building(building_in)