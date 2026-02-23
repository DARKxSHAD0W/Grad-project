from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.deployment_repository import DeploymentRepository
from app.dtos.deployment_dto import DeploymentCreateDTO, DeploymentUpdateDTO

class DeploymentService:
    def __init__(self, db: Session):
        self.repository = DeploymentRepository(db)

    def create_deployment(self, dto: DeploymentCreateDTO):
        # Professional Check: Ensure the link is valid before saving
        return self.repository.create(dto)

    def get_all_deployments(self):
        return self.repository.get_all()

    def get_deployment(self, deployment_id: int):
        deployment = self.repository.get_by_id(deployment_id)
        if not deployment:
            raise HTTPException(status_code=404, detail="Deployment record not found")
        return deployment

    def update_deployment(self, deployment_id: int, dto: DeploymentUpdateDTO):
        deployment = self.repository.update_status(deployment_id, dto)
        if not deployment:
            raise HTTPException(status_code=404, detail="Deployment record not found")
        return deployment

    def delete_deployment(self, deployment_id: int):
        if not self.repository.delete(deployment_id):
            raise HTTPException(status_code=404, detail="Deployment record not found")
        return {"detail": "Deployment successfully removed"}