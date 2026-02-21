from pydantic import BaseModel, ConfigDict, field_serializer
from typing import Optional
from datetime import datetime

class BuildingCreateDTO(BaseModel):
    """Data sent by the user to create a building."""
    building_name: str
    phone_number: Optional[str] = None
    status: bool = True

class BuildingUpdateDTO(BaseModel):
    """Data sent by the user to update an existing building."""
    building_name: Optional[str] = None
    phone_number: Optional[str] = None
    status: Optional[bool] = None

class BuildingResponseDTO(BaseModel):
    """Data returned to the user (The Presenter)."""
    building_id: int
    building_name: str
    phone_number: Optional[str]
    status: bool
    # Represented in UTC as per industry standard
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    # Formats the UTC time into a readable string for the API response
    @field_serializer('created_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')