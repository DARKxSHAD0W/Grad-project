from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.camera_repository import CameraRepository
from app.dtos.camera_dto import CameraCreateDTO, CameraUpdateDTO

class CameraService:
    def __init__(self, db: Session):
        self.repository = CameraRepository(db)

    def create_camera(self, dto: CameraCreateDTO):
        return self.repository.create(dto)

    def get_all_cameras(self):
        return self.repository.get_all()

    def get_camera(self, camera_id: int):
        camera = self.repository.get_by_id(camera_id)
        if not camera:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found")
        return camera

    def update_camera(self, camera_id: int, dto: CameraUpdateDTO):
        camera = self.repository.update(camera_id, dto)
        if not camera:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found")
        return camera

    def delete_camera(self, camera_id: int):
        if not self.repository.delete(camera_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found")
        return {"detail": "Camera deleted successfully"}