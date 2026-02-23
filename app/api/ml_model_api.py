from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.ml_model_service import MLModelService
from app.dtos.ml_model_dto import MLModelCreateDTO, MLModelUpdateDTO, MLModelResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/models", tags=["4. ML Models"])

@router.get("/", response_model=List[MLModelResponseDTO])
def list_models(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all models - Admin Only"""
    return MLModelService(db).get_all_models()

@router.get("/{model_id}", response_model=MLModelResponseDTO)
def get_model(model_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get model by ID - Admin Only"""
    return MLModelService(db).get_model(model_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MLModelResponseDTO)
def register_model(dto: MLModelCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Register new model - Admin Only"""
    return MLModelService(db).create_model(dto)

@router.put("/{model_id}", response_model=MLModelResponseDTO)
def update_model(model_id: int, dto: MLModelUpdateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update model - Admin Only"""
    return MLModelService(db).update_model(model_id, dto)

@router.delete("/{model_id}")
def remove_model(model_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete model - Admin Only"""
    return MLModelService(db).delete_model(model_id)