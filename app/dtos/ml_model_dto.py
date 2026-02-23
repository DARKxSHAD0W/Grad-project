from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MLModelCreateDTO(BaseModel):
    version: str
    file_path: str
    status: str
    employee_id: int

class MLModelUpdateDTO(BaseModel):
    version: Optional[str] = None
    file_path: Optional[str] = None
    status: Optional[str] = None
    employee_id: Optional[int] = None

class MLModelResponseDTO(BaseModel):
    # 1. ID at the top
    model_id: int
    # 2. Then the rest of the data
    version: str
    status: str
    employee_id: int
    trained_at: datetime
    file_path: str

    class Config:
        from_attributes = True