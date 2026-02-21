from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.dtos.employee_dto import EmployeeCreateDTO, EmployeeResponseDTO, EmployeeUpdateDTO
from app.services.employee_service import EmployeeService

router = APIRouter()

@router.post("/", response_model=EmployeeResponseDTO, status_code=status.HTTP_201_CREATED)
def create_employee(dto: EmployeeCreateDTO, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.create_employee(dto)

@router.get("/", response_model=List[EmployeeResponseDTO])
def list_employees(db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.get_all_employees()

@router.get("/{employee_id}", response_model=EmployeeResponseDTO)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.get_employee(employee_id)

@router.put("/{employee_id}", response_model=EmployeeResponseDTO)
def update_employee(employee_id: int, dto: EmployeeUpdateDTO, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.update_employee(employee_id, dto)

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    service = EmployeeService(db)
    return service.delete_employee(employee_id)

