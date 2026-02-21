from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse
from app.services.employee_service import EmployeeService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/employees", response_model=EmployeeResponse)
def create_employee(employee_in: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        # 1. Initialize the service with the database session
        service = EmployeeService(db)
        # 2. Call the service to save the DTO data
        return service.register_employee(employee_in)
    except Exception as e:
        # 3. If it crashes, give a clear message instead of a 500 error
        raise HTTPException(status_code=400, detail=str(e))