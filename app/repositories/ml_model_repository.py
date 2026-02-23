from sqlalchemy.orm import Session
from app.db.models import MLModel
from app.dtos.ml_model_dto import MLModelCreateDTO, MLModelUpdateDTO

class MLModelRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: MLModelCreateDTO) -> MLModel:
        new_model = MLModel(
            version=dto.version,
            file_path=dto.file_path,
            status=dto.status,
            employee_id=dto.employee_id
        )
        self.db.add(new_model)
        self.db.commit()
        self.db.refresh(new_model)
        return new_model

    def get_all(self):
        return self.db.query(MLModel).all()

    def get_by_id(self, model_id: int):
        return self.db.query(MLModel).filter(MLModel.model_id == model_id).first()

    def update(self, model_id: int, dto: MLModelUpdateDTO):
        db_model = self.get_by_id(model_id)
        if db_model:
            update_data = dto.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_model, key, value)
            self.db.commit()
            self.db.refresh(db_model)
        return db_model

    def delete(self, model_id: int):
        db_model = self.get_by_id(model_id)
        if db_model:
            self.db.delete(db_model)
            self.db.commit()
            return True
        return False