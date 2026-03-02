from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.ml_model_service import MLModelService
from app.dtos.ml_model_dto import MLModelCreateDTO, MLModelUpdateDTO, MLModelResponseDTO
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/api/ml-models", tags=["4. ML Model Management"])

@router.get("/", response_model=List[MLModelResponseDTO])
def list_models(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """List all ML models - Accessible by any logged-in user"""
    return MLModelService(db).get_all_models()

@router.get("/{model_id}", response_model=MLModelResponseDTO)
def get_model(model_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Get model by ID - Accessible by any logged-in user"""
    return MLModelService(db).get_model(model_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MLModelResponseDTO)
def register_model(dto: MLModelCreateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Register a new ML model - Accessible by any logged-in user (including Employees)"""
    return MLModelService(db).create_model(dto)

@router.put("/{model_id}", response_model=MLModelResponseDTO)
def update_model(model_id: int, dto: MLModelUpdateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Update model details/version - Accessible by any logged-in user (including Employees)"""
    return MLModelService(db).update_model(model_id, dto)

@router.delete("/{model_id}")
def delete_model(model_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Delete a model - Accessible by any logged-in user (including Employees)"""
    return MLModelService(db).delete_model(model_id)