from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.employee_repository import EmployeeRepository
from app.dtos.employee_dto import EmployeeCreateDTO, EmployeeUpdateDTO
from app.core.security import security

class EmployeeService:
    def __init__(self, db: Session):
        self.repository = EmployeeRepository(db)

    def get_all_employees(self):
        employees = self.repository.get_all()
        # Sorts alphabetically by full_name
        return sorted(employees, key=lambda x: x.full_name.lower())

    def get_employee(self, employee_id: int):
        employee = self.repository.get_by_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def create_employee(self, dto: EmployeeCreateDTO):
        dto.password = security.hash_password(dto.password)
        return self.repository.create(dto)

    def update_employee(self, employee_id: int, dto: EmployeeUpdateDTO):
        if dto.password:
            dto.password = security.hash_password(dto.password)
        employee = self.repository.update(employee_id, dto)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def delete_employee(self, employee_id: int):
        if not self.repository.delete(employee_id):
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"detail": "Employee deleted successfully"}