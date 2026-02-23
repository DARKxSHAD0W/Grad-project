from pydantic import BaseModel, ConfigDict, field_serializer
from datetime import datetime, date
from typing import Optional

class CameraActionCreateDTO(BaseModel):
    camera_id: int
    employee_id: int
    action_type: str # e.g., "UPDATE_LOCATION", "RESTART", "SENSITIVITY_CHANGE"
    old_value: Optional[str] = None
    new_value: Optional[str] = None

class CameraActionResponseDTO(BaseModel):
    action_id: int
    camera_id: int
    employee_id: int
    action_type: str
    old_value: Optional[str]
    new_value: Optional[str]
    action_time: datetime
    action_date: date

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('action_time')
    def serialize_time(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    @field_serializer('action_date')
    def serialize_date(self, d: date, _info):
        return d.strftime('%Y-%m-%d')