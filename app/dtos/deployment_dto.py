from pydantic import BaseModel, ConfigDict, field_serializer
from datetime import datetime
from typing import Optional

class DeploymentCreateDTO(BaseModel):
    camera_id: int
    model_id: int
    deployment_status: str = "Active" # e.g., Active, Retired, Testing
    deployed_by: int # The employee_id of the technician

class DeploymentUpdateDTO(BaseModel):
    deployment_status: Optional[str] = None

class DeploymentResponseDTO(BaseModel):
    deployment_id: int
    camera_id: int
    model_id: int
    deployed_at: datetime
    deployment_status: str
    deployed_by: int

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('deployed_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y-%m-%d %H:%M:%S') # Standard UTC format