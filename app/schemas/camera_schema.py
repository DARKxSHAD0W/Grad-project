from pydantic import BaseModel, ConfigDict, field_serializer
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CameraCreate(BaseModel):
    camera_serial: str
    location_name: str
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    building_id: Optional[int] = None # Link to Building
    model_id: Optional[int] = None    # Link to ML Model
    status: Optional[str] = "Active"

class CameraResponse(BaseModel):
    camera_id: int
    camera_serial: str
    location_name: str
    status: str
    installed_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('installed_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')