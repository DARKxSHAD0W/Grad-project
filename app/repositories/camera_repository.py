from sqlalchemy.orm import Session
from app.db.models import Camera
from app.dtos.camera_dto import CameraCreateDTO, CameraUpdateDTO

class CameraRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: CameraCreateDTO) -> Camera:
        new_camera = Camera(
            camera_serial=dto.camera_serial,
            location_name=dto.location_name,
            latitude=dto.latitude,
            longitude=dto.longitude,
            status=dto.status,
            building_id=dto.building_id,
            model_id=dto.model_id
        )
        self.db.add(new_camera)
        self.db.commit()
        self.db.refresh(new_camera)
        return new_camera

    def get_all(self):
        return self.db.query(Camera).all()

    def get_by_id(self, camera_id: int):
        return self.db.query(Camera).filter(Camera.camera_id == camera_id).first()

    def update(self, camera_id: int, dto: CameraUpdateDTO):
        db_camera = self.get_by_id(camera_id)
        if db_camera:
            update_data = dto.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_camera, key, value)
            self.db.commit()
            self.db.refresh(db_camera)
        return db_camera

    def delete(self, camera_id: int):
        db_camera = self.get_by_id(camera_id)
        if db_camera:
            self.db.delete(db_camera)
            self.db.commit()
            return True
        return False