from sqlalchemy.orm import Session
from app.db.models import Employee
from app.dtos.employee_dto import EmployeeCreateDTO, EmployeeUpdateDTO

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: EmployeeCreateDTO) -> Employee:
        new_employee = Employee(
            full_name=dto.full_name,
            username=dto.username,
            password=dto.password,  # This will be the hashed password from the service
            role=dto.role
        )
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_all(self):
        return self.db.query(Employee).all()

    def get_by_id(self, employee_id: int):
        return self.db.query(Employee).filter(Employee.employee_id == employee_id).first()

    def update(self, employee_id: int, dto: EmployeeUpdateDTO):
        db_employee = self.get_by_id(employee_id)
        if db_employee:
            # Update only the fields that were provided in the request
            update_data = dto.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_employee, key, value)
            self.db.commit()
            self.db.refresh(db_employee)
        return db_employee

    def delete(self, employee_id: int):
        db_employee = self.get_by_id(employee_id)
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()
            return True
        return False