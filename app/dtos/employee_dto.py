from pydantic import BaseModel, ConfigDict
from typing import Optional

class EmployeeCreateDTO(BaseModel):
    full_name: str
    username: str
    password: str
    role: Optional[str] = "Staff"

class EmployeeUpdateDTO(BaseModel):
    full_name: Optional[str] = None
    role: Optional[str] = None
    # Password updates usually require a separate specialized logic,
    # but we include it here for basic CRUD.
    password: Optional[str] = None

class EmployeeResponseDTO(BaseModel):
    employee_id: int
    full_name: str
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)