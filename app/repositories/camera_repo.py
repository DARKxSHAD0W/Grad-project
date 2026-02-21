from sqlalchemy.orm import Session
from app.db.models import Camera

class CameraRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        """Fetch all cameras from the database"""
        return self.db.query(Camera).all()

    def get_by_id(self, camera_id: int):
        """Fetch one specific camera"""
        return self.db.query(Camera).filter(Camera.camera_id == camera_id).first()

    def create(self, camera_data: dict):
        """Save a new camera to the database"""
        db_camera = Camera(**camera_data)
        self.db.add(db_camera)
        self.db.commit()
        self.db.refresh(db_camera)
        return db_camera