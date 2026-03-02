from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.employee_service import EmployeeService
from app.dtos.employee_dto import EmployeeCreateDTO, EmployeeUpdateDTO, EmployeeResponseDTO
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/employees", tags=["2. Employee Management"])

# --- ALL ROUTES ARE ADMIN ONLY ---

@router.get("/", response_model=List[EmployeeResponseDTO])
def list_employees(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """List all employees - Strictly Admin Only"""
    return EmployeeService(db).get_all_employees()

@router.get("/{employee_id}", response_model=EmployeeResponseDTO)
def get_employee(employee_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Get employee details - Strictly Admin Only"""
    return EmployeeService(db).get_employee(employee_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmployeeResponseDTO)
def create_employee(dto: EmployeeCreateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Create a new employee/admin - Strictly Admin Only"""
    return EmployeeService(db).create_employee(dto)

@router.put("/{employee_id}", response_model=EmployeeResponseDTO)
def update_employee(employee_id: int, dto: EmployeeUpdateDTO, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Update employee details/roles - Strictly Admin Only"""
    return EmployeeService(db).update_employee(employee_id, dto)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    """Delete an employee - Strictly Admin Only"""
    return EmployeeService(db).delete_employee(employee_id)