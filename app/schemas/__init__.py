from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

# This is the DTO for Creating a camera (What the user sends)
class CameraCreate(BaseModel):
    camera_serial: str # [cite: 34]
    location_name: str # [cite: 36]
    latitude: Optional[Decimal] = None # [cite: 39, 40]
    longitude: Optional[Decimal] = None # [cite: 50]
    building_id: Optional[int] = None # [cite: 61]
    model_id: Optional[int] = None # [cite: 63]

# This is the DTO for Sending data back (What the user sees)
class CameraResponse(BaseModel):
    camera_id: int # [cite: 17]
    camera_serial: str # [cite: 34]
    status: str # [cite: 55]

    class Config:
        from_attributes = True # This allows it to work with SQLAlchemy