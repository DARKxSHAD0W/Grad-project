from sqlalchemy.orm import Session
from app.db.models import ModelDeployment
from app.dtos.deployment_dto import DeploymentCreateDTO, DeploymentUpdateDTO

class DeploymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: DeploymentCreateDTO) -> ModelDeployment:
        new_deployment = ModelDeployment(
            camera_id=dto.camera_id,
            model_id=dto.model_id,
            deployment_status=dto.deployment_status,
            deployed_by=dto.deployed_by
        )
        self.db.add(new_deployment)
        self.db.commit()
        self.db.refresh(new_deployment)
        return new_deployment

    def get_all(self):
        return self.db.query(ModelDeployment).all()

    def get_by_id(self, deployment_id: int):
        return self.db.query(ModelDeployment).filter(ModelDeployment.deployment_id == deployment_id).first()

    def update_status(self, deployment_id: int, dto: DeploymentUpdateDTO):
        db_dep = self.get_by_id(deployment_id)
        if db_dep:
            db_dep.deployment_status = dto.deployment_status
            self.db.commit()
            self.db.refresh(db_dep)
        return db_dep

    def delete(self, deployment_id: int):
        db_dep = self.get_by_id(deployment_id)
        if db_dep:
            self.db.delete(db_dep)
            self.db.commit()
            return True
        return False