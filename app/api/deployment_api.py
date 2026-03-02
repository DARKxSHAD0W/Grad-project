from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.deployment_service import DeploymentService
from app.dtos.deployment_dto import DeploymentCreateDTO, DeploymentUpdateDTO, DeploymentResponseDTO
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/api/deployments", tags=["5. Model Deployments"])

@router.get("/", response_model=List[DeploymentResponseDTO])
def list_deployments(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """List all deployments - Accessible by any logged-in user"""
    return DeploymentService(db).get_all_deployments()

@router.get("/{deployment_id}", response_model=DeploymentResponseDTO)
def get_deployment(deployment_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Get deployment by ID - Accessible by any logged-in user"""
    return DeploymentService(db).get_deployment(deployment_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DeploymentResponseDTO)
def create_deployment(dto: DeploymentCreateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Create a new deployment - Accessible by any logged-in user (including Employees)"""
    return DeploymentService(db).create_deployment(dto)

@router.put("/{deployment_id}", response_model=DeploymentResponseDTO)
def update_deployment(deployment_id: int, dto: DeploymentUpdateDTO, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Update deployment - Accessible by any logged-in user (including Employees)"""
    return DeploymentService(db).update_deployment(deployment_id, dto)

@router.delete("/{deployment_id}")
def delete_deployment(deployment_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    """Delete deployment - Accessible by any logged-in user (including Employees)"""
    return DeploymentService(db).delete_deployment(deployment_id)