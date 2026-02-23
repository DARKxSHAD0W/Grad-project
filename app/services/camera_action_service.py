from fastapi import HTTPException, status
from app.repositories.camera_action_repository import CameraActionRepository

class CameraActionService:
    def __init__(self, db):
        self.repository = CameraActionRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, action_id: int):
        action = self.repository.get_by_id(action_id)
        if not action:
            raise HTTPException(status_code=404, detail="Camera Action not found")
        return action

    def create(self, dto):
        return self.repository.create(dto)

    def update(self, action_id: int, dto):
        action = self.repository.update(action_id, dto)
        if not action:
            raise HTTPException(status_code=404, detail="Camera Action not found")
        return action

    def delete(self, action_id: int):
        if not self.repository.delete(action_id):
            raise HTTPException(status_code=404, detail="Camera Action not found")
        return {"detail": "Action log deleted successfully"}