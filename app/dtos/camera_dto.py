from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CameraCreateDTO(BaseModel):
    camera_serial: str
    location_name: str
    longitude: float
    latitude: float
    status: str
    building_id: int
    model_id: Optional[int] = None

class CameraUpdateDTO(BaseModel):
    camera_serial: Optional[str] = None
    location_name: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    status: Optional[str] = None
    building_id: Optional[int] = None
    model_id: Optional[int] = None

class CameraResponseDTO(BaseModel):
    # This is now at the top
    camera_id: int
    camera_serial: str
    location_name: str
    longitude: float
    latitude: float
    status: str
    installed_at: datetime
    building_id: int
    model_id: Optional[int] = None

    class Config:
        from_attributes = True