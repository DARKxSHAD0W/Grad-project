from sqlalchemy.orm import Session
from app.repositories.employee_repo import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate

class EmployeeService:
    def __init__(self, db: Session):
        self.repo = EmployeeRepository(db)

    def register_employee(self, data: EmployeeCreate):
        # Professional logic: convert DTO to dict for the repo
        employee_dict = data.model_dump()
        return self.repo.create(employee_dict)