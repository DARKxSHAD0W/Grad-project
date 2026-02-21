from pydantic import BaseModel
from typing import Optional

# DTO for Input: What the user sends (Includes password)
class EmployeeCreate(BaseModel):
    full_name: str # [cite: 98-99]
    username: str # [cite: 100-101]
    password: str #
    role: str # [cite: 104-105]

# DTO for Output: What the API shows back (NO password)
class EmployeeResponse(BaseModel):
    employee_id: int # [cite: 97]
    full_name: str # [cite: 98-99]
    username: str # [cite: 100-101]
    role: str # [cite: 104-105]

    class Config:
        from_attributes = True