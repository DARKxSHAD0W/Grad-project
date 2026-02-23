from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.deployment_service import DeploymentService
from app.dtos.deployment_dto import DeploymentCreateDTO, DeploymentUpdateDTO, DeploymentResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/deployments", tags=["5. Model Deployments"])

@router.get("/", response_model=List[DeploymentResponseDTO])
def list_deployments(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all deployments - Admin Only"""
    return DeploymentService(db).get_all_deployments()

@router.get("/{deployment_id}", response_model=DeploymentResponseDTO)
def get_deployment(deployment_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get deployment by ID - Admin Only"""
    return DeploymentService(db).get_deployment(deployment_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DeploymentResponseDTO)
def create_deployment(dto: DeploymentCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Create a new deployment - Admin Only"""
    return DeploymentService(db).create_deployment(dto)

@router.put("/{deployment_id}", response_model=DeploymentResponseDTO)
def update_deployment(deployment_id: int, dto: DeploymentUpdateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update deployment - Admin Only"""
    return DeploymentService(db).update_deployment(deployment_id, dto)

@router.delete("/{deployment_id}")
def delete_deployment(deployment_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete deployment - Admin Only"""
    return DeploymentService(db).delete_deployment(deployment_id)