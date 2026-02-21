from sqlalchemy.orm import Session
from app.db.models import Employee

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, employee_data: dict):
        db_employee = Employee(**employee_data)
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee