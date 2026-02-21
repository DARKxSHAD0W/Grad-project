from app.repositories.camera_repo import CameraRepository
from app.schemas.camera_schema import CameraCreate


class CameraService:
    def __init__(self, db):
        self.repository = CameraRepository(db)

    def add_new_camera(self, camera_data: CameraCreate):
        # Professional Step: Convert the DTO object into a Dictionary
        # SQLAlchemy cannot save a Pydantic object directly
        camera_dict = camera_data.model_dump()

        # Add any default logic (e.g., status is Active by default)
        if "status" not in camera_dict or camera_dict["status"] is None:
            camera_dict["status"] = "Active"

        return self.repository.create(camera_dict)