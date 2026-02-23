from pydantic import BaseModel, ConfigDict, field_serializer
from datetime import datetime
from typing import Optional

class FireEventCreateDTO(BaseModel):
    camera_id: int
    confidence: float
    message: Optional[str] = None
    image_url: Optional[str] = None

# This is the class your API was looking for!
class FireEventUpdateDTO(BaseModel):
    message: Optional[str] = None
    confidence: Optional[float] = None
    image_url: Optional[str] = None

class FireEventResponseDTO(BaseModel):
    fire_event_id: int
    camera_id: int
    confidence: float
    detected_at: datetime
    message: Optional[str]
    image_url: Optional[str]

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('detected_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S')