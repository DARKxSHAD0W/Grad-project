from sqlalchemy.orm import Session
from app.db.models import CameraAction
from app.dtos.camera_action_dto import CameraActionCreateDTO

class CameraActionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(CameraAction).all()

    def get_by_id(self, action_id: int):
        return self.db.query(CameraAction).filter(CameraAction.action_id == action_id).first()

    def create(self, dto: CameraActionCreateDTO):
        new_action = CameraAction(**dto.dict())
        self.db.add(new_action)
        self.db.commit()
        self.db.refresh(new_action)
        return new_action

    def update(self, action_id: int, dto: CameraActionCreateDTO):
        action = self.get_by_id(action_id)
        if action:
            for key, value in dto.dict().items():
                setattr(action, key, value)
            self.db.commit()
            self.db.refresh(action)
        return action

    def delete(self, action_id: int):
        action = self.get_by_id(action_id)
        if action:
            self.db.delete(action)
            self.db.commit()
            return True
        return False