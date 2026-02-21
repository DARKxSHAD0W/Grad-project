from pydantic import BaseModel, ConfigDict, field_serializer
from typing import Optional
from datetime import datetime

class BuildingCreate(BaseModel):
    building_name: str
    phone_number: Optional[str] = None
    status: bool = True

class BuildingResponse(BaseModel):
    building_id: int
    building_name: str
    phone_number: Optional[str]
    status: bool
    created_at: datetime

    # This replaces 'class Config' to fix your Pydantic warning
    model_config = ConfigDict(from_attributes=True)

    # This makes the "ugly" database time look nice (2026-02-21 01:00)
    @field_serializer('created_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')