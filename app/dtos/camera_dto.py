from pydantic import BaseModel, ConfigDict, field_serializer
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CameraCreateDTO(BaseModel):
    camera_serial: str
    location_name: str
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    status: Optional[str] = "Active"
    building_id: int  # Required to link to a building
    model_id: Optional[int] = None # Optional link to an ML model

class CameraUpdateDTO(BaseModel):
    location_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    status: Optional[str] = None
    model_id: Optional[int] = None

class CameraResponseDTO(BaseModel):
    camera_id: int
    camera_serial: str
    location_name: str
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    status: str
    installed_at: datetime
    building_id: int
    model_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('installed_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')