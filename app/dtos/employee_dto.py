from pydantic import BaseModel
from typing import Optional

class EmployeeCreateDTO(BaseModel):
    full_name: str
    username: str
    password: str
    role: str

class EmployeeUpdateDTO(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

class EmployeeResponseDTO(BaseModel):
    # Move this to the top line
    employee_id: int
    full_name: str
    username: str
    password: str
    role: str

    class Config:
        from_attributes = True