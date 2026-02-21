from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.employee_repository import EmployeeRepository
from app.dtos.employee_dto import EmployeeCreateDTO, EmployeeUpdateDTO
from app.core.security import security  # Your Bcrypt helper


class EmployeeService:
    def __init__(self, db: Session):
        self.repository = EmployeeRepository(db)

    def create_employee(self, dto: EmployeeCreateDTO):
        # Encrypt the password before saving
        dto.password = security.hash_password(dto.password)
        return self.repository.create(dto)

    def get_all_employees(self):
        return self.repository.get_all()

    def get_employee(self, employee_id: int):
        employee = self.repository.get_by_id(employee_id)
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
        return employee

    def update_employee(self, employee_id: int, dto: EmployeeUpdateDTO):
        # If the user is updating the password, hash the new one
        if dto.password:
            dto.password = security.hash_password(dto.password)

        employee = self.repository.update(employee_id, dto)
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
        return employee

    def delete_employee(self, employee_id: int):
        success = self.repository.delete(employee_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
        return {"detail": "Employee deleted successfully"}