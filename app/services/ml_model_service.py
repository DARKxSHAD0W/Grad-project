from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.ml_model_repository import MLModelRepository
from app.dtos.ml_model_dto import MLModelCreateDTO, MLModelUpdateDTO

class MLModelService:
    def __init__(self, db: Session):
        self.repository = MLModelRepository(db)

    def create_model(self, dto: MLModelCreateDTO):
        # Business Logic: You could add a check here to ensure the file_path is valid
        return self.repository.create(dto)

    def get_all_models(self):
        return self.repository.get_all()

    def get_model(self, model_id: int):
        model = self.repository.get_by_id(model_id)
        if not model:
            raise HTTPException(status_code=404, detail="ML Model not found")
        return model

    def update_model(self, model_id: int, dto: MLModelUpdateDTO):
        model = self.repository.update(model_id, dto)
        if not model:
            raise HTTPException(status_code=404, detail="ML Model not found")
        return model

    def delete_model(self, model_id: int):
        if not self.repository.delete(model_id):
            raise HTTPException(status_code=404, detail="ML Model not found")
        return {"detail": "ML Model deleted successfully"}